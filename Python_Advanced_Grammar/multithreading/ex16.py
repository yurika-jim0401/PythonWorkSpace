import threading
import time


class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
        if mutex.acquire(1):
            num += 1
            msg = self.name + 'set num to ' + str(num)
            print(msg)
            mutex.acquire()
            mutex.release()
            mutex.release()


num = 0
# 设置一个普通锁,在自己调用自己的时候就会出现问题
# mutex = threading.Lock()
# 这里要设置为可重入锁才可以
mutex = threading.RLock()


def testTh():
    for i in range(5):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    testTh()
