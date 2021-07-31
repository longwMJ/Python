
import requests 

# https://fanyi.baidu.com/#en/zh/dog

url = 'https://fanyi.baidu.com/sug'

q = input("请输入你要翻译的英文单词:")


# 字典 我认为是参数的意思
resData =  {
    "kw": f'{q}'
}

res = requests.post(url, data=resData)
print(res.json())