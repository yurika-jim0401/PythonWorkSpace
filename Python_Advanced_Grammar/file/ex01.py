import time
# 打开文件,用写的方式
# f称为文件句柄
# 字符串前加r后表示字符串内容不需要转义,方便\等符号写法
f = open(r"F:\PythonWorkSpace\pest2.txt", 'w')
# 文件打开后必须关闭(特别是以写方式打开)
f.close()

# with语句案例
with open(r"F:\PythonWorkSpace\pest2.txt", 'r') as f:
    # 下面的语句块就可以开始对文件f进行操作
    # 在这个模块中就不需要再使用close关闭文件f
    pass

with open(r"F:\PythonWorkSpace\pest.txt", 'r') as f1:
    # 按行读取内容
    strline = f1.readline()
    # 此结构保证能完整读取文件直到结束
    while strline:
        print(strline)
        strline = f1.readline()


# list 能用打开的文件作为参数,把文件内每一行内容作为一个元素
with open(r"F:\PythonWorkSpace\pest.txt", 'r') as f2:
    # 以打开的文件f作为参数,创建列表
    content_line = list(f2)
    for i in content_line:
        print(i)

# read是按字符读取文件内容
# 允许输入参数决定读取几个字符,如果没有指定,从当前位置读取到结尾
# 否则,从当前位置读取指定个数字符
with open(r"F:\PythonWorkSpace\pest.txt", 'r') as f3:
    strChar = f3.read()
    # 除了最后一行,每一行行尾有换行符
    print(len(strChar))
    print(strChar)
    # 思考下这里为什么读不出字符
    strChar_single = f3.read(5)
    print(strChar_single)

# seek案例
# 打开文件后,从第5个字节开始读取
# 打开后读写指针在0处,即文件的开头
with open(r"F:\PythonWorkSpace\pest.txt", 'r') as f4:
    # seek移动的单位是字节,这里表示从文件开头0开始偏移,偏移4个字节,即指针现在在第5个字节处
    # 其实就是跳过功能
    f4.seek(4, 0)
    # 从当前位置开始读
    strChar = f4.read()
    print(strChar)

# 关于读取文件的练习
# 打开文件,三个字符一组读出内容,然后显示在屏幕上
# 每读一次,休息一秒钟
# 让程序暂停可以用sleep
print("-"*50)
with open(r"F:\PythonWorkSpace\pest.txt", 'r') as f5:
    # read参数的单位是字符,可以理解成一个字就是一个字符
    strChar_three = f5.read(3)
    while strChar_three:
        print(strChar_three)
        time.sleep(1)
        strChar_three = f5.read(3)
# 为什么运行结果不对,不是每行三个字符

# tell函数:tell的返回数字的单位是byte
with open(r"F:\PythonWorkSpace\pest.txt", 'r') as f6:
    strChar_three = f6.read(3)
    pos = f6.tell()
    while strChar_three:
        print(pos)
        print(strChar_three)
        strChar_three = f6.read(3)
        pos = f6.tell()

# write 案例
# 1. 向文件中追加一句话
with open(r"F:\PythonWorkSpace\pest.txt", 'a') as f7:
    f7.write("it's really, \ni think")
    # 可以直接写入多行,用writeline,参数为一个序列list
    seq = ["生活不仅有眼前的苟且\n", "还有远方的枸杞"]
    f7.writelines(seq)

