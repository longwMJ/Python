from threading import Thread

class myThread(Thread):
    def run(self): #固定写法 
        for i in range(100):
            print('子线程打印:', i)


if __name__ == '__main__':

    
    t = myThread()

    # t.run() 错误写法 方法调用类,  -》 单线程
    # t.run()

    t.start()

    # 单线程
    for i in range(100):
        print('主线程打印:', i)



    # 子线程打印: 0
    # 子线程打印: 1
    # 主线程打印: 0
    # 子线程打印: 2
    # 主线程打印: 1
    # 子线程打印: 3
    # 主线程打印: 2
    # 子线程打印: 4
    # 主线程打印: 3
    # 子线程打印: 5
    # 主线程打印: 4






