import ex01 as st

# 正常来讲，由于Python的变量名不能以数字开头，但是如果以数字开头的py文件导入时，就会有问题
# 借助于importlib包可以实现导入以数字开头的模块名称
import importlib
# 将该包重新命名
ex = importlib.import_module("01")

stu = st.Student("jim",23)
stu.say()
st.sayHello()