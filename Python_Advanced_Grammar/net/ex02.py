"""
- 客户(client)端:
    - 1.建立socket端口
    - 2.发送消息(要有ip+port)到指定服务器
    - 3.等待反馈
"""
import socket


def clientFunc():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    text = "i love yyt"

    # 发送的数据必须编码为bytes格式
    srt = text.encode()

    # 发送消息
    addr = ("127.0.0.1", 7852)
    sock.sendto(srt, addr)

    # 等待反馈
    data, server_addr = sock.recvfrom(200)
    data_decode = data.decode()
    print(data_decode)


if __name__ == '__main__':
    clientFunc()
