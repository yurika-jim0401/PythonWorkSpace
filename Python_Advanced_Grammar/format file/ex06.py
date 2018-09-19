import xml.etree.ElementTree as et

# 在内存中创建一个空文档
etree = et.ElementTree()
e = et.Element('Student')
# 将文档etree的根设定为上面定义的元素Student
etree._setroot(e)
# 添加根元素Student的子元素Name
e_name = et.SubElement(e, 'Name')
e_name.text = "jim"
etree.write("etree_creat.xml")
