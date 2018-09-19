# 装饰器案例
# 任务:对hello函数进行功能扩展,每次执行hello前打印当前时间
import time


# 高阶函数,以函数作为参数
def printTime(f):
    def wrapper(*args, **kwargs):
        print("Time: ",time.ctime())
        return f(*args,**kwargs)
    return wrapper


# 上面定义了装饰器,使用的时候需要用到@,此符号是Python的语法塘
@printTime
def hello():
    print("hello world")


hello()


@printTime
def hello2():
    print("This is hello2")
    print("还可以有很多选择")


hello2()
# 上面对函数的装饰使用了系统定义的语法塘
# 下面开始手动执行装饰器
def hello3():
    print("我是手动执行的")
hellotest = printTime(hello3)
hellotest()