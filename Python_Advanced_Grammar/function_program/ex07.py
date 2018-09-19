import collections
# 类似于C语言的结构Struts
Point = collections.namedtuple("Point",['x','y'])
p = Point(11,22)
print(p.x)
print(p[0])

# 定义一个圆
Circle = collections.namedtuple("Circle",['x','y','r'])
# 圆心(100,150)半径50
c = Circle(100,150,50)
print(c)

# 想检查以下namedtuple到底输出谁的之类
print(isinstance(c,tuple))

# deque
q = collections.deque(['a','b','c'])
print(q)
q.append("d")
q.appendleft("x")
print(q)


# defaultdict
d1 = {"one":1,"two":2,"three":3}
print(d1["one"])
# 字典里查找的key必须得有,不然会报错
# print(d1["four"])
# lambda表达式,直接返回字符串
func = lambda:"jim"
# 先给d2定义一个默认值,是一个函数
d2 = collections.defaultdict(func)
d2["one"] = 1
print(d2["one"])
print(d2["four"])

# Counter
# 这个函数是以字符串里每一个字符为键
# 括号中的内容必须可迭代
print(collections.Counter("fangsaupjwlkngads.gdaopgijap;sgasdnfowjga"))

s = ["jim","love","yyt"]
print(collections.Counter(s))