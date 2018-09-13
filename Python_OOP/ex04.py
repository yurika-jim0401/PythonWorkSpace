class A():
    pass


class B(A):
    pass


# 不推荐多个父类
class C(B,A):
    pass


print(A.__mro__)
print(B.__mro__)


# 多继承案例
# 子类可以直接拥有父类的属性和方法，私有属性和方法除外
class Fish():
    def __init__(self,name):
        self.name = name
    def swim(self):
        print("i am swimming")


class Bird():
    def __init__(self,name):
        self.name = name
    def fly(self):
        print("i am flying")


class Person():
    def __init__(self,name):
        self.name = name
    def work(self):
        print("working")


class SuperMan(Person,Bird,Fish):
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self,name):
        self.name = name


s = SuperMan("jim")
s.fly()
s.swim()

t = Student("yyt")
s.work()


# 菱形继承问题
class A():
    pass


class B(A):
    name ="jim"
    age = 23
    pass


class C(A):
    pass


class D(B,C):
    pass


# 构造函数例子
class People():
    """
    对People类进行实例化的时候，姓名要确定，年龄要确定，地址要确定
    """
    def __init__(self):
        self.name = "NoName"
        self.age = 18
        self.address = "shanghai"
        print("init function")


p = People()
b = B()
setattr(b,"age",23)
print(b.age)
print(getattr(b,"name"))