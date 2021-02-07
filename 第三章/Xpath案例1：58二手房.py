import requests
from lxml import  etree
if __name__ == '__main__':
    url = 'https://fy.58.com/ershoufang/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text
    print(page_text)
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//section[@class="house-list-wrap"]/li')
    print(li_list)
    fp = open('58.txt','w',encoding='utf-8')
    for li in li_list:
        # 局部解析要加点
        title = li.xpath('./div[2]/h2/a/text()')[0]
        fp.write(title+'\n')
