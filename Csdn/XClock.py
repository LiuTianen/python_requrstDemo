# -*- encoding:utf-8 -*-

"""
3.1 线程锁 Lock
前几天，我想在一个几百人的微信群里统计喜欢吃苹果的人数。
有人说，大家从1开始报数吧，并敲了起始数字1，立马有人敲了数字2，3
。但是统计很快就进行不下去了，因为大家发现，有好几个人敲4，有更多的人敲5。

这就是典型的资源竞争冲突：统计用的计数器就是唯一的资源，很多人（子线程）都想取得写计数器的资格。
怎么办呢？Lock（互斥锁）就是一个很好的解决方案。
Lock只能有一个线程获取，获取该锁的线程才能执行，否则阻塞；执行完任务后，必须释放锁。
"""
import time
import threading

lock = threading.Lock() #创建互斥锁
counter = 0 #计数器

def hello():
    """线程函数"""

    global counter

    if lock.acquire():   #请求互斥锁，如果被占用，则阻塞，直至获取到锁
        time.sleep(0.2)
        counter += 1
        print('我是第%d个'%counter)

    lock.release()  #释放互斥锁

def demo():
    threads = list()
    for i in range(30): #假设群里有30人，都喜欢吃苹果
        threads.append(threading.Thread(target=hello))
        threads[-1].start()

    for t in threads:
        t.join()

    print('统计完毕，共有%d人'%counter)

if __name__ == '__main__':
    demo()