# 返回函数案例
# 定义一个普通函数
def myF(a):
    print('In myF')
    return None

a = myF(8)
print(a)


# 函数作为返回值返回,被返回的函数在函数体内定义
def myF2():
    def myF3():
        print("In myF3")
        return 3
    return myF3


# 使用函数
# 调用myF2,返回一个函数myF3，赋值给f3,f3就是一个函数,值是myF3
f3 = myF2()
print(f3)
f3()
print(f3())

# 复杂一点的返回函数的例子(闭包)
# args:参数列表
# 1.myF4定义函数,返回内部定义的函数myF5
# 2.myF5使用了外部变量,这个变量是myF4的参数
def myF4( *args):
    def myF5():
        rst = 0
        for n in args:
            rst += n
        return rst
    return myF5
f5 = myF4(1,2,3,4,5,6,7)
print(f5())

# 闭包的常见问题
def count():
    """
    定义列表,列表里存放的是定义的函数
    :return:
    """
    fs = []
    for i in range(1,4):
        # 每一次循环就定义一个函数
        # 这个f是一个闭包结构
        def f():
            return i * i
        fs.append(f)
    return fs
f1,f2,f3 = count()
print(f1(),f2(),f3())
# 结果出现问题:
# 上面的结果产生的原因:返回函数引用了变量i,i并非立即执行,而是等到三个函数都返回的
# 时候才统一使用,此时i已经变成了3,最终调用的时候,都返回的是 3*3
# 此问题描述为:返回闭包时,返回函数不能引用任何循环变量
# 解决方案:再创建一个函数,用该函数的参数绑定循环变量的当前值,无论循环变量以后如何改变,
# 已经绑定的函数参数值不再改变
def count1():
    """
    定义列表,列表里存放的是定义的函数
    :return:
    """
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3 = count1()
print(f1(),f2(),f3())