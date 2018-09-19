from collections import Iterable
from collections import Iterator
ll = [i for i in range(1,6)]
# 判断ll是否是可迭代对象
print(isinstance(ll, Iterable))
# 判断ll是否是迭代器
print(isinstance(ll, Iterator))

# iter函数
s = 'i love yyt'
print(isinstance(s, Iterable))
print(isinstance(s, Iterator))
s_iter = iter(s)
print(isinstance(s_iter, Iterable))
print(isinstance(s_iter, Iterator))

# 直接使用生成器
# 将这个放在中括号里就是列表生成器
L = [x*x for x in range(5)]
# 放在小括号里就是生成器
g = (x*x for x in range(5))
print(g)
for i in g:
    print(i)


# 函数案例
def odd():
    print("step 1")
    print("step 2")
    print("step 3")
    return None


odd()

# 将上面普通函数改成生成器案例
# 在函数odd中,yield负责返回


def odd():
    print("step 1")
    yield 1
    print("step 2")
    yield 2
    print("step 3")
    yield 3


# odd() 是调用生成器
g = odd()
one = next(g)
print(one)
two = next(g)
print(two)


# for循环调用生成器
# 斐波那契数列的生成器写法
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1
    # 需要注意,报出异常的返回值是return的返回值
    return 'done'


g = fib(5)
for i in range(6):
    rst = next(g)
    print(rst)

ge = fib(10)
# 在for循环中使用生成器
"""
生成器的典型用法就是在for中使用
比较常用的典型生成器就是range
"""
for i in ge:
    print(i)
