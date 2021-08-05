
import asyncio

imgUrls = [
    'https://img1.baidu.com/it/u=4138100449,883826593&fm=15&fmt=auto&gp=0.jpg',
    'https://img0.baidu.com/it/u=202074831,1321913496&fm=15&fmt=auto&gp=0.jpg',
    'https://img2.baidu.com/it/u=566719294,1419140494&fm=15&fmt=auto&gp=0.jpg',
]


async def aiodwonload():

    asyncio.ClientSession()


async def main():
    tasks = []
    for url in imgUrls:
        tasks.append(aiodwonload(url))
        # ????? 未完成
    await async.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())
