# mail编程
## 邮件工作流程
 - MUA(MailUserAgent) 邮件用户代理
 - MTA(MailTransferAgent) 邮件传输代理
 - MDA(MailDeliveryAgent) 邮件投递代理
 - 247993972@qq.com 
 - jimjx@icloud.com
 - 流程
    - 1.MUA -> MTA 邮件已经在服务器上了
    - 2.qq MTA ->...-> iCloud MTA, 邮件在苹果服务器上
    - 3.iCloud MTA -> iCloud MDA,此时邮件已经在你的邮箱里了
    - 4.iCloud MDA -> MUA 邮件下载到本地电脑
 - 编写程序
    - 发送:  MUA->MTA with SMTP:SimpleMailTransferProtocol,包含MTA->MTA
    - 接受:  MDA->MUA with POP3 and IMAP:PostOfficeProtocol v3 and 
      InternetMessageAccessProtocol v4
 - 准备工作
    - 注册邮箱
    - 第三方邮箱需要授权设置
        - 进入设置中心
        - 取得授权码
 - Python for main
    - SMTP协议负责发送邮件
        - 使用email模块构建邮件
            - 纯文本邮件(案例见ex01)
        - HTML格式邮件发送(案例见ex02)
            - 准备HTML代码作为内容
            - 把邮件的subtype设置为html
            - 发送 
        - 发送带附件的邮件(案例见ex03)
            - 可以把邮件看做一个文本邮件和一个附件邮件的合体
            - 一封邮件如果涉及多个部分,需要使用MIMEMultipart格式构建
            - 添加一个MIMEText正文
            - 添加一个MIMEBase或者MIMEText作为附件
        - 添加邮件头,抄送等信息(案例见ex04)
            - mail["From"] 表示发送者的信息,包括姓名和邮件
            - mail["To"] 表示接收者的信息,包括姓名和邮件地址
            - mail["Subject"] 表示摘要或者主体信息
        - 同时支持html和text格式的邮件(案例见ex05)
            - 构建一个MIMEMultipart格式邮件
            - MIMEMultipart的subtype设置成alternative格式
            - 添加HTML和text邮件
        - 使用smtplib模块发送邮件
    - POP3协议负责接收邮件(案例见ex06)
        - 本质上是MDA到MUA的一个过程
        - 从MDA上下载下来的是一个完整的邮件结构体,需要解析才能得到每个具体的内容
        - 步骤:
            - 1.用poplib下载邮件结构体原始内容
                - 1)准备相应内容(邮件地址,密码,pop3实例)
                - 2)身份认证
                - 3)一般会先得到邮箱内邮件的整体列表
                - 4)根据相应序号,得到某一封信的数据流
                - 5)利用解析函数进行解析出相应的邮件结构体
            - 2.用email解析邮件的具体内容
        
                
                
                - 1)准备相应内容(邮件地址,密码,pop3实例)
                
                - 1)准备相应内容(邮件地址,密码,pop3实例)
                
                
                