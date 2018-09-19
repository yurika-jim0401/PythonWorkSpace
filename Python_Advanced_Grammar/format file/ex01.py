import xml.dom.minidom
# 负责分析xml文件
from xml.dom.minidom import parse
# 使用minidom打开xml文件
DOMTree = xml.dom.minidom.parse("exam.xml")
# 得到文档对象
doc = DOMTree.documentElement

# 显示子元素
for ele in doc.childNodes:
    if ele.nodeName == "Student":
        print("------Node:{0}------".format(ele.nodeName))
        childs = ele.childNodes
        for child in childs:
            if child.nodeName == "name":
                # data是文本节点的一个属性,表示他的值
                print("name:{0}".format(child.childNodes[0].data))
                if child.hasAttribute("detail"):
                    print("Student-detail:{0}".format(child.getAttribute("detail")))
            if child.nodeName == "age":
                # data是文本节点的一个属性,表示他的值
                print("age:{0}".format(child.childNodes[0].data))

