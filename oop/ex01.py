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


# 实例化一个学生信息
yyt = PythonStudent()
yyt.name = "yyt"
print(yyt.name)
print(yyt.age)
yyt.doHomework()