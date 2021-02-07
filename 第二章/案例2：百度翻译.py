#  Ajax是一项用于网站开发的重要技术。 可以在不刷新网页的情况下,与服务端交互。
#  百度翻译我们输入文字之后就会发起Ajax请求
#  对每个字符发起Ajax请求（post请求）
#  post请求携带了数据
#  响应的数据时json数据
import requests
import json
if __name__ == '__main__':
    # 指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # ua伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    # 参数处理
    word = input("请输入要翻译的内容")
    data = {
        'kw': word
    }
    # 请求发送
    response = requests.post(url = post_url,data=data,headers = headers)
    # 获取响应数据:json方法返回的是obj，确认响应数据时json才可以
    dic_obj = response.json()
    # 持久化存储
    # print(dic_obj['data'])
    fileName = word + '.json'
    fp = open(fileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp = fp,ensure_ascii=False)