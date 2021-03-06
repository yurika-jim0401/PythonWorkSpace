# 异常
 - 广义上的错误分为错误和异常
 - 错误指的是可以人为避免
 - 异常指的是在语法逻辑都正确的前提下，出现的问题
 - 在Python中，异常是一个类，可以处理和使用
 - 异常有很多种类型，诸如xxxError都是异常的类型

# 异常处理(见案例ex01)
 - 不能保证成员永远正确运行
 - 但是，必须保证程序在最坏的情况下得到的问题被妥善处理
 - Python的异常处理模块全部语法:
        
        
        try:
            尝试实现某个操作。
            如果没有异常，任务就可以完成
            如果出现异常，将异常从当前代码块扔出去尝试解决异常
        except 异常类型1:
            解决方案1:用于尝试在此处处理异常，解决问题
        except 异常类型2:
            解决方案2:用于尝试在此处处理异常，解决问题
        except (异常类型1,异常类型2...):
            解决方案1:针对多个异常使用相同的处理方式
        except:
            解决方案:所有异常的的解决方案
        else:
            如果没有出现任何异常,将会执行此处代码
        finally:
            无论是否有异常都要执行的代码

 - 流程
    - 1.执行try下面的语句
    - 2.如果出现异常，则在except语句里查找对应异常并进行处理
    - 3.如果没有出现异常，则执行else语句内容
    - 4.最后。不管是否出现异常，都要执行finally语句
 - 除了except(最少一个)以外，else和finally都是可选的

# 用户手动引发异常
 - 当某些情况，用户希望自己引发一个异常的时候，可以使用raise关键字来引发异常
 - 案例见ex02
 - 建议手动抛出异常的时候都是抛出自定义异常

# 关于自定义异常
 - 只要是raise异常，则推荐自定义异常
 - 在自定义异常的时候，一般包含以下内容:
    - 自定义发生异常的异常代码
    - 自定义发生异常后的问题提示
    - 自定义发生异常的行数
 - 最终目的是，一旦发生异常，方便程序员快速定位错误现场
 