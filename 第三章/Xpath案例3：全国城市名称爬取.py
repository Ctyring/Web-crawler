import requests
from lxml import etree
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url = url,headers = headers).text
    tree = etree.HTML(page_text)
    host_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    all_city_names = []
    for li in host_li_list:
        hot_cith_name = li.xpath('./a/text()')[0]
        all_city_names.append(hot_cith_name)
    city_names_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    for li in city_names_list:
        city_name = li.xpath('./a/text()')[0]
        all_city_names.append(city_name)
    print(all_city_names)
# 热门和全部同时获取
# a_list = tree.xpath('//div[@class="bottom"]/ul/li | //div[@class="bottom"]/ul/div[2]/li')