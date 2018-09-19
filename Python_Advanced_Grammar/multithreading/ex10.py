# 多线程共享变量
import threading
sum1 = 0
loopsum = 100000

# 生成一个锁的实例
lock = threading.Lock()


def myadd():
    global sum1, loopsum
    for i in range(1, loopsum):
        # 上锁/申请锁
        lock.acquire()
        # 使用被锁资源
        sum1 += 1
        # 使用完毕,释放锁
        lock.release()


def myminu():
    global sum1, loopsum
    for i in range(1, loopsum):
        lock.acquire()
        sum1 -= 1
        lock.release()


if __name__ == '__main__':
    print("starting at {0}".format(sum1))

    # 开始多线程执行
    t1 = threading.Thread(target=myadd, args=())
    t2 = threading.Thread(target=myminu, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("end at {0}".format(sum1))
