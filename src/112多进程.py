from multiprocessing import Process

# 多进程消耗比较大, 不建议使用

def fun(name):
    for i in range(100):
        print(f'子进程{name}', i)

if __name__ == '__main__':
    # 传参
    p = Process(target=fun, args=('周杰伦',))
    p.start()

    p2 = Process(target=fun, args=('蔡依林',))
    p2.start()

    for i in range(100):
        print('主进程', i)


