import xml.etree.ElementTree as et
# 生成一个新的元素Student
stu = et.Element("Student1")
# 生成一个Student的子元素Name
name = et.SubElement(stu, "Name")
# 给Name添加一个属性lang并赋值en
name.attrib = {'lang', 'en'}
name.text = 'jim'

age = et.SubElement(stu, 'Age')
age.text = 23
et.dump(stu)
