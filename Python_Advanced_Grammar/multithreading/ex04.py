"""
利用time函数,生成两个函数
采用多线程方式运行函数(带参函数)
计算总的运行时间
"""
import time
import threading


def loop1(int1):
    # ctime 获得当前时间
    print('strat loop1 at:', time.ctime())
    print("我是参数 {0}".format(int1))
    # 睡眠时间,单位:秒
    time.sleep(4)
    print('end loop1 at:', time.ctime())


def loop2(int1, int2):
    # ctime 获得当前时间
    print('strat loop2 at:', time.ctime())
    print("我是参数 {0}和{1}".format(int1, int2))
    # 睡眠时间,单位:秒
    time.sleep(2)
    print('end loop2 at:', time.ctime())


def main():
    print("staring at:", time.ctime())
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程的函数为start_new_thread
    # 参数有两个,一个是需要运行的函数名,第二个是函数的参数作为元组使用,为空则使用空元组
    # 注意,如果函数只有一个参数,需要参数后有一个逗号
    # 这里主线程时间太短,线程loop1和loop2都还没执行完,主线程就跑完了,
    # 所以看不到loop1和loop2的结束时间
    # 这里的线程里可以给执行的函数传入参数,如果参数只有一个,记得元组的第一个元素后加逗号以提示是元组
    t1 = threading.Thread(target=loop1, args=("jim",))
    t1.start()
    t2 = threading.Thread(target=loop2, args=("jim", "yyt"))
    t2.start()
    # 有了jion方法,主线程就会等待进程执行完毕才会结束
    t1.join()
    t2.join()
    print("all done at:", time.ctime())


if __name__ == '__main__':
    main()
