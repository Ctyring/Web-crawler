import requests
from lxml import  etree
import os
if __name__ == '__main__':
    url = 'http://pic.netbian.com/4kyouxi/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    response = requests.get(url = url,headers=headers)
    # 手动设定响应数据的编码格式 方案1
    # response.encoding = 'utf-8'
    page_text = response.text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')
    if not os.path.exists('./youxi'):
        os.mkdir('./youxi')
    for li in li_list:
        img_src = 'http://pic.netbian.com/' + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        # 方案2 遇到乱码两个换着试试
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        img_data = requests.get(url = img_src,headers=headers).content
        img_path = './youxi/'+img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(img_name,"下载成功")
