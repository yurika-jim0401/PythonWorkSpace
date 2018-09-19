# 正则案例
import re
# 制定正则规则
# ()里的是一组的规则
# 这里的正则目的是: 要匹配的内容必须是可以分成两组,组和组之间用空格区分,每一组只能且至少包含一个小写字母
# 第二个参数I 表示忽略大小写
p = re.compile(r'([a-z]+) ([a-z]+)', re.I)

# 查找用的正则
p1 = re.compile(r'\d+')

# 替换用正则
p2 = re.compile(r'(\w+) (\w+)')

# 中文用匹配正则
p3 = re.compile(r'[\u4e00-\u9fa5]+')

m = p.match("I am really love yyt")

# 查找语法search,思考下跟ex09的match为什么不一样
m1 = p1.search("one12two34three567four")
# 查找所有符合规则的
rst = p1.findall("one12two34three567four")
# 替换用字符串
s = "hello 123 wang 456 yyt, i love you"
# 匹配中文用字符串,空格隔开两个中文或者标点也可以隔开
title = u'世界，你好,hello world'

# 开始匹配中文
rst2 = p3.findall(title)

# 开始替换,只要满足  (字母/数字 字母/数字)这种模式的,就被替换掉,这里预计会替换的内容为:
# 第一组: hello 123 第二组: wang 456 第三组: i love
rst1 = p2.sub(r'Hello world', s)

# 匹配的结果全部打印
print(m)
# group的参数如果为0表示所有匹配到的组,为1表示匹配出的第一组，为2表示...以此类推
print(m.group(2))
# start 和 end 的参数如果为0表示匹配到的所有组的起始位置和结束位置,为1表示第一组的起始位置和结束位置...以此类推
print(m.start(1))
print(m.end(1))
# groups表示打印出所有的组以元组格式
print(m.groups())

# 查看查找结果
print(m1.group())
print(rst)
print(rst1)
print(rst2)
