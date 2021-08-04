import requests

# https://www.zdaye.com/FreeIPList.html 查看免费ip

# ip 59.55.166.25
# 端口 3256
# 59.55.166.25:3256

proxies = {
    # "http": '',
    "https": 'https://59.55.166.25:3256', # 以前版本是是 59.55.166.25:3256
}

# 没有成功!!!!!!!!!!!
res = requests.get('https://www.baidu.com/', proxies=proxies)
res.encoding = 'utf-8'
print(res.text)

res.close()