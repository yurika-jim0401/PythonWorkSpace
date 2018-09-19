# map案例
# 有一个列表,想对列表里的每一个元素乘以10,并得到新的列表
from functools import reduce
l1 = [i for i in range(10)]
print(l1)
l2 = []
for i in l1:
    l2.append(i*10)
print(l2)


# 上述功能还可以利用map来实现
def mulTen(n):
    return n*3


l3 = map(mulTen,l1)
for i in l3:
    print(i,end=" ")

print()

# reduce 案例
# 定义一个操作函数
# 加入操作函数只是相加
def myAdd(x,y):
    return x + y


# 在不断地迭代相加
rst = reduce(myAdd,l1)
print(rst)
