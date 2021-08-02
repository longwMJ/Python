import requests
import parsel
from tqdm import tqdm
import time

url = 'https://www.biquges.com/66_66497'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

def save(name, title, content):
    with open(name + '.txt', mode='a', encoding='utf-8') as f:
        f.write(title)
        f.write('\n')
        f.write(content)
        f.write('\n')
        f.close()

def getChildRes(html_url):
    res = requests.get(url=html_url, headers=headers)
    return res

def getRes(html_url):
    res = requests.get(url=html_url, headers=headers)
    selector = parsel.Selector(res.text)
    novel_title = selector.css('#info h1::text').get()
    print(novel_title)
    hrefs = selector.css('#list dd a::attr(href)').getall()

    # print(hrefs)

    for i in tqdm(hrefs):
        link_url = 'https://www.biquges.com' + i
        childText = getChildRes(link_url).text
        # print(childText)
        childSelector = parsel.Selector(childText)
        childName = childSelector.css('.bookname h1::text').get()
        childContentList = childSelector.css('#content::text').getall()
        # 转字符串 强转  用''.join()
        childContentJoin = ''.join(childContentList)
        # print(childContentJoin)
        save(novel_title, childName, childContentJoin)
        time.sleep(1)
        # break
    
    res.close()
    print('over')

getRes(html_url=url)



