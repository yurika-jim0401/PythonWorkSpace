# 时间模块使用需要单独导入
import time

# 时间模块的属性：
# timezone:当前时区和UTC时间相差的秒数，在没有夏令时的情况下的间隔,东八区是-28800(固定值)
# altzone:获取当前时区与UTC时间相差的秒数，有夏令时的情况下
# daylight:检测当前是否是夏令时时间状态,0表示是
print(time.timezone)

# 得到时间戳
print(time.time())

# localtime显示当前时间，返回的是一个时间的结构
# asctime(time)返回元组的正常字符串化后的时间格式
print(time.localtime())
print(time.localtime().tm_hour)
print(time.asctime(time.localtime()))

# ctime:获取字符串化的当前时间,不需要上面这么麻烦
print(time.ctime())

# mktime() 使用时间元组获取对应的时间戳
# 格式: time.mktime(时间元组)
# 返回值:浮点数时间戳
print(time.mktime(time.localtime()))

# clock:获取cpu时间,3.0-3.3可以直接使用,以前用来测量一段代码的运行时间
# sleep: 使程序进入睡眠.n秒后继续
# for i in range(10):
#     print(i)
#     time.sleep(1)

def p():
    time.sleep(2.5)
t0 = time.clock()
p()
t1 = time.clock()
print(t1-t0)

# strftime:将时间元组转化为自定义的字符串格式
'''
格式  含义  备注
%a  本地（locale）简化星期名称    
%A  本地完整星期名称    
%b  本地简化月份名称    
%B  本地完整月份名称    
%c  本地相应的日期和时间表示    
%d  一个月中的第几天（01 - 31）   
%H  一天中的第几个小时（24 小时制，00 - 23）   
%I  一天中的第几个小时（12 小时制，01 - 12）   
%j  一年中的第几天（001 - 366）  
%m  月份（01 - 12） 
%M  分钟数（00 - 59）    
%p  本地 am 或者 pm 的相应符    注1
%S  秒（01 - 61）  注2
%U  一年中的星期数（00 - 53 星期天是一个星期的开始）第一个星期天之前的所有天数都放在第 0 周   注3
%w  一个星期中的第几天（0 - 6，0 是星期天） 注3
%W  和 %U 基本相同，不同的是 %W 以星期一为一个星期的开始  
%x  本地相应日期  
%X  本地相应时间  
%y  去掉世纪的年份（00 - 99）    
%Y  完整的年份   
%z  用 +HHMM 或 -HHMM 表示距离格林威治的时区偏移（H 代表十进制的小时数，M 代表十进制的分钟数）      
%%  %号本身
'''

# 把时间表示成我们习惯的格式
# 这里直接用strftime将格式设置时候，如果里面有中文就会出现编码问题，
# 原理是：“在Windows里，time.strftime使用C运行时的多字节字符串函数strftime，
# 这个函数必须先根据当前locale配置来编码格式化字符串（使用PyUnicode_EncodeLocale）。”
# 如果不设置好locale的话，
# 根据默认的"C" locale，底层的wcstombs函数会使用latin-1编码（单字节编码）来编码格式化字符串，
# 然后导致题主提供的多字节编码的字符串在编码时出错。
import locale
locale.setlocale(locale.LC_CTYPE,'chinese')
t = time.localtime()
ft = time.strftime("%Y年%m月%d日 %H:%M:%S",t)
print(ft)