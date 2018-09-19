import threading
from time import sleep, ctime

loop = [4, 2]


class ThreadFunc:
    def __init__(self, name):
        self.name = name

    def loop(self, nloop, nsec):
        """

        :param nloop: loop函数的名称
        :param nsec: 系统休眠时间
        :return:
        """
        print("start loop{0} at:{1}".format(nloop, ctime()))
        sleep(nsec)
        print("end loop{0} at:{1}".format(nloop, ctime()))


def main():
    print("starting at:", ctime())
    # ThreadFunc("loop").loop 跟以下两个式子相等:
    # t = ThreadFunc("loop")
    # t.loop
    t = ThreadFunc("loop")
    t1 = threading.Thread(target=t.loop, args=("loop1", 4))
    # 下面这种写法更好一些,不需要将类实例化,直接调用类方法,将类方法放入线程中
    t2 = threading.Thread(target=ThreadFunc('loop').loop, args=("loop2", 2))
    # 以上写法的常见错误写法:
    # t1 = threading.Thread(target=ThreadFunc('loop').loop("loop1", 4))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("all done at:", ctime())


if __name__ == '__main__':
    main()