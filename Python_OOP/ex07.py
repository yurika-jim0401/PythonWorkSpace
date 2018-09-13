import abc

# 类和对象的三种方法
class Person():
    # 实例方法
    def eat(self):
        print(self)
        print("eat...")

    # 类方法
    # 类方法第一个参数一般命名为cls
    @classmethod
    def play(cls):
        print(cls)
        print("play...")

    # 静态方法
    # 不需要第一个参数表示自身或者类
    @staticmethod
    def say():
        print("say...")


p = Person()
# 实例可以调用实例方法,类方法，静态方法
p.eat()
p.play()
p.say()

# 类不能调用实例方法
# Person.eat()
Person.play()
Person.say()


# 变量的三种用法
class A():
    def __init__(self):
        self.name = "haha"
        self.age = 18


print("-"*50)
a = A()
#属性的三种用法
#1.赋值
#2.读取
#3.删除
a.name = "jim"
print(a.name)
# 删除a.name之后，本实例中就没有这个属性了
del a.name
print(a.__dict__)
print("-"*50)

# 类属性 property
# 应用场景
# 对变量除了普通的三种操作，还想增加一些附加的操作，那么可以通过property完成
class B():
    def __init__(self):
        self.name = "haha"
        self.age = 18

    # 此功能，是对变量进行读取操作的时候应该执行的函数功能
    def fget(self):
        print("被读取了...")
        return self.name

    # 此功能是对变量进行写入操作时应该执行的函数功能
    def fset(self,name):
        print("被写入了...")
        self.name = "SHU "+name

    # fdel模拟的是删除变量的时候进行的操作
    def fdel(self):
        pass

    # property的四个参数顺序是固定的
    # 第一个参数是读取，第二个是写入，第三个是删除，最后一个是文档
    name2 = property(fget,fset,fdel,"这是一个property")


b = B()
print(b.name2)

print("-"*50)

# 抽象类
# 声明一个类并且指定当前类的元类
class Animal(metaclass=abc.ABCMeta):
    # 这里不写方法的具体实现，因为继承这个父类的各个子类的该方法实现可能各有不同
    # 定义一个抽象方法
    @abc.abstractmethod
    def sayHello(self):
        pass

    # 定义类抽象方法
    @abc.abstractmethod
    def eat(cls):
        pass

    # 定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass

class Dog(Animal):
    # 重新复写父类的方法
    def sayHello(self):
        print("闻一下")


class Person(Animal):
    def sayHello(self):
        print("打个招呼")


print("-"*50)


# 自己组装一个类
class Test():
    pass


def see(self):
    print("see..")

# 函数可以当成变量用于赋值,赋值之后就相当于给Test类组装了一个成员方法
a = Test()
Test.see = see
a.see()

# 另外一种直接将函数组装到实例上面
class Test1():
    pass


def see1(self):
    print("see again...")

t1 = Test1()
# 如果直接这样将函数赋值给实例，会使得实例的成员方法缺少参数self
# 必须借助工具来组装 MethodType(func,class)
from types import  MethodType
t1.see1 = MethodType(see1,Test1)
t1.see1()

# 利用type造一个类
# 先定义类应具有的成员函数
def see2(self):
    print("see you too...")


def talk(self):
    print("talking...")


# 用type来创建一个类
Test2 = type("AName",(object,),{"class_see":see2,"class_talk":talk})
# 用上述方法就创建好了一个类，可以正常使用了
t2 = Test2()
t2.class_see()
t2.class_talk()

# 元类示例
# 元类写法是固定的，必须继承于type
# 元类一般命名以MetaClass结尾
class JimMetaClass(type):
    # 注意以下写法
    def __new__(cls,name,bases,attrs):
        # 自己的业务处理
        print("这是一个元类")
        attrs['id'] = '000000'
        attrs['addr'] = "上海市"
        return type.__new__(cls,name,bases,attrs)


# 元类定义完就可以使用，使用注意写法
class Teacher(object,metaclass=JimMetaClass):
    pass

t = Teacher()
print(t.id)

