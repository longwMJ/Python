import requests
import parsel
from tqdm import tqdm
import time
import pandas as pd

a_url = 'https://www.biquges.com'

url = 'https://www.biquges.com/66_66497'

search_url = 'https://www.biquges.com/modules/article/search.php'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

def save(name, title, content):
    # with open(name + '.txt', mode='a', encoding='utf-8') as f:
    with open(title + '.txt', mode='a', encoding='utf-8') as f:
        f.write(title)
        f.write('\n')
        f.write(content)
        f.write('\n')
        f.close()

def getChildResText(html_url):
    res = requests.get(url=html_url, headers=headers)
    text = res.text
    res.close()
    return text

def saveText(url, title):
    childText = getChildResText(url)
    childSelector = parsel.Selector(childText)
    childName = childSelector.css('.bookname h1::text').get()
    childContentList = childSelector.css('#content::text').getall()
    # 转字符串 强转  用''.join()
    childContentJoin = ''.join(childContentList)
    print('novel_title', title)
    print('childName', childName)
    if childName is None:
        saveText(url=url, title=title)
    else:
        save(title, childName, childContentJoin)

def getRes(html_url):
    res = requests.get(url=html_url, headers=headers)
    selector = parsel.Selector(res.text)
    novel_title = selector.css('#info h1::text').get()
    href = selector.css('#list dd a::attr(href)').getall()
    hrefs = href[ 9 - len(href):]
    for i in tqdm(hrefs):
        link_url = a_url + i
        saveText(url=link_url, title=novel_title)

    res.close()
    print('over')

# 程序主入口 main
if __name__ == '__main__':
    while True:
        word = input('请输入要下载的小说名或者作者名:')
        data = {
            # 'searchkey': '登天',
            'searchkey': word,
            'searchtype': 'articlename'
        }

        # resSearch.text 得到的是乱码
        resSearch = requests.post(url=search_url, headers=headers, data=data)
        # 自动转码
        resSearch.encoding = resSearch.apparent_encoding
        # 获取小说名字, 小说id 作者名字..
        resSearchSelector = parsel.Selector(resSearch.text)
        resSearch.close()
        # 提取查询的每一个小说 按理说, 一个页面只有一个唯一的id值, 这里却有多个, html不够好
        nrs = resSearchSelector.css('#nr')
        searchlist = []
        for i in nrs:
            name = i.css('#nr .odd a::text').get()
            # /58_58594/ -> 58_58594
            id = i.css('#nr .odd a::attr(href)').get().split('/')[1]
            authorName = i.css('#nr td:nth-child(3)::text').get()
            dit = {
                '书名': name,
                'id': id,
                '作者': authorName,
            }
            searchlist.append(dit)

        print(f'搜索到{len(searchlist)}条内容:')
        pd_searchlist = pd.DataFrame(searchlist)

        print(pd_searchlist)

        if len(searchlist):
            num = input('请输入你要下载小说的序号:')
            cuId = searchlist[int(num)]['id']
            novel_url = f'{a_url}/{cuId}'
            getRes(html_url=novel_url)
            again =input('是否继续下载小说(y/n):')
            if again == 'y':
                continue
            else:
                break
        else:
            print('没有搜索结果, 请重新输入')
