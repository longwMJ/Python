
# 安装插件

# pip install requests
import requests 


# 动态查询
query = input("输入一位明星名字:")

# 周杰伦
# url = 'https://www.sogou.com/web?query=%E5%91%A8%E6%9D%B0%E4%BC%A6' 


url = f'https://www.sogou.com/web?query={query}' 

# res =  requests.get(url)

# # res:  <Response [200]>


# # 页面源代码
# print(res.text)

# 里面有一段文字: 
# 用户您好，我们的系统检测到您网络中存在异常访问请求。<br>此验证码用于确认这些请求是您的正常行为而不是自动程序发出的，需要您协助验证


# 从浏览器控制台获取User-Agent

# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36

# User-Agent 告诉服务器当前是以什么设备访问, 如果没有, 可能被认为爬虫
xueheaders = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

resHeaders =  requests.get(url, headers=xueheaders)

print(resHeaders.text)