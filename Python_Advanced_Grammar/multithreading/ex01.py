"""
利用time函数,生成两个函数
顺序调用,总时长大约6秒loop1: 4秒;loop2: 2秒
计算总的运行时间
"""
import time


def loop1():
    # ctime 获得当前时间
    print('strat loop1 at:', time.ctime())
    # 睡眠时间,单位:秒
    time.sleep(4)
    print('end loop1 at:', time.ctime())


def loop2():
    # ctime 获得当前时间
    print('strat loop2 at:', time.ctime())
    # 睡眠时间,单位:秒
    time.sleep(2)
    print('end loop2 at:', time.ctime())


def main():
    print("staring at:", time.ctime())
    loop1()
    loop2()
    print("all done at:", time.ctime())


if __name__ == '__main__':
    main()

