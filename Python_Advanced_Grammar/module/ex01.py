# 包含一个学生类
# 一个sayHello函数
# 一个打印语句
# 这三个都是平级的


class Student():
    def __init__(self,name = "NoName",age=18):
        self.name = name
        self.age = age

    def say(self):
        print("my name is {0}".format(self.name))


def sayHello():
    print("Hello")

# 这种代码在模块中最好不要有，一旦模块被导入一次就会直接执行
# 可以做一个判断，在这个模块单独执行的时候会执行下面这个函数，被引用的时候就不会执行
# 一般来讲，模块建议以这句话开始，作为程序的入口
if __name__ == "__main__" :
    print("我是模块p01")