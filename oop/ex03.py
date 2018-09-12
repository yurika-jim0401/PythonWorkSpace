# 继承的语法
# 在Python中，任何一个类都有一个共同的父类叫object
class Person():
    name = "NoName"
    gender = "male"
    __age = 0  # 年龄作为私有
    _petname = "sec" # 人的小名 作为保护的
    def sleep(self):
        print("i am sleeping")
    def work(self):
        print("make some money")

# 定义老师这个类继承person类
# 子类扩充父类功能
# 人有工作函数，老师也有工作函数，但是老师的工作要讲课
class Teacher(Person):
    teacher_id = "1234"
    gender = "female"

    def teach(self):
        print("i am teaching")

    def work(self):
        # 扩充人（父类）的工作内容成为老师（子类）的工作内容，只需调用父类相应函数
        # 子类可以冒充父类，父类不可以冒充子类，这里将self是老师，但是当父类的self使用
        Person.work(self)
        # 或者这样写也是一样,这里就不需要传self参数了，已经默认传过了
        super().work()
        self.teach()


t = Teacher()
# 子类父类的name是同一个
print(t.name,id(t.name))
print(Person.name,id(Person.name))
# 受保护的外部不能访问，为啥这里可以？因为Teacher是Person的子类
print(t._petname)
# 优先使用子类中gender的定义
print(t.gender)
t.work()
t.sleep()
t.teach()


# 构造函数
class Animal():
    def __init__(self):
        print("i am Animal")


class BuRuAni(Animal):
    def __init__(self,name):
        print("i am BuRuAni {0}".format(name))


class Dog(BuRuAni):
    # __init__ 就是构造函数
    # 每次实例化的时候，第一个被调用
    # 因为主要工作是进行初始化
    def __init__(self):
        print("i am init in dog")


# 猫不写构造函数
class Cat(BuRuAni):
    pass


# 继承中的构造函数
# 实例化的时候，括号内参数需要跟构造函数参数匹配
# 因为在Dog类中找到了构造函数，则不在父类中查找父类的构造函数
xiaogou = Dog()
# Cat没有构造函数，此时应往上找，找父类(BuRuAni)的构造函数,就不再向上查找了
# 在给Cat父类的构造函数多加一个参数name时，如果实例化的时候不传入相应参数，就会有问题，
# 而Dog中有不带多余参数的构造函数，所以不会有问题。
xiaomao = Cat("tom")

