# -*- encoding: utf8 -*-
"""
3.4 条件 Condition
两位小朋友，Hider 和 Seeker，打算玩一个捉迷藏的游戏，
规则是这样的：Seeker 先找个眼罩把眼蒙住，喊一声“我已经蒙上眼了”；
听到消息后，Hider 就找地方藏起来，藏好以后，也要喊一声“我藏好了，你来找我吧”；
Seeker 听到后，也要回应一声“我来了”，捉迷藏正式开始。
各自随机等了一段时间后，两位小朋友都憋住了跑了出来。谁先跑出来，就算谁输。
"""
import time
import threading
import random

cond = threading.Condition()    #创建对象条件
draw_Seeker = False #Seeker小朋友认输
draw_Hidwer = False #Hidwer小朋友认输

def seeker():
    """Seeker小朋友的线程函数"""

    global draw_Seeker, draw_Hidwer

    time.sleep(1)   #确保Hider小朋友的已经进入消息等待状态
    cond.acquire()  #阻塞时请求资源
    time.sleep(random.random()) #假装蒙眼需要花费时间
    print('Seeker:我已经蒙上眼了')
    cond.notify()   #把消息通知到Hider小朋友
    cond.wait() #释放资源并等待Hider小朋友已经藏好的消息

    print('Seeker: 我来了')    # 收到Hider小朋友已经藏好的消息后
    cond.notify()   # 把消息通知到Hider小朋友
    cond.release()  # 不要再听消息了，彻底释放资源
    time.sleep(random.randint(3,10))    #seeker小朋友的耐心只有3-10秒钟

    if draw_Hidwer:
        print('Seeker: 哈哈，我找到你了，我赢了')
    else:
        draw_Seeker = True
        print('Seeker: 算了，我找不到你，我认输啦')

def hider():
    """Hider小朋友的线程函数"""

    global draw_Seeker, draw_Hidwer

    cond.acquire()  #阻塞时请求资源
    cond.wait() #如果先于seeker小朋友请求到资源，则立刻释放并等待
    time.sleep(random.random()) #假装找地方躲藏需要花费时间
    print('Hider: 我藏好了，你来找我吧')
    cond.notify()   #把消息通知到seeker小朋友
    cond.wait() #释放资源并等待seeker小朋友开始找人的消息

    cond.release()  #不再监听消息，彻底释放资源
    time.sleep(random.randint(3,10))    #Hider小朋友的耐心只有3-10秒钟

    if draw_Seeker:
        print('Hider: 哈哈，你没找到我，我赢了')
    else:
        draw_Hidwer = True
        print('Hider: 算了，这里太闷了，我认输，自己出来吧')

def demo():
    th_seeker = threading.Thread(target=seeker)
    th_hider = threading.Thread(target=hider)
    th_seeker.start()
    th_hider.start()

    th_seeker.join()
    th_hider.join()

if __name__ == '__main__':
    demo()
