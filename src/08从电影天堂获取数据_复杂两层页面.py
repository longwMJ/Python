import requests
import re

child_href_list = []

url = 'https://www.dytt89.com/'

erUrl = 'https://www.dytt89.com'

# verify=False 去除安全验证
res = requests.get(url, verify=False)

# 指定 网页的 字符集
res.encoding = 'gb2312'

# print(res.text)


with open('dytt.html', 'w') as f:
    f.write(res.text)
    print("over ok")

reObj = re.compile(r'2021必看热片.*?<ul>(?P<newUl>.*?)</ul>', re.S)
aObj = re.compile(r"<a href='(?P<href>.*?)'", re.S)

# <td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="magnet:?xt=urn:btih:35c6652f69d73ae69d918cc9def27d7e83d239eb&amp;dn=[电影天堂www.dytt89.com]哆啦A梦：伴我同行2-2021_BD国粤日三语中字.mp4&amp;tr=http://t.t789.me:2710/announce&amp;tr=http://t.t789.co:2710/announce&amp;tr=http://t.t789.vip:2710/announce">magnet:?xt=urn:btih:35c6652f69d73ae69d918cc9def27d7e83d239eb&amp;dn=[电影天堂www.dytt89.com]哆啦A梦：伴我同行2-2021_BD国粤日三语中字.mp4</a></td>
# caObj = re.compile(r'◎片　　名(?P<movieName>.*?)<br>.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">')
caObj = re.compile(r'片　　名(?P<movieName>.*?)<')

reFind = reObj.finditer(res.text)

print(reFind)

for i in reFind:
    urlText = i.group('newUl')
    print(urlText)
    hrefFind = aObj.finditer(urlText)
    for j in hrefFind:
        child_href = erUrl + j.group('href')
        print(child_href)
        child_href_list.append(child_href)


print(child_href_list)

for i in child_href_list:
    child_res = requests.get(i, verify=False)
    child_res.encoding = 'gb2312'
    # print(child_res.text)

    # 解析有问题, 后面再想办法吧
    varUrl = caObj.search(child_res.text)
    print(varUrl.group("movieName"))
    # print(varUrl.group("download"))

res.close()
f.close()

