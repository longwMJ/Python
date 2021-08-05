import time
import asyncio


async def fun():
    print('go 111')
    # 阻塞3秒, cup不为我工作
    # 类似还有 input()    requetsts.get()

    # 协程: 在单线程单条件下, 当程序遇到阻塞时候, 可以选择性切换到其他任务上
    # 当程序出现同步操作时(time.sleep), 异步就中断了 所以我们要用 asyncio.sleep
    # time.sleep(3)

    await asyncio.sleep(3)
    print('very go 111')

async def fun2():
    print('go 222')
    await asyncio.sleep(3)
    print('very go 222')

async def fun3():
    print('go 333')
    await asyncio.sleep(3)
    print('very go 333')


if __name__ == '__main__':
    # fun()
    # asyncio.run(fun())

    t1 = time.time()
    asyncio.run(asyncio.wait(
        [
          fun(),  
          fun2(),  
          fun3(),  
        ]
    ))
    t2 = time.time()
    print(t2 - t1)