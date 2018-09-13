# Mixin案例
class Person():
    name = "jim"
    age = 23

    def eat(self):
        print("eat...")
    def drink(self):
        print("drink...")
    def sleep(self):
        print("sleep...")


class Teacher(Person):
    def work(self):
        print("work...")


class Student(Person):
    def study(self):
        print("study...")


# 助教类，继承于老师和学生(普通方式实现多继承)
class Tutor(Teacher,Student):
    pass

t = Tutor()
print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)

print("-"*50)

# 使用Mixin来实现多继承
# 这里的老师跟学生都没有父类，只是表示一个单一的功能
class TeacherMixin():
    def work(self):
        print("work...")


class StudentMixin():
    def study(self):
        print("study...")


# TutoMixin的父类仅仅是Person
class TutorMixin(Person,TeacherMixin,StudentMixin):
    pass

tt = TutorMixin()
print(TutorMixin.__mro__)
print(tt.__dict__)
print(TutorMixin.__dict__)