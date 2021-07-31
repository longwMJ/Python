

# 运行py文件: shift + 回车 , 或者点击右上角有三角形

from urllib.request import urlopen

url = 'https://blog.csdn.net/qq_42098115/article/details/106793000'

resp = urlopen(url)

# name = 'xue'

# print(name)
print(resp.read().decode("utf-8"))



