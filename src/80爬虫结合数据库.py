import requests
import parsel
from tqdm import tqdm
from multiprocessing import Pool
import pandas as pd
from functools import partial
import sqlite3

a_url = 'https://www.biquges.com'

url = 'https://www.biquges.com/66_66497'

search_url = 'https://www.biquges.com/modules/article/search.php'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

def save(title, content):
    conn = sqlite3.connect('novel.db')
    cursor = conn.cursor()

    sql = "UPDATE NovelDBPABC SET  Content = ? WHERE Title = ?"

    cursor.execute(sql, (content,  title))

   # 提交事物
    conn.commit()

    #关闭游标
    cursor.close()

    #关闭连接
    conn.close()

def getChildResText(html_url):
    res = requests.get(url=html_url, headers=headers)
    text = res.text
    res.close()
    return text

def saveText(url):
    herf_url = a_url + url
    childText = getChildResText(herf_url)
    childSelector = parsel.Selector(childText)
    childTitle = childSelector.css('.bookname h1::text').get()
    childContentList = childSelector.css('#content::text').getall()
    # 转字符串 强转  用''.join()
    childContentJoin = ''.join(childContentList)
    if childTitle is None:
        saveText(url=url)
    else:
        save(title=childTitle.strip(), content=childContentJoin)

def getRes(html_url):
    res = requests.get(url=html_url, headers=headers)
    selector = parsel.Selector(res.text)
    novel_Name = selector.css('#info h1::text').get()
    # 所有章节
    href = selector.css('#list dd a::attr(href)').getall()
    hrefs = href[9 - len(href):]
    # 所有章节
    aTitle = selector.css('#list dd a::text').getall()
    aTitles = aTitle[9 - len(aTitle):]

    conn = sqlite3.connect('novel.db')

    # 创建游标
    cursor = conn.cursor()

    sql = 'CREATE TABLE NovelDBPABC(id integer PRIMARY KEY autoincrement, Name  TEXT, title TEXT, content TEXT)'
    cursor.execute(sql)

    sql = "INSERT INTO NovelDBPABC(Name, Title) VALUES(?, ?)"

    # 创建游标
    cursor = conn.cursor()

    for t in aTitles:
        cursor.execute(sql, (novel_Name, t.strip()))

    # 提交事物
    conn.commit()

    #关闭游标
    cursor.close()

    #关闭连接
    conn.close()

    # 固定传入title参数 
    # saveText_work = partial(saveText, title = novel_Name)
    saveText_work = partial(saveText)
    with Pool(2) as p:
      list(tqdm(p.imap(saveText_work, hrefs), total=len(hrefs)))

    conn = sqlite3.connect('novel.db')

    # 创建游标
    cursor = conn.cursor()

    sql = "select * from NovelDBPABC"

    content_text = ''
    values = cursor.execute(sql)
    for i in values:
        # print(i)
        cc = ''.join(i[3])
        content_text = f'{content_text}{i[2]}\n\n\n{cc}\n\n\n'
       
    with open(novel_Name + '.txt', mode='a', encoding='utf-8') as f:
        f.write(content_text)
        f.close()

    #删除表格Student
    cursor.execute("DROP TABLE NovelDBPABC")

    # 提交事物
    conn.commit()

    #关闭游标
    cursor.close()

    #关闭连接
    conn.close()

    res.close()
    print('over')

# 程序主入口 main
if __name__ == '__main__':
    while True:
        word = input('请输入要下载的小说名或者作者名:')
        data = {
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
            again = input('是否继续下载小说(y/n):')
            if again == 'y':
                continue
            else:
                break
        else:
            print('没有搜索结果, 请重新输入')
