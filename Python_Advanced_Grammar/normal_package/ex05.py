# coding=gbk
import shutil
import zipfile
import random
# shutil 模块方法案例
# copy() 复制文件
rst = shutil.copy("F:\PythonWorkSpace\pest.txt","F:\PythonWorkSpace\jim\pest1.txt")
print(rst)
# copyfile()
shutil.copy("F:\PythonWorkSpace\pest.txt","F:\PythonWorkSpace\jim\pest1.txt")

# help(shutil.make_archive)
# 想得到一个叫做guidang.my的归档文件
ma = shutil.make_archive("F:\PythonWorkSpace\guidang","zip","F:\PythonWorkSpace\jim")
print(ma)

# zipfile包案例
zf = zipfile.ZipFile("F:\PythonWorkSpace\yasuo.zip")

# 获取zip文档内指定文件的信息,返回一个zipfile.ZipInfo对象,包括文件的详细信息
print(zf.getinfo("pest1.txt"))

# ZipFile.namelist()
# 获取zip文档内所有文件的名称列表
nl = zf.namelist()
print(nl)

# ZipFile.extractall([path[,members[,pwd]]])
# 解压zip文档中的所有文件到当前目录。参数members的默认值为zip文档内所有文件名称列表
rst = zf.extractall("F:\PythonWorkSpace")

# random函数，返回一个0-1的随机小数
print(random.random())
# random(a,b),返回a到b之间的一个随机整数,左闭右闭
print(random.randint(1,100))
# choice() 随机返回序列中的某个值
l = [str(i)+"haha" for i in range(10)]
print(l)
rss = random.choice(l)
print(rss)

# shuffle() 打乱原序列,并返回一个None
l1 = [i for i in range(10)]
print(l1)
l2 = random.shuffle(l1)
print(l1)
print(l2)
