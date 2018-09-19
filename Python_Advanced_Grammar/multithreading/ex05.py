import time
import threading

"""
主线程虽然死亡,但是fun这个线程不会消亡,而是会执行完毕
"""


def fun():
    print("start fun")
    time.sleep(2)
    print("end fun")


print("main thread")
t1 = threading.Thread(target=fun, args=())
t1.start()
time.sleep(1)
print("main thread end")
