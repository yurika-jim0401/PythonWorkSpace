# 属性案例
# 创建Student类，描述学生类
# 学生具有Student.name属性
# 但name格式不统一
# 这里可以增加一个函数，然后用自动调用，但是多此一举
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # 初始化函数中直接调用，大写姓名，这样做虽然可以，但是很麻烦
        self.setName(name)

    def introduce(self):
        print("hi,my name is {0}".format(self.name))

    def setName(self,name):
        self.name = name.upper()

s1 = Student("jim",18)
s2 = Student("yyt",18)
s1.introduce()
s2.introduce()

# property案例
# 定义一个Person类，具有name，age属性
# 对于任意输入的姓名，我们希望都用大写方式保存
# 对于输入的年龄，内部统一用整数保存

class Person():
    # 函数的名称可以任意
    def fget(self):
        return self._name*2

    def fset(self,name):
        # 所有输入的姓名以大写形式保存
        self._name = name.upper()

    def fdel(self):
        self._name = "NoName"

    name = property(fget,fset,fdel,"对name进行操作")

p1 = Person()
# 赋值的时候是写操作，调用了fset
p1.name = "jim"
# 打印的时候是读操作，调用了fget
print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__bases__)
#print(p1.__bases__)

print(p1.name)

# 作业：
# 1.在用户输入年龄的时候，可以输入整数，小数，浮点数
# 2、但内部为了数据清洁，我们需要统一保存整数，直接舍去小数点

print("-"*50)
# 魔法函数实例
# __call__实例
# __str__实例
# __getattr__实例
class A():
    def __init__(self,name=0):
        print("init is starting")

    def __call__(self, *args, **kwargs):
        print("call is starting")

    def __str__(self):
        return "this is a class A"

    def __getattr__(self, item):
        print("没有这个属性")
a = A()
# 不能将a当函数使用，会报错：is not callable
# 在类中定义过__call__函数之后，就可以了,而且执行的是call函数里的代码块
a()
# 直接将对象a当做字符串打印，没有什么意义，当定义过__str__之后，就可以打印__str__中的代码块
print(a)
# 当找对象找类中根本不存在的属性时会报错，但是定义过__getattr__之后，就不会报错，并且会返回一个None
print(a.name)

print("-"*50)
# __setattr__ 案例
class Student():
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        print("this is set attr")
        # 下面语句会导致死循环
        # self.name = value
        # 此种情况，为了避免死循环，规定统一调用父类魔术函数
        super().__setattr__(key,value)


s = Student()
print(s.__dict__)
s.name = "jim"

print("-"*50)
# __gt__ 案例
class Worker():
    def __init__(self,name):
        self._name = name

    def __gt__(self, other):
        print("{0}和{1}可以比较大小".format(self._name,other._name))
        return self._name > other._name


work1 = Worker("jim")
work2 = Worker("yyt")
print(work1 > work2)