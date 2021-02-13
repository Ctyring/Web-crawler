import requests
url = "https://www.baidu.com/s?wd=ip"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}
page_text = requests.get(url = url,headers=headers,proxies={"https://":"175.146.209.36:9999"}).text
with open("./id.html","w",encoding="utf-8") as fp:
    fp.write(page_text)
