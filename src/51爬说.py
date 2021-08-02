import requests
import parsel
from bs4 import BeautifulSoup

url = 'https://www.biquges.com/66_66497'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

# res = requests.get(url=url, headers=headers)


# <Response [200]>
# print(res)

def getRes(html_url):
    res = requests.get(url=html_url, headers=headers)
    selector = parsel.Selector(res.text)
    novel_title = selector.css('#info h1::text').get()
    print(novel_title)




getRes(html_url=url)



