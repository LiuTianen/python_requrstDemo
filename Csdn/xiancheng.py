"""
你（主线程）启动3个子线程，名字分别是A、B、C。
其中A线程启动后，你要先观察5秒钟，再启动其他线程。
每个子线程的任务是每隔指定时间间隔就向你问好，
并报上自己的名字，你呢，只管睡觉。30秒后，你醒了。你逐一检查了各个子线程的工作状态之后，结束运行。
"""

import time
import threading

def hello(name, t):
    """线程函数"""

    for i in range(10):
        print('Hello, 我是小%s'%name)
        time.sleep(t)

def demo():
    A = threading.Thread(target=hello, args=('A',1), name='A')
    B = threading.Thread(target=hello, args=('B',2), name='B')
    C = threading.Thread(target=hello, args=('C',3), name='C')

    C.setDaemon(True) # 设置子线程在主线程结束时是否无条件跟随主线程一起退出

    A.start()
    A.join(5)
    B.start()
    C.start()

    time.sleep(20)

    print('进程A%s'%('还在工作中' if A.is_alive() else '已经结束工作'))
    print('进程B%s'%('还在工作中' if B.is_alive() else '已经结束工作'))
    print('进程C%s'%('还在工作中' if C.is_alive() else '已经结束工作'))

    print('下班了...')

if __name__ == '__main__':
    demo()