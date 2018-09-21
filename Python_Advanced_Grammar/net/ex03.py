"""
- Server端编程:
        - 1.建立socket负责具体通信,这个socket其实只负责接收对方的请求,真正通信的是链接后重新建立的socket
        - 2.绑定端口和地址
        - 3.监听接入的访问socket
        - 4.接收访问的socket,其实就是接受访问即建立了一个通讯的链接通路
        - 5.接收对方的发送内容,给对方发送反馈信息
        - 6.如果有必要,给对方发送反馈信息
        - 7.关闭链接通路
"""
import socket


def tcp_srv():
    # 1.建立socket负责具体通信,这个socket其实只负责接收对方的请求,真正通信的是链接后重新建立的socket
    # 这里有两个参数: 1)表明IP地址类型为ipv4  2)表明使用的是tcp协议通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定端口和地址
    # 地址信息是一个元组类型,一共有两个部分,第一部分为字符串类型的ip地址,第二部分为数字型端口号
    addr = ("127.0.0.1", 8998)
    sock.bind(addr)

    # 3.监听接入的访问socket
    sock.listen()

    while True:
        # 4.接收访问的socket, 其实就是接受访问即建立了一个通讯的链接通路
        # accept返回的元组第一个元素赋值给skt(此为接收的客户端的socket),第二个赋值个addr
        skt, client_addr = sock.accept()

        # 5.接收对方的发送内容,给对方发送反馈信息
        # 500代表接收使用的buffersize
        msg = skt.recv(500)
        # 接收到的是bytes格式的内容,要得到str格式,必须先解码
        msg = msg.decode()
        # 打印接收的信息到屏幕
        rst = "received msg :{0} from {1}".format(msg, client_addr)
        print(rst)

        # 6.如果有必要,给对方发送反馈信息
        skt.send(rst.encode())

        # 7.关闭链接通路
        skt.close()


if __name__ == '__main__':
    print("starting server...")
    tcp_srv()
    print("ending server...")
