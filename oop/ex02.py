class Teacher():
    name = "jim"
    age = 23
    def say(self):
        self.name = "yyt"
        self.age = 18
        print("my name is {0}".format(self.name))
        print("my age is {0}".format(self.age))
    def sayagain():
        # 调用类成员变量需要用__class__.变量名
        print(__class__.name)
        print(__class__.age)
        print("i have said again")

t = Teacher()
t.say()

# 用实例来调用类中的参数时会默认传入一个参数，而这里的sayagain定义的时候没有参数，所以会报错
# t.sayagain()

# 调用绑定类的函数只能使用类名来调用
Teacher.sayagain()

# 关于self案例
class A():
    name = "liuneng"
    age = 18

    def __init__(self):
        self.name = "aaaa"
        self.age = 200

    def say(self):
        print(self.name)
        print(self.age)

class B():
    name = "bbbb"
    age = 99


a = A()
# 此时，系统会默认把a作为第一个参数传入函数
a.say()

# 此时，self被a替换
A.say(a)
# 同样可以把A作为参数传入
A.say(A)
# 此时，传入的是类实例B，因为B具有name和age属性，所以不会报错
A.say(B)

# 以上代码，利用了鸭子模型

class Person():
    # name是共有的成员
    name = "jim"
    # age就是私有成员
    __age = 18
p = Person()
print(p.name)
# 无法在外面访问age
# print(p.__age)

# name mangling技术
print(Person.__dict__)
p._Person__age = 19
print(p._Person__age)

# 受保护的封装protected也是用name mangling技术
