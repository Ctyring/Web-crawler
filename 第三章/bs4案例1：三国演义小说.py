import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url,headers=headers).text
    soup = BeautifulSoup(page_text,'lxml')
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail = 'https://www.shicimingju.com' + li.a['href']
        detail_page_text = requests.get(url = detail,headers=headers).content.decode('utf-8')
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        detail_li_list = detail_soup.find('div',class_ = 'chapter_content').text
        fp.write(title+':'+detail_li_list+'\n')
        print("{}已成功下载".format(title))

