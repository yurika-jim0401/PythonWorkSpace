"""
- 服务器(server)端:
    - 1.建立socket,socket是赋值具体通信的一个实例
    - 2.port+ip 绑定:为创建的socket指派固定的端口和ip地址
    - 3.接受访问
    - 4.返回信息(非必须步骤)
"""
import socket
import time

def serverFunc():
    # 1.建立socket
    # socket.AF_INET: 使用ipv4协议族
    # socket.SOCK_DGRAM: 使用UDP通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定ip地址和端口(port)号
    # 127.0.0.1 : 这个ip地址代表的是机器本身
    # 7852: 随便指定的端口号
    # 地址是一个tuple类型(ip,port)
    # ip是字符串,port是数字
    addr = ("127.0.0.1", 7852)
    sock.bind(addr)

    # 3.接收对方的消息
    # 等待方式为死等,没有其他可能
    # recvfrom接收,返回值是一个元组,前一项表示数据,后一项表示地址(客户端的地址)
    # 参数的含义是缓冲区大小
    data, addr = sock.recvfrom(500)
    print(data)
    print(type(data))
    # 发送过来的数据是bytes格式,必须通过解码才能得到str格式内容
    # decode默认参数是utf8
    text = data.decode()
    print(text)

    # 4.给对方返回信息
    rsp = "我已经接收到信息了!"
    # 发送过去前需要将字符串编码成bytes格式
    # 默认是utf8,编码跟解码必须一致
    data = rsp.encode()
    # 发送用sendto()这是UDP格式发送
    sock.sendto(data, addr)


if __name__ == '__main__':
    print("starting server...")
    # 服务器端无限运行
    while True:
        try:
            serverFunc()
        except Exception as e:
            print(e)
        time.sleep(1)