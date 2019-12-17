# -*- encoding: utf8 -*-
"""
3.3 事件Event
想象我们每天早上上班的场景：为了不迟到，总得提前几分钟（我一般都会提前30分钟）到办公室，打卡之后，一看表，
还不到工作时间，大家就看看新闻、聊聊天啥的；工作时间一到，立马开工。如果有人迟到了呢，自然就不能看新闻聊天了，得立即投入工作中。
这个场景中，每个人代表一个线程，工作时间到，表示事件(Event)发生。
事件发生前，线程会调用 wait() 方法阻塞自己（对应看新闻聊天），一旦事件发生，会唤醒所有调用 wait() 而进入阻塞状态的线程。
"""
import time
import threading

E = threading.Event()   #创建事件

def work(id):
    """线程函数"""

    print('<%d号员工>上班打卡'%id)
    if E.is_set():  #已经到点了
        print('<%d号员工>迟到了'%id)
    else:   #还不到点
        print('<%d号员工>浏览新闻中...'%id)
        E.wait()    #等上班铃声

    print('<%d号员工>开始工作了...'%id)
    time.sleep(10)  #工作10S后下班
    print('<%d号员工>下班了'%id)

def demo():
    E.clear()   #设置为“未到上班时间”
    threads = list()

    for i in range(3):  #3人提前到公司打卡
        threads.append(threading.Thread(target=work, args=(i, )))
        threads[-1].start()

    time.sleep(5)   #5秒钟后上班时间到
    E.set()

    time.sleep(5)   #5秒钟后，大佬(9号)到
    threads.append(threading.Thread(target=work, args=(9, )))
    threads[-1].start()

    for t in threads:
        t.join()

    print('都下班了，关灯关门走人')

if __name__ == '__main__':
    demo()
