'''
定义一个学生类，用来描述学生
'''
class Student():
    # 一个空类，pass表示直接跳过，此次pass必须有，否则报错
    pass


# 定义一个对象
jim = Student()


# 再定义一个类，用来描述学Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    # 注意以下几点：
    # 1. def fun() 的缩进层级
    # 2. 系统默认有一个self参数
    def doHomework(self):
        print("{0} is doing homework!".format(self.name))
        # 推荐在函数末尾使用return
        return None


class A():
    name = "jim"
    age = 23

    # 注意say的写法，参数由一个self
    def say(self):
        self.name = "aaaa"
        self.age = 18
        print("my name is {0}".format(self.name))
        print("my age is {0}".format(self.age))
        # print("i am {0} years old".format(self.age))
    def sayagain(self):
        print("my name is {0}".format(self.name))
        print("my age is {0}".format(self.age))
# 实例化一个学生信息
yyt = PythonStudent()
yyt.name = "yyt"
print(yyt.name)
print(yyt.age)
yyt.doHomework()
print(yyt.__dict__)
print(PythonStudent.__dict__)

# 测试类与对象的属性关系
# 此时，A称为类实例
# 这个案例说明 类实例的属性和其对象的实例的属性在不对对象的实例属性赋值的前提下，指向同一个变量
print(A.name)
print(A.age)
print("*"*30)
# id用来鉴别一个变量是否和另外一个变量是同一个变量
print(id(A.name))
print(id(A.age))
print("*"*30)
a = A()
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
print("*"*30)
# 在对其赋值之后，就不会指向同一变量了
a = A()
a.name = "yyt"
a.age = 18
print(id(a.name))
print(id(a.age))
a.say()
a.sayagain()
