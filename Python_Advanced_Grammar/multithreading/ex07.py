import time
import threading


def loop1():
    print("start loop1 at:", time.ctime())
    time.sleep(4)
    print("end loop1 at:", time.ctime())


def loop2():
    print("start loop2 at:", time.ctime())
    time.sleep(2)
    print("end loop2 at:", time.ctime())


def loop3():
    print("start loop3 at:", time.ctime())
    time.sleep(5)
    print("end loop3 at:", time.ctime())


def main():
    print("starting main at:", time.ctime())
    t1 = threading.Thread(target=loop1, args=())
    t1.setName('THR_1')
    t1.start()
    t2 = threading.Thread(target=loop2, args=())
    t2.setName('THR_2')
    t2.start()
    t3 = threading.Thread(target=loop3, args=())
    t3.setName('THR_3')
    t3.start()

    time.sleep(3)
    for thr in threading.enumerate():
        print("正在运行的线程名字是:{0}".format(thr.getName()))
    print("正在运行的子线程数量:{0}".format(threading.activeCount()))
    print("all done at:", time.ctime())


if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)
