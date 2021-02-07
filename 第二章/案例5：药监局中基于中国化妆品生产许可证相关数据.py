# 动态加载数据
# 详情页面的url都是一样的，只有参数id不同
# id可以通过爬取首页ajax请求获得
# 然后域名和id拼接即可
# 但详情页也是ajax请求（套娃）
import requests
import json
import time
if __name__ == '__main__':
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    id_list = []
    res_list = []
    for page in range(1,4):
        page = str(page)
        data = {
            'on' : 'true',
            'page' : page,
            'pageSize' : '15',
            'productName' : '',
            'conditionType' : '1',
            'applyname' : '',
            'applysn' : '',
        }
        response = requests.post(url=url, data=data, headers=headers)
        time.sleep(1)
        json_id = response.json()
        for dic in json_id['list']:
            id_list.append(dic['ID'])
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id' : id
        }
        response = requests.post(url = post_url, headers = headers,data=data).json()
        time.sleep(3)
        res_list.append(response)
    print(res_list)
    # fp = open('./allData.json','w',encoding='utf-8')
    # json.dump(res_list,fp = fp,ensure_ascii=False)