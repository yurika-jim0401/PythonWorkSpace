import re

title = u'<div>name</div><div>age</div>'

# p1为贪婪匹配 "."表示任意一个东西,"*"表示可以前面的"."的东西可以出现0次或任意次,
# 正则默认贪婪,这里找到了第一个 <div>name</div>,会继续往后找,又找到了<div>age</div>
p1 = re.compile(r'<div>.*</div>')
# p2为非贪婪匹配 加上了"?" 表示我要找的东西是非贪婪的,找到第一个<div>name</div>后,不会再向下找了
p2 = re.compile(r'<div>.*?</div>')

m1 = p1.search(title)
print(m1.group())

m2 = p2.search(title)
print(m2.group())
