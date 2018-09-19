import time
import threading

"""
这里将fun设置为守护线程:
当主线程消亡,守护线程会跟主线程一起消亡
"""


def fun():
    print("start fun")
    time.sleep(2)
    print("end fun")


print("main thread")
t1 = threading.Thread(target=fun, args=())
# 将t1设置为守护线程
t1.setDaemon(True)
t1.start
time.sleep(1)
print("main thread end")