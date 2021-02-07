# 反爬机制 UA检测
# UA User-Agent
# 门户网站的服务器会检测对应请求的载体身份标识，如果检测到载体身份标识为某一款浏览器
# 说明这是一个正常的请求
# 如果检测到请求不是基于某一款浏览器
# 说明这是一个不正常的请求，则服务器很有可能拒绝该次请求
# UA伪装 将User-Agent封装到一个字典中
import requests
if __name__ == '__main__':
    # UA 伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    # 1 指定url
    url = 'https://www.baidu.com/s'
    # 处理url携带的参数: 封装到字典中
    kw = input('请输入要查找的关键词：')
    param = {
        'wd': kw
    }
    # 2 对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url = url, params = param,headers = headers)
    # 3 获取响应数据
    page_text = response.text
    # 3 持久化存储
    fileName = kw + '.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

















