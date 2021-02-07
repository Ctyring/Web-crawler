# 爬虫会用到两个模块
#       1 urllib 模块         古老，繁琐
#       2 requests 模块       新兴，简洁（主要学习这个模块）
# requests模块 python中原生的基于网络请求的模块
#       功能强大 简单便捷 效率极高
#       作用：模拟浏览器发请求
#       掌握requests就能掌握爬虫的半壁江山
#   如何使用：（requests模块的编码流程）
#       1 指定url（输入网址）
#       2 发起请求（get，post）
#       3 获取相应数据
#       4 持久化存储
# 实战编码：
#       爬取搜狗首页的页面数据
# 1 导入模块
import requests
if __name__ == '__main__':
    # 2 指定url
        url = 'https://www.sogou.com/'
    # 3 发起请求
        response = requests.get(url = url)
    # 4 获取响应数据(.txt返回字符串形式的响应数据)
        page_txt = response.text
        print(page_txt)
    # 5 持久化存储
        with open('./sougou.html','w',encoding = 'utf-8') as fp:
            fp.write(page_txt)
        print('爬取结束')