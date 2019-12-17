# -*- encoding: utf8 -*-

"""
3.2 信号量 Semaphore
上面的例子中，统计用的计数器是唯一的资源，因此使用了只能被一个线程获取的互斥锁。
假如共享的资源有多个，多线程竞争时一般使用信号量（Semaphore）同步。
信号量有一个初始值，表示当前可用的资源数，多线程执行过程中会通过 acquire() 和 release() 操作，动态的加减信号量。
比如，有30个工人都需要电锤，但是电锤总共只有5把。使用信号量（Semaphore）解决竞争的代码如下：
"""
import time
import threading

S= threading.Semaphore(5)   #有5把电锤可供使用

def us_heammer(id):
    """线程函数"""

    S.acquire() #P操作，阻塞式请求电锤
    time.sleep(0.2)
    print('%d号刚刚用完电锤'%id)
    S.release() #V操作，释放资源（信号量加1）

def demo():
    threads = list()
    for i in range(30): #有30名工人要求使用电锤
        threads.append(threading.Thread(target=us_heammer, args=(i, )))
        threads[-1].start()

    for t in threads:
        t.join()

    print('所有线程工作结束')

if __name__ == '__main__':
    demo()