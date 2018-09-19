import xml.etree.ElementTree
assert isinstance(xml.etree.ElementTree.parse,xml.etree.ElementTree.parse().getroot())
tree = xml.etree.ElementTree.parse("student_edit.xml")
root = tree.getroot()
for e in root.iter('Name'):
    print(e.text)

for stu in root.iter('Student'):
    name = stu.find('Name')
    if name is not None:
        name.set('test', name.text * 2)

stu = root.find('Student')

# 生成一个新的元素
e = xml.etree.ElementTree.Element('ADDer')
e.attrib = {'A':'B'}
e.text = '新加的'
stu.append(e)

# 一定要把修改后的内容写回文件,否则修改无效
tree.write('student_edit.xml')

