import requests
from lxml import etree
import time
def novel(url):
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }
    url = url
    # img_name = img_name.encode('iso-8859-1').decode('gbk')
    html = requests.get(url,headers=headers).text
    html = html.encode('iso-8859-1').decode('utf-8')
    tree = etree.HTML(html)
    title = tree.xpath('//*[@id="info"]/h1/text()')[0]
    url_list = tree.xpath('//*[@id="list"]/dl/dd/a/@href')
    title = './'+title+'.txt'
    fp = open(title,'w',encoding='utf-8')
    for url in url_list:
        url = 'http://www.paoshuzw.com/' + url
        html = requests.get(url=url,headers=headers).text
        html = html.encode('iso-8859-1').decode('utf-8')
        tree = etree.HTML(html)
        novel_text_list = tree.xpath('// *[ @ id = "content"] / text()')
        for novel_text in novel_text_list:
            novel_text = novel_text[4:]
            fp.write(novel_text)
        time.sleep(1)
if __name__ == '__main__':
    print("请输入要下载小说的url：")
    url = input()
    novel(url)
    print("小说已全部下载完毕")