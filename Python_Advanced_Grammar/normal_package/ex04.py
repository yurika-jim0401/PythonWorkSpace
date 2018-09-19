# -*- coding:utf-8 -*-
# OS模块案例
import os

# 获取当前的工作目录
mydir = os.getcwd()
print(mydir)

# 改变当前的工作目录
os.chdir("F:\PythonWorkSpace")
print(os.getcwd())

# 获取一个目录中所有子目录和文件的名称列表
ld = os.listdir()
print(ld)

# 创建一个文件夹,参数exit_ok=True时,若文件已存在,语句仍会执行,不会报错
# 参数exit_ok默认值为False,如果不写,若文件已存在,会报错
rst = os.makedirs("jim",exist_ok=True)

# 运行系统命令 创建一个文件夹
# rst = os.system("mkdir jimsys")

# 获取指定环境变量的值,windows的下的：
# 当前目录:"."
# 父目录:".."
# 路径分隔符:"\"
# 换行符:"\r\n"
# 操作系统名称:"nt"
# linux下的:
# 当前目录:"."
# 父目录:".."
# 路径分隔符:"/"
# 换行符:"\n"
# 操作系统名称:"posix"
# 因为linux和windows的有些不同,所以拼写路径的时候最好不要自己手写,而使用os.path模块
print(os.getenv("PATH"))
print(os.pardir)

# os.path模块相关方法
import os.path as op
absp = op.abspath(os.getcwd())
print(absp)
# basename 返回指定路径的最后一个文件夹的名字或文件名
bn = op.basename(os.getcwd())
print(bn)

# jion 组合路径,这样拼成的地址具有可移植性
fn = "jimjion"
p = op.join(os.getcwd(),fn)
print(p)

# split 切割
t = op.split("F:\PythonWorkSpace\jim")
# 或者这样写更方便
d,p = op.split("F:\PythonWorkSpace\jim")
# isdir() 判断是否为目录
print(op.isdir("F:\PythonWorkSpace\jim"))
# exists() 判断文件或者目录是否存在
print(op.exists("F:\PythonWorkSpace\jim"))