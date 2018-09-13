# raise案例
# 自定义异常必须是系统异常的子类


class JimError(ValueError):
    pass


try:
    print("i love yyt")
    print(3.1415926)
    # 手动引发一个异常
    # 语法：raise ErrorClass_Name
    raise JimError
    # 上面的已经抛出异常，下面的print则不会执行
    print("还没结束")
except NameError as e:
    print("NameError!")
# 如果异常中没有找到自己定义的异常类，就会找他的父类
except JimError as e:
    print("JimError!")
except ValueError as e:
    print("ValueError!")
except Exception as e:
    print("Exception!")
finally:
    print("这个语句一定执行")