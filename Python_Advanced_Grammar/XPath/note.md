# XPath
 - 在XML文件中查找信息的一套规则/语言,根据XML的元素或者属性进行遍历
 - http://www.w3school.com.cn/xpath/index.asp
# XPath 开发工具
 - 开源的XPath表达式编辑工具: XMLQuire
 - Chrome插件: XPath Helper
 - Firefox插件: XPath Checker
# 选取XML文件的节点
 - nodename: 选取此节点的所有子节点
 - /: 从根节点开始选取
 
 
        /Student  从根节点开始查找这个节点,查不到,没有
        /School 从根节点开始查找名为School的节点,能找到
 - //: 选取节点,不考虑位置
 
 
        //age  有多少个age节点都能找出了,组成一个列表返回
 - "." : 选取当前节点
 - ".." : 选取当前节点的父节点
 - "@" : 选取属性
 - xpath中查找一般按照路径方法查找
 
 
        School/Teacher : 返回Teacher节点
        School/Student : 返回两个Student节点,以list形式
        //Student : 选取所有Student的节点,不考虑位置
        School//age : 选取School后代中所有age节点, 不考虑School之后的所有位置
        //@detail : 选取所有的detail属性
        //age[@detail] : 选取带有detail属性的age元素
# 谓语-Predicates
 - /School/Student[1] : 选取School下面的第一个Student节点
 - /School/Student[last()] : 选取School下面的最后一个Student节点
 - /School/Student[last()-1] : 选取School下面的倒数第二个Student节点
 - /School/Student[position()<3] : 选取School下面的前两个Student节点
 - //School[@score] : 选取带有属性score的Student节点
 - //School[@score="99"] : 选取带有属性score并且其值是99的Student节点
 - //School[@score]/Age : 选取带有属性score的Student节点的子节点Age
 
# XPath的一些操作
 - | : 或者
 
        
        //Student[@score] | //Teacher : 选取带有属性score的Student节点 或者(和) Teacher节点
        
 - 其余不常见XPath运算符合包括 +, -, *, div, >, <
 
 
 
 
