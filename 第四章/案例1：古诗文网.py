import requests
from lxml import etree
from 验证码示例代码 import Chaojiying_Client
# 封装识别验证码图片的函数
def getCodeText(imgPath,codeType):
    chaojiying = Chaojiying_Client('ctyring', '***', '912749')  # 用户中心>>软件ID 生成一个替换 96001
    im = open(imgPath, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    res = chaojiying.PostPic(im, codeType)  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    return res
# 将验证码下载到本地
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}
page_text = requests.get(url = url,headers = headers).text
tree = etree.HTML(page_text)
img_src = 'https://so.gushiwen.org/' + tree.xpath('//*[@id="imgCode"]/@src')[0]
img_data = requests.get(url=img_src,headers=headers).content
with open('./code.jpg','wb') as fp:
    fp.write(img_data)
# 调用打码平台的示例程序进行验证码图片数据识别
code_text = getCodeText('code.jpg',1004)
print(code_text['pic_str'])