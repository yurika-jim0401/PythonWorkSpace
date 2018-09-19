# 格式化文件存储
 - xml,json
 - 为了解决不同设置直接的信息移植问题
 - xml
 - json
# xml文件
 - 参考资料
    - https://docs.python.org/3/library/xml.etree.elementtree.html
    - http://www.runoob.com/python/python-xml.html
    - https://blog.csdn.net/seetheworld518/article/details/49535285
 - XML(eXtensibleMarkupLanguage), 可扩展标记语言
    - 标记语言: 语言中使用尖括号括起来的文本字符串标记
    - 可扩展: 用户可以自定义需要的标记
    - 例如:
        
        
        <Teacher>
            自定义标记Teacher
            在两个标记直接任何内容都应该跟Teacher有关
        </Teacher>
      
 
 - 是w3c组织制定的一个标准
 - XML描述的是数据本身,即数据的结构和语义
 - HTML侧重于如何显示web页面中的数据
 - XML文档的构成(案例见exam.xml)
    - 处理指令(可以认为一个文件内只有一个处理指令): 
        - 最多只有一行,且必须在第一行
        - 内容是与xml本身处理相关的一些声明或者指令
        - 以xml关键字开头
        - 一般用于声明XML的版本和采用的编码
            - version控制版本
            - encoding控制编码
    - 根元素(一个文件内只有一个根元素)
        - 在整个xml文件中,可以把他看做一个树形结构
        - 根元素有且只有一个
    - 子元素
    - 属性
    - 内容
        - 表明标签所存储的信息
    - 注释
        - 其说明作用的信息
        - 注释不能嵌套在标签里
        - 只有在注释的开始和结尾使用双短横线
        - 三短横线只能出现在注释的开头而不能用在结尾
        
        
         <name> <!-- wangdapeng -->   </name> #可以
         <name <!-- wangdapeng -->>   </name> #不可以，注释在标签内
         <!--my-name-by-wang--> #可以，注释内容可以有一个短横线
         <!--my--name--by--wang-->#不可以，双短横线只能出现在开头或结尾
         <!---my-name--> #可以， 三短横线只能出现在开头
         <!---my-name---> #不可以， 三短横线只能出现在开头 
 - 保留字符的处理
    - XML中使用的符号可能跟实际符号相冲突,典型的就是左右尖括号
    - 使用实体引用(EntityReference)来表示保留字节
          
          
         <score> score>80 </score> #有错误，xml中不能出现>
         <score> score&gt;80</score> #使用实体引用,  &gt; 就是表示 >
    
   - 把包含有保留字的部分放在CDATA块内部,CDATA块把内部信息视为不需要转义
   
         
         <![CDATA[
            select name,age
            from Student
            where score>80
            ]]>
    
   - 常用的需要转义的保留字符合对应实体引用
        - &: &amp;
        - <: &lt;
        - >: &gt;
        - ': &apos;
        - ": &quot;
        - 一共有五个,每个实体引用都以&开头;结尾
 - XML标签的命名规则
    - Pascal命名法
        - 用单词表示,第一个字母大写
        - 大小写严格区分
        - 配对的标签必须一致
 - 命名空间
   - 为了防止命名冲突
    
      
      <Student>
        <Name>LiuYing</Name>
        <Age>23</Age>
      </Student>
      <Room>
        <Name>2014</Name>
        <Location>1-23-1</Location>
      </Room>         
    
   -如果归并上述两个内容的信息,会产生冲突
   
        
       <Schooler>
           <Name>LiuYing</Name>
           <Age>23</Age>
           <Name>2014</Name>
           <Location>1-23-1</Location>
       </Schooler>
    
   - 为了避免冲突,需要给可能产生冲突元素添加命名空间
   - xmlns: xml name space
        
       
        <Schooler xmlns:student="http://my_student" xmlns:room="http://my_room">
            <student:Name>LiuYing</student:Name>
            <Age>23</Age>
            <romm:Name>2014</room:Name>
            <Location>1-23-1</Location>
        </Schooler>

# XML访问
## 读取
 - XML读取分为两个主要技术:SAX,DOM
 - SAX(Simple API for XML):
    - 基于事件驱动的API
    - 利用SAX解析文档设计到解析器和事件处理两部分
    - 特点:
        - 快
        - 流式读取
 - DOM
    - 是W3C规定的XML编程接口
    - 一个XML文件在缓存中以树形结构保存,读取
    - 用途:
        - 定位浏览XML任何一个节点信息
        - 添加删除相应内容
    - 工具:
        - minidom(案例见ex01)
            - minidom.parse(filename):加载读取的xml文件, filename也可以是xml代码
            - doc.documentElement:获取xml文档对象，一个xml文件只有一个对于的文档对象
            - node.getAttribute(attr_name):获取xml节点的属性值
            - node.getElementByTagName(tage_name)：得到一个节点对象集合
            - node.childNodes:得到所有孩子节点
            - node.childNodes[index].nodeValue:获取单个节点值
            - node.firstNode:得到第一个节点，等价于node.childNodes[0]
            - node.attributes[tage_name]
        - etree(案例见ex02)
            - 以树形结构来表示xml
            - root.getiterator:得到相应的可迭代的node集合
            - root.iter
            - find(node_name):查找指定node_name的节点,返回一个node
            - root.findall(node_name):返回多个node_name的节点
            - node.tag: node对应的tagename
            - node.text:node的文本值
            - node.attrib： 是node的属性的字典类型的内容
## xml文件写入(案例见ex03)
 - 更改
    - ele.set:修改属性
    - ele.append:添加子元素
    - ele.remove:删除子元素
 - 生成/创建
    - SubElement(案例见ex04)
    - Minidom(案例见ex05)
    - etree(案例见ex06) 

# json
 - 在线工具
    - https://www.sojson.com/
    - http://www.w3school.com.cn/json/
    - http://www.runoob.com/json/json-tutorial.html
 - JSON(JavaScriptObjectNotataion)
 - 轻量级的数据交换格式,基于ECMAScript
 - json格式是一个键值对形式的数据集
    - key:字符串
    - value:字符串,数字,列表,json
    - json使用大括号包裹
    - 键值对之间用逗号隔开
    
        
        student={"name":"jim","age":18,"mobile":"18018598984"}
        
 - json和python格式的对应
    - 字符串: 字符串
    - 数字: 数字
    - 队列: list
    - 对象: dict
    - 布尔值: 布尔值
 - python for json 
    - json包
    - json和python对象的转换(案例见ex07)
        - json.dumps():对数据编码,把python格式表示成json格式
        - json.loads():对数据解码,把json格式转换成python格式
    - python读取json文件(案例见ex08)
        - json.dump(): 把内容写入文件
        - json.load(): 把json文件内容读入python
        
# 正则表达式(RegularExpression, re)
 - 是一个计算机科学的概念
 - 用于使用单个字符串来描述,匹配符合某个规则的字符串
 - 常常用来检索、替换某些模式的文本

# 正则的写法
 - .(点号): 表示任意一个字符,除了\n,比如:查找所有的一个字符
 - "[ ]":匹配中括号中列举的任意字符,比如:[L,Y,0], LLY,Y0,LIU 前两个可以,最后一个不可以
 - \d: 任意一个数字
 - \D: 除了数字以外的任何一个
 - \s: 表示空格,tab键
 - \S: 除了空白符合
 - \w: 单词字符,就是a-z,A-Z,0-9._
 - \W: 除了以上的都可以
 - " * " : 表示前面内容重复零次或者多次,  \w* 表示a-z,A-Z,0-9出现多次或没有
 - "+" : 表示前面内容至少出现一次 \w+
 - ? : 表示前面出现的内容为零次或一次
 - {m,n}:允许前面内容出现最少m次，最多n次
 - ^:匹配字符串的开始
 - $:匹配字符串的结尾
 - \b:匹配单词的边界
 - ():对正则表达式内容进行分组， 从第一个括号开始，编号逐渐增大


      验证一个数字： ^\d$
      必须有一个数字，最少一位：^\d+$
      只能出现数字，且位数为5-10位： ^\d{5,10}$
      注册者输入年龄，要求16岁以上，99岁以下： ^[16-99]$
      只能输入英文字符和数字： ^[A-Za-z0-9]$
      验证qq号码： [0-9]{5,12}
 - \A: 只匹配字符串开头， \Aabcd, 则abcd
 - \Z: 仅匹配字符串末尾， abcd\Z, abcd
 - |: 左右任意一个
 - (?P...): 分组，除了原来的编号再制定一个别名， (?P12345){2}， 1234512345
 - (?P=name): 引用分组
 
# RE使用大致步骤
 - 使用compile将表示正则的字符串编译为一个pattern对象
 - 通过pattern对象提供一系列方法对文本进行查找匹配,获得匹配结果,一个Match对象
 - 最后使用Match对象提供的属性和方法获得信息,根据需要进行操作
# RE常用函数(案例见ex09 ex10)
 - group(): 获得一个或者多个分组匹配的字符串,当要获得整个匹配的子串时,直接使用group或者goup(0)
 - start: 获取分组匹配的子串在整个字符串中的起始位置,参数默认为0
 - end: 获取分组匹配的子串在整个字符串中的结束位置,默认为0
 - span: 返回结构技术(start(group),end(group)) 
# 查找(案例见ex10)
 - search(str, [,pos[, endpos]]): 在字符串中查找匹配,pos和endpos表示起始位置
 - findall: 查找所有
 - finditer : 查找,返回一个iter结果
# sub替换(案例见ex10)
 - sub(rep1, str[, count])
 
# 匹配中文(案例见ex10)
 - 大部分中文内容表示范围是[u4e00-u9fa5],不包括全角标点
# 贪婪和非贪婪(案例见ex11)
 - 贪婪:尽可能多的匹配, (*)表示贪婪匹配
 - 非贪婪:找到符合条件的最小内容即可, (?)表示非贪婪
 - 正则默认使用贪婪匹配