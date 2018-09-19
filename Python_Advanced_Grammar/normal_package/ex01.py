# 使用需要先导入

# 日历包
import calendar
# calender : 获取一年的日历字符串
# 参数
# w = 每个日期直接的间隔字符数
# l = 每周所占用的行数
# c = 每个月之间的间隔字符数
# 返回值是一个字符串
cal = calendar.calendar(2017,w=0,c=2)
print(cal)

# isleap:判断某一年是否是闰年
print(calendar.isleap(2020))
# leapdays:获取指定年份之间的闰年个数(左闭右开)
print(calendar.leapdays(2000,2020))
# month() 获取某个月的日历字符串
# 格式:calendar.month(年,月)
print(calendar.month(2018,9))
# monthrange() 获取一个月的从周几开始和天数
# 格式:calendar.monthrange(年,月)
# 返回值:元组(周几开始,总天数)
# 注意：周默认0-6表示为星期一到星期日
print(calendar.monthrange(2018,9))
# 既然返回的是元组，那么就可以这样来接收元组数据:w保存周几开始，t保存总天数
w,t = calendar.monthrange(2018,9)

# monthcalendar() 返回一个月每天的矩阵列表
# 格式:calendar.monthcalendar(年,月)
# 返回值：二级列表
# 注意：矩阵中没有天数用0表示
m = calendar.monthcalendar(2018,9)
print(m)
# 句柄方式遍历二维数组
for i in m:
    for j in i:
        print(j,end="\t")
    print(" ")

# 或者这种方法遍历
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j],end="\t")
    print(" ")
# prcal:print calendar 直接打印日历
calendar.prcal(2018)

# prmonth() 直接打印整个月的日历
# 格式：calendar.promonth(年,月)
# 返回值:无
calendar.prmonth(2018,3)

# weekday() 获取周几
# 格式:calendar.weekday(年,月,日)
# 返回值：周几对应的数字
print (calendar.weekday(2018,9,13))