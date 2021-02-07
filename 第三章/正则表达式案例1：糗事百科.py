import requests
import re           # 正则的查找
import json
import os           # 用来创建文件夹
# text 返回字符串响应数据 content 返回二进制响应数据 json() 返回对象类型响应数据
if __name__ == '__main__':
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    # 创建文件夹
    if not os.path.exists('./qiutu'):
        os.mkdir('./qiutu')
    # 指定url
    url = 'https://www.qiushibaike.com/imgrank/page/{}/'
    # ua伪装
    for pageNum in range(1,3):
        new_url = url.format(pageNum)
        page_text = requests.get(url=new_url, headers=headers).text
        # 然后用聚焦爬虫解析数据
        # 正则
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex,page_text,re.S)
        # print(img_src_list)
        for src in img_src_list:
            src = 'https:' + src
            res = requests.get(url=src,headers=headers).content
            # 生成图片名称    根据斜杠切分，取最后一个
            img_name = src.split('/')[-1]
            img_path = './qiutu/'+img_name
            with open(img_path,"wb") as fp:
                fp.write(res)


