# datetime模块常见属性
# datetime.date:一个理想化的日期，提供year，month，day属性
import datetime
import time
import timeit
dt = datetime.date(2018,9,14)
print(dt)
print(dt.day,dt.year,dt.month)

# datetime.time:提供一个理想的时间，提供hour,minute,second,microsec属性
# datetime.datetime:提供日期跟时间的组合
# datetime类中常用方法:
# today,now,utcnow,fromtimestamp:从时间戳返回本地时间
# datetime.timedelta:提供一个时间差，时间长度
dt = datetime.datetime(2018,9,14)
print(dt.today())
print(dt.now())
print(dt.utcnow())
print(dt.fromtimestamp(time.time()))

# datetime.timedelta
# 表示一个时间间隔
from datetime import  datetime,timedelta
t1 = datetime.now()
# 将td设置为一个小时的时间间隔
td = timedelta(hours=1)
# 当前时间t1加上时间间隔td之后,再将的得到的一个小时之后的时间格式化输出
print((t1+td).strftime("%Y-%m-%d %H:%M:%S"))


# timeit-时间测量工具
def p():
    time.sleep(2)


t1 = time.time()
p()
print(time.time() - t1)

# 生成列表的两种方法的比较
# 如果单纯比较生成一个列表的时间，很难实现
c = '''
sum = []
for i in range(1000):
    sum.append(i)
'''
# timeit(stmt=要执行的代码片段,number=执行次数)
t1 = timeit.timeit(stmt="[i for i in range(1000)]",number=10000)
# 测量代码C执行100000此的运行结果
t2 = timeit.timeit(stmt=c,number=10000)
print(t1,"---",t2)


def doit():
    num = 3
    for i in range(num):
        print("Repeat for {0}".format(i))


s = """
def doit(num):
    for i in range(num):
        print("Repeat for {0}".format(i))
"""

# timeit还可以用来执行函数,来测量一个函数的执行时间,这里将函数重复10次
# 执行doit(num)
# setup负责把环境变量准备好 s+"num=3" 相当于给doit传值
# 在setup小环境中，代码执行的顺序大致是
# def doIt(num):
#    pass
# num = 3
# doit(num)

t3 = timeit.timeit(stmt=doit,number=10)
t4 = timeit.timeit("doit(num)",setup=s+"num=3",number=10)
print(t3)
print(t4)