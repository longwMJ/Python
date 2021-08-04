# 线程池: 一次性开辟一些线程, 直接给线程提交任务, 线程任务多调度交给线程池完成

# ProcessPoolExecutor 进程池 就不写了 ThreadPoolExecutor替换成ProcessPoolExecutor就是了
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def fun(name):
    for i in range(100):
        print(name, i)

if __name__ == '__main__':
    # 创建线程池
    # 5个线程池
    with ThreadPoolExecutor(5) as t:
        # 10个任务
        for i in range(10):
            t.submit(fun, name=f'线程{i}')

    print('123')