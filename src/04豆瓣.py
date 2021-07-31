
import requests
from requests.api import get

# https://fanyi.baidu.com/#en/zh/dog

url = 'https://movie.douban.com/j/chart/top_list'
urlAll = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20'


# 设置get请求参数
# reqData = {
#     'type': 24,
#     'interval_id': '100: 90',
#     'action': '',
#     'start': 0,
#     'limit': 20,
# }
reqData = {
    "type": "24",
    # 参数值要规范上面我写成 100: 90 结果没有数据
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20,
}

# res = requests.get(url=url, params=reqData)

# # print(res.request.url)

# # 查看内容, 发现什么也没有, 可能是有反爬虫
# print(res.text)

# # 查看默认 headers
# # {'User-Agent': 'python-requests/2.26.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
# print(res.request.headers)


newheaders = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

res = requests.get(url=url, params=reqData, headers=newheaders)
# res = requests.get(url=urlAll, headers=newheaders)

print(res.request.path_url)
print(res.text)

# 记得关掉爬虫!!!! 避免请求次数过多的问题
res.close()
