import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase,MIMEMultipart

# 先构建邮件(包括正文和附件的邮件)
mail_mul = MIMEMultipart()

# 构建邮件正文
# MIMEText 三个主要参数
# 1.邮件内容
# 2.MIME子类型,此案例用plain表示text类型
# 3.邮件编码格式
mail_text = MIMEText("Hello,I am jim", "plain", "utf-8")

# 把构建好的邮件正文附加进邮件中
mail_mul.attach(mail_text)

# 构建附件
# 需要先从本地读入附件
# 以rb格式打开本地文件
with open("attach.html", 'rb') as f:
    s = f.read()
    # 设置附件的MIME 和文件名
    m = MIMEText(s, 'base64', "utf-8")
    m["Content-Type"] = "application/octet-stream"
    # 需要注意几点:1.attachment后为分好的英文状态 2.filename后面需要用引号包裹
    m["Content-Disposition"] = "attachment; filename='attach.html'"
    # 将组装好内容和格式的附件添加进邮件中
    mail_mul.attach(m)


# 发送email地址,此处地址直接使用QQ邮箱
from_addrr = "247993972@qq.com"
# 密码是授权码
from_pwd = "azmclajgpejybjea"
# 收件人信息
to_addr = "jimjx@icloud.com"

# 输入SMTP服务器地址
# 此处根据不同的邮件服务商有不同的值
# 任何一家邮件服务商,如果采用第三方收发邮件,都需要开启授权选项

smtp_srv = "smtp.qq.com"

try:
    # SMTP协议默认端口25
    # 第一个参数是服务器地址,一定是bytes格式,所以需要编码
    # 第二个参数是服务器的接受访问端口,465是默认的安全访问SSL的端口
    # 这里已经生成了一个服务器的实例srv
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)
    # 登录邮箱发送
    srv.login(from_addrr, from_pwd)
    # 发送邮件,三个参数:
    # 1.发送地址 2.接收地址,list格式 3.发送内容,作为字符串发送
    srv.sendmail(from_addrr, [to_addr], mail_mul.as_string())
    srv.quit()
except Exception as e:
    print(e)
