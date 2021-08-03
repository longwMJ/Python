import requests
from concurrent.futures import ThreadPoolExecutor
from time import perf_counter


# 开设线程 (多少条)
n_threads = 5

# 缓冲区大小
buffer_size = 1024

# # 下载处理函数
# def download_img(url):
#     res = requests.get(url, stream=True)
#     # 文件名
#     filename = url.split('/')[-1]
#     with open(filename, 'wb') as f:
#         for i in res.iter_content(buffer_size):
#             f.write(i)
#             f.close()
#     res.close()
# 下载处理函数
def download_img(url):
    # res = requests.get(url, stream=True)
    res = requests.get(url)
    # 文件名
    filename = url.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(res.content)
        f.close()
        res.close()

if __name__ == '__main__':
    urls = [
        'https://wx3.sinaimg.cn/mw690/a7295e45gy1gt36eofxe3j20zk0np7gn.jpg',
        'https://wx2.sinaimg.cn/mw690/a7295e45gy1gt36f3l2sbj20nm0exgof.jpg',
        'https://wx1.sinaimg.cn/mw690/a7295e45gy1gt36eovjbsj20zk0nph0f.jpg',
        'https://wx3.sinaimg.cn/mw690/a7295e45gy1gt36epghi3j20zk1hctw2.jpg',
        'https://wx1.sinaimg.cn/mw690/a7295e45gy1gt36eqsj9qj20rs0ic40g.jpg',
        'https://wx4.sinaimg.cn/mw690/a7295e45gy1gt36epy5faj20zk1hctty.jpg',
        'https://wx1.sinaimg.cn/mw690/a7295e45gy1gt36f40oycj20nm0eyq61.jpg',
        'https://wx3.sinaimg.cn/mw690/a7295e45gy1gt36eqg2mqj20zk1hckhf.jpg',
        'https://wx3.sinaimg.cn/mw690/a7295e45gy1gt36f4lg3aj20nm0fotcw.jpg',
    ]

    t = perf_counter()

    # 单线程 4.48s
    # for url in urls:
    #     download_img(url)
    # 



    # 多线程 1.59s
    with ThreadPoolExecutor(max_workers=n_threads) as pool:
        pool.map(download_img, urls)
        

    print(f'花费时间:{perf_counter() - t:.2f}s')         