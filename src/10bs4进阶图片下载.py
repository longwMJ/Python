from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup
# import os

import time

url = 'https://www.umei.net/bizhitupian/weimeibizhi/'

# pathVal = os.path.dirname(os.path.abspath('.'))

# print(pathVal)

res = requests.get(url)
res.encoding = 'utf-8'

main_page = BeautifulSoup(res.text, 'html.parser')

alist = main_page.find('div', class_='TypeList').find_all('a')

for a in alist:
    child_href = 'https://www.umei.net' + a.get('href')
    # print(child_href)

    # https://www.umei.net/bizhitupian/weimeibizhi/225259.htm

    child_page = requests.get(child_href)
    child_page.encoding = 'utf-8'
    child_page_text = child_page.text

    # 从子页面拿到下载途经
    child_page_bs = BeautifulSoup(child_page_text, 'html.parser')
    img_src = child_page_bs.find('p', align='center').find('img').get('src')
    img_name = img_src.split('/')[-1]
    # 下载img
    img_res = requests.get(img_src)
    # 拿到到是字节
    # img_res.content

    with open(img_name, mode='wb') as f:
    # with open(pathVal+'/img/'+img_name, mode='wb') as f:
        f.write(img_res.content)
        f.close()
        child_page.close()
        # 休息3秒  这样对服务器友好一些
        time.sleep(3)

res.close()
print('all over')

