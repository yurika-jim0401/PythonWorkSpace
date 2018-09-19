# -*- coding: utf-8 -*-
# lambda表达式,计算一个数字的100倍
# 因为就是一个表达式,所以没有return
stm = lambda x : x * 100
# 使用上跟函数调用一模一样
print(stm(89))

# 多参数的lambda表达式
stm2 = lambda x,y,z: x+y*10+z*100
print(stm2(4,5,6))

# 高阶函数内容:
# 变量可以赋值
a = 100
b = a
# 函数的名称其实也是一个变量
def funA():
    print("i am A")
funB = funA
funB()


# 高阶函数举例
# funC是个普通函数,返回一个传入数字的100倍
def funC(n):
    return n*100


# 再写一个函数,把传入参数乘3,这一种方式传入的参数没有函数,将代码块写死了,不是很灵活
def funD(n):
    return funC(n)*3


print(funD(5))


# 写一个高阶函数,这一种写法比上面的写法更好更灵活。
def funE(n,f):
    """
    假定函数是把n扩大100倍
    """
    return f(n)*3
print(funE(9,funC))


# 需求变了,需要把n放大30倍,如果用第一种写法就需要改函数,第二种只需要调用别的函数就行了
def funF(n):
    return n*10


print(funE(9,funF))