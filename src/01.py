

# 运行py文件: shift + 回车 , 或者点击右上角有三角形

from urllib.request import urlopen

url = 'https://blog.csdn.net/qq_42098115/article/details/106793000'
# url = 'https://www.baidu.com/'

resp = urlopen(url)

# name = 'xue'

# print(name)
print(resp.read().decode("utf-8"))


# 保存网页
# with open("demo.html", mode="w") as f:
#     f.write(resp.read().decode("utf-8"))
#     print("over")

# val = resp.read().decode("utf-8")

with open('demo7.html', 'w') as f:
    f.write(resp.read().decode("utf-8"))
    # f.write(val)
    # f.flush()  # 强制将缓存区内容写进文件
    print("over ok")
