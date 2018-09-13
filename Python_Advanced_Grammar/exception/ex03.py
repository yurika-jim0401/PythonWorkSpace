# 异常中的else语句案例
# else和except只会执行其一
try:
    num = int(input("please input your number:"))
    rst = 100/num
    print("计算结果是:{0}".format(rst))
except Exception as e:
    print(e)
else:
    print("No Exception")
finally:
    print("一定会执行这句话")