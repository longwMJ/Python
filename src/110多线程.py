from threading import Thread

def fun():
    for i in range(100):
        print('runUUUU:', i)

if __name__ == '__main__':

    # 多线程
    t = Thread(target=fun)
    # 开始执行该线程
    t.start()



    # 单线程
    fun()






