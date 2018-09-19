import functools
# 偏函数案例
# 把字符串转换成十进制数字
# 想把字符串12345转化成八进制的整数
print(int("12345",base=8))

# 新建一个函数,此函数默认输入的字符串是16进制数字
# 把此字符串返回十进制的数字
def int16(x,base=16):
    return int(x,base)
print(int16("12345"))

# 将函数int做成偏函数int16,并且固定了一个参数base=16
int8 = functools.partial(int,base = 8)
print(int8("12345"))

# zip案例,若一个列表元素少于另一个列表,多余的元素不存入
l1 = [i for i in range(1,6)]
l2 = [i for i in range(11,66) if i % 11 == 0]
print(l1)
print(l2)
# 生成的是一个可迭代的zip类型
z = zip(l1,l2)
print(type(z))
print(z)
for i in z:
    print(i)

# enumerate案例
l3 = [i for i in range(11,66) if i % 11 == 0]
# 默认参数start=0,可修改
em = enumerate(l3)
l2 = [i for i in em]
print(l2)