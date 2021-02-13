import http.client
import urllib
import requests
import time
import hashlib
import random
import urllib.request
import urllib.parse
import json
import execjs
import re
import ssl
import sys

opto = 2

def youdao(s):
    fr = ["xxx","auto","zh-CHS","en","de","ja"]
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    i = s
    lts = int(time.time() * 1000)
    salt = lts * 10 + random.randint(0, 9)
    lts = str(lts)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-599080939@10.108.160.105; OUTFOX_SEARCH_USER_ID_NCOO=359883062.9839014; JSESSIONID=aaaMIFcnqlp6Q9oS62tEx; JSESSIONID=abcDlYZpHIFPTalq45tEx; _ntes_nnid=66e340e73938fbafbe8538eb83beed1c,1613094159923; SESSION_FROM_COOKIE=test; UM_distinctid=17793f165ac5b2-0033f4acc63d58-53e3566-144000-17793f165ad470; ___rl__test__cookies=' + str(
            salt)
    }
    sign_str = 'new-fanyiweb' + str(salt) + 'ydsecret://newfanyiweb.doctran/sign/0j9n2{3mLSN-$Lg]K4o0N2}' + i
    sign = hashlib.md5(sign_str.encode('utf8')).hexdigest()
    data = {
        'i': i,
        'sign': sign,
        'salt': salt,
        'from': 'auto',
        'to': fr[opto+1],
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'lts': lts,
        'bv': '3da01a09873456cfb5dba05f2124b148',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }
    response = requests.post(url=url, data=data, headers=headers).json()
    return response['translateResult'][0][0]['tgt']
def baidu(s):
    fr = ["xxx", "auto", "zh", "en", "de", "jp"]
    appid = '***'  # 填写你的appid
    secretKey = '***'  # 填写你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = 'auto'  #原文语种
    toLang = fr[opto+1]   #译文语种
    salt = random.randint(32768, 65536)
    q = s
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

        return (result['trans_result'][0]['dst'])

    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()


ssl._create_default_https_context = ssl._create_unverified_context


class GoogleTrans(object):
    def __init__(self):
        self.url = 'https://translate.google.cn/translate_a/single'
        self.TKK = "434674.96463358"  # 随时都有可能需要更新的TKK值

        self.header = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cookie": "NID=188=M1p_rBfweeI_Z02d1MOSQ5abYsPfZogDrFjKwIUbmAr584bc9GBZkfDwKQ80cQCQC34zwD4ZYHFMUf4F59aDQLSc79_LcmsAihnW0Rsb1MjlzLNElWihv-8KByeDBblR2V1kjTSC8KnVMe32PNSJBQbvBKvgl4CTfzvaIEgkqss",
            "referer": "https://translate.google.cn/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
            "x-client-data": "CJK2yQEIpLbJAQjEtskBCKmdygEIqKPKAQi5pcoBCLGnygEI4qjKAQjxqcoBCJetygEIza3KAQ==",
        }

        self.data = {
            "client": "webapp",  # 基于网页访问服务器
            "sl": "auto",  # 源语言,auto表示由谷歌自动识别
            "tl": "vi",  # 翻译的目标语言
            "hl": "zh-CN",  # 界面语言选中文，毕竟URL都是cn后缀了，就不装美国人了
            "dt": ["at", "bd", "ex", "ld", "md", "qca", "rw", "rm", "ss", "t"],  # dt表示要求服务器返回的数据类型
            "otf": "2",
            "ssel": "0",
            "tsel": "0",
            "kc": "1",
            "tk": "",  # 谷歌服务器会核对的token
            "q": ""  # 待翻译的字符串
        }

        with open('token.js', 'r', encoding='utf-8') as f:
            self.js_fun = execjs.compile(f.read())

        # 构建完对象以后要同步更新一下TKK值
        # self.update_TKK()

    def update_TKK(self):
        url = "https://translate.google.cn/"
        req = urllib.request.Request(url=url, headers=self.header)
        page_source = urllib.request.urlopen(req).read().decode("utf-8")
        self.TKK = re.findall(r"tkk:'([0-9]+\.[0-9]+)'", page_source)[0]

    def construct_url(self):
        base = self.url + '?'
        for key in self.data:
            if isinstance(self.data[key], list):
                base = base + "dt=" + "&dt=".join(self.data[key]) + "&"
            else:
                base = base + key + '=' + self.data[key] + '&'
        base = base[:-1]
        return base

    def query(self, q, lang_to=''):
        self.data['q'] = urllib.parse.quote(q)
        self.data['tk'] = self.js_fun.call('wo', q, self.TKK)
        self.data['tl'] = lang_to
        url = self.construct_url()
        req = urllib.request.Request(url=url, headers=self.header)
        response = json.loads(urllib.request.urlopen(req).read().decode("utf-8"))
        targetText = response[0][0][0]
        originalText = response[0][0][1]
        originalLanguageCode = response[2]
        return targetText


def google(s):
    fr = ["xxx","auto","zh-CN","en","de","ja"]
    if opto == 1:
        s = GoogleTrans().query(s,'zh-CN')
    if opto == 2:
        s = GoogleTrans().query(s,'en')
    return s
op = 0
if __name__ == '__main__':
    while(True):
        while(True):
            print("请选择选项：【1】开始翻译 【2】调整模式")
            op = int(input())
            if op == 2:
                print("请选择目标语言：【1】中文 【2】英语")
                opto = int(input())
            if op == 1:
                break
        while(True):
            print("请输入要翻译的内容:")
            s = input()

            print("谷歌翻译结果:{}".format(google(s)))
            time.sleep(1)
            print("有道翻译结果:{}".format(youdao(s)))
            time.sleep(1)
            print("百度翻译结果:{}".format(baidu(s)))
            print("请选择选项：【1】继续翻译 【2】打开菜单 【3】退出")
            op = int(input())
            if op == 2 :
                break
            if op == 3:
                sys.exit()
    # while(True):
    #     print("【1】开始翻译 【2】调整模式 【3】退出")
    #     op = int(input())
    #     if(op == 3):
    #         sys.exit()
    #     elif op == 2:
    #         print("【1】汉译英 【2】英译汉")
    #         langop = input()
    #         if()
    #     else:
    #         print("请输入要翻译的内容")
    #         s = input()
    #         # print("百度翻译结果:{}".format(baidu(s)))
    #         print("谷歌翻译结果:{}".format(google(s)))
    #         print("有道翻译结果:{}".format(youdao(s)))