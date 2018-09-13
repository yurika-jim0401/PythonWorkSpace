# 异常处理案例
# 给出异常提示信息
try:
    num = int(input("please input your number:"))
    rst = 100/num
    print("计算结果是:{0}".format(rst))
    # 捕获异常后，把异常实例化，出错信息会在实例里
    # 注意下面捕获异常的写法
    # 以下语句是捕获ZeroDivisionError异常并且实例化e
except ZeroDivisionError as e:
    # 想一想为什么这里直接打印实例e，就显示了异常信息，这里的实例e应该实现了哪个函数
    print(e)
    # exit是退出程序
    exit()
# 自己也不确定会出现哪种异常，可以写很多异常，要把越具体的错误越往前放
# 在异常类继承关系中，越是子类的异常越具体
# 越是父亲类的异常，越要往后放
# 在处理异常的时候，一旦拦截到某一个异常，则不在继续往下查看，直接进行下一个代码
# 即有finally则执行finally语句块，否则就执行下一个大的语句
except NameError as e:
    print(e)
    exit()
except AttributeError as e:
    print(e)
    exit()
# 所有异常都是继承自Exception
# 如果写上下面这句话，任何异常都会拦截住
# 而且，下面这句话一定是最后一个exception
except Exception as e:
    print(e)
    exit()
