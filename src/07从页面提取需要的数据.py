import re
import requests

url = 'https://movie.douban.com/top250'

newheaders = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

res = requests.get(url, headers=newheaders)


resText = res.text

# print(resText)

# 解析数据

obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>', re.S)

resFind = obj.finditer(resText)

for i in resFind:
    print(i.group("name"))








