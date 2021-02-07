import requests
import json
if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    param = {
        'cname':'',
        'pid':'',
        'keyword': '洛阳',
        'pageIndex': '1',
        'pageSize': '10',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    response = requests.get(url = url,params=param,headers=headers)
    list_data = response.json()
    fp = open('./KFC.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)
    print(list_data)