# filter 案例
# 需要定义过滤函数
# 过滤函数必须要求有输入,返回布尔值
# 这个过滤函数是找出列表中的偶数


def filterA(n):
    if n%2 == 0:
        return True


l1 = [i for i in range(10)]
print(l1)
l2 = filter(filterA,l1)
# filter返回的是一个filter迭代对象,用for访问
for i in l2:
    print(i,end=" ")

print()
# 排序案例
a = [231,3423,1314,23,1234,545,135,2325,123562]
# sorted()有个默认参数reverse=False,就是正序排序,修改参数可以变成倒序
print(sorted(a))

# 排序
b = [-31,-2421,231,-231,34325,-34652]
# 按照绝对值排序(倒叙)
# abs是求绝对值
print(sorted(a,key=abs,reverse=True))

# sorted案例
astr = ['jim','YYt','yurika']
# 正常排序,大写排在小写前面
str1 = sorted(astr)
print(str1)
# 关键词排序,小写排前面
str2 = sorted(astr,key = str.lower)
print(str2)