# 常用模块
 - calendar
 - time
 - datetime
 - timeit
 - os
 - shutil
 - zip
 - math
 - string
 - 上述所有模块使用理论上都应该先导入，string是特例
 - calendar,time,datetime的区别参考中文意思
 
# calendar模块
 - 跟日历相关的模块(用法见案例ex01)

# time模块(用法见案例ex02)
 - 先介绍时间戳的概念：
    - 一个时间的表示,根据不同语言,可以使整数或者浮点数
    - 表示从1970年1月1日0时0分0秒到现在经历的秒数
    - 如果表示的时间是1970年以前或者太遥远的为了,可能出现异常
    - 32位操作系统能够支持到2038年
 - UTC时间
    - UTC称为世界协调时间,以英国的格林尼治天文所所在地区时间为参考的时间标准,也叫做世界标准时间
    - 中国时间是 UTC+8 东八区
 - 夏令时
    - 夏令时就是在夏天的时候将时间调快一小时。
 - 时间元组
    - 一个包含时间内容的普通元组
        
        
        索引      内容    属性            值

        0       年       tm_year     2015
        1       月       tm_mon      1～12
        2       日       tm_mday     1～31
        3       时       tm_hour     0～23
        4       分       tm_min      0～59
        5       秒       tm_sec      0～61  60表示闰秒  61保留值
        6       周几     tm_wday     0～6
        7       第几天    tm_yday     1～366
        8       夏令时    tm_isdst    0，1，-1（表示夏令时）

# datetime模块
 - 提供日期和时间的运算和表示

# datetime.datetime 模块
 - 提供比较好用的时间
 - 类定义
 
        class datetime.datetime(year, month, day[, hour
          [, minute
          [, second
          [, microsecond
          [, tzinfo]]]]])
        # The year, month and day arguments are required.
        MINYEAR <= year <= MAXYEAR
        1 <= month <= 12
        1 <= day <= n
        0 <= hour < 24
        0 <= minute < 60
        0 <= second < 60
        0 <= microsecond < 10**
 - 类方法
    - datetime.today() 返回当前本地datetime.
    - datetime.now() 返回当前本地日期和时间, 如果可选参数tz为None或没有详细说明,这个方法会像today()
    - datetime.fromtimestamp(timestamp[,tz]) 根据时间戳返回本地的日期和时间,tz指定时区
    - datetime.utcfromtimestamp(timestamp) 根据时间戳返回 UTC
    - datetime.fromordinal(ordinal) 根据Gregorian ordinal 返回datetime
    - datetime.combine(date, time) 根据date和time返回一个新的datetime
    - datetime.strptime(date_string, format) 根据date_string和format返回一个datetime
 - 实例方法
    - datetime.date() 返回相同年月日的date对象
    - datetime.time() 返回相同时分秒微秒的time对象
    - datetime.replace(kw): kw in [year, month, day, hour, minute, second, microsecond, tzinfo], 与date类似. 类属性
    - datetime.min: datetime(MINYEAR, 1, 1). datetime.max: datetime(MAXYEAR, 12, 31, 23, 59, 59, 999999).
 - 实例属性
    - datetime.year: 1 至 9999 
    - datetime.month: 1 至 12 
    - datetime.day: 1 至 n 
    - datetime.hour: In range(24). 0 至 23 
    - datetime.minute: In range(60) 
    - datetime.second: In range(60)
    - datetime.microsecond: In range(1000000)
    
# OS - 操作系统相关
 - 跟操作系统相关，主要是文件操作
 - 与操作相关的操作,主要包含在三个模块里
    - os:操作系统目录相关
    - os.path:系统路径相关操作
    - shutil:高级文件操作,目录树的操作,文件赋值,删除,移动
 - 路径:
    - 绝对路径 :总是从根目录上开始
    - 相对路径 :基本以当前环境为开始的一个相对的地方

# OS模块 (案例见ex04)
 - getcwd():获取当前的工作目录
    - 格式:os.getcwd()
    - 返回值:当前工作目录的字符串
    - 当前工作目录就是诚信在进行文件相关操作,默认查找的文件的目录
 - chdir():改变当前的工作目录
    - change directory
    - 格式:os.chdir(路径)
    - 返回值:无
 - listdir():获取一个目录中所有子目录和文件的名称列表
    - 格式:os.listdir(路径/None)
    - 返回值:所有子目录和文件名称的列表
 - makedirs():递归创建一个文件夹
    - 格式:os.makedirs(递归路径)
    - 返回值:无
    - 递归路径:多个文件夹层层包含的路径就是递归路径,如a/b/c...
 - system():运行系统shell命令
    - 格式:os.system(系统命令)
    - 返回值:打开一个shell或者终端界面
    - ls是列出当前文件和文件夹的系统命令
    - 一般推荐使用subprocess代替而不用这个
 - getenv():获取指定的系统环境变量值
    - 格式:os.getenv(环境变量名)
    - 返回值:指定环境变量名对应的值
    - 与之对应的还有putenv()方法
 - exit():退出当前程序
    - 格式:exit()
    - 返回值:无
# OS模块的属性
 - os.curdir:当前目录
 - os.pardir:当前目录的父目录
 - os.sep:当前系统的路径分隔符
 - os.linesep:当前系统的换行符合
 - os.name:当前系统名称
 
# os.path模块,跟路径相关的模块
 - abspath():将路径转换为绝对路径
    - 格式:os.path.abspath(路径)
    - 返回值:路径的绝对路径形式
 - basename():获取路径中的文件名部分
    - 格式:os.path.basename(路径)
    - 返回值:文件名字符串
 - join():将多个路径拼成一个路径
    - 格式:os.path.join(路径1,路径2,...)
    - 返回值:组合之后的新路径字符串
 - split():将路径切割为文件夹部分和当前文件部分
    - 格式:os.path.split(路径)
    - 返回值:路径和文件名组成的元组
 - isdir():检查是否是目录
    - 格式:os.path.isdir(路径)
    - 返回值:布尔值
 - exists():检查文件或者目录是否存在
    - 格式:os.path.exists(路径)
    - 返回值:布尔值
# shutil 模块(案例见ex05)
 - copy():复制文件
    - 格式:shutil.copy(来源路径,目标路径)
    - 返回值:返回目标路径
    - 拷贝的同时可以给文件重命名
 - copy2():复制文件,保留元数据(文件信息)
    - 格式:shutil.copy2(来源路径,目标路径)
    - 返回值:返回目标路径
    - 注意:copy和copy2的唯一区别在于copy2复制文件时尽量保留元数据
 - copyfile():将一个文件中的内容复制到另外一个文件当中
    - 格式:shutil.copyfile(来源路径,目标路径)
    - 返回值:无
 - move():移动文件/文件夹
    - 格式:shutile.move(来源路径,目标路径)
    - 返回值:目标路径
# 归档和压缩
 - 归档:把多个文件或者文件夹合并到一个文件当中
    - 格式:shutil.make_archive(归档之后的目录和文件名,后缀,需要归档的文件夹)
    - 返回值:归档之后的地址
 - 压缩:用算法把多个文件或者文件夹无损或者有损合并到一个文件当中
 - 解包:就是归档的逆操作
    - 格式:shutil.unpack_archive(归档文件地址,解包地址)
    - 返回值:解包之后的地址
 
# zip - 压缩包
 - 模块名:zipfile
 - 创建一个ZipFile对象,表示一个zip文件.参数file表示文件的路径或者类文件对象
    - 格式:zipfile.ZipFile(zip文件路径)
# random 模块
 - 随机数
 - 所有的随机模块都是伪随机
 - random() 获取0-1之间的随机小数
    - 格式:random.random()
    - 返回值:随机0-1之间的小数
 - choice() 随机返回序列中的某个值
    - 格式:random.choice(序列)
    - 返回值:序列中的某个值
 - shuffle() 随机打乱原列表
    - 格式:random.shuffle(列表)
    - 返回值:None
# Log模块资料
