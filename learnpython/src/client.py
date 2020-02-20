#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""author:hahahtm
   date:

"""
from socket import *


# 创建socket
tcp_client_socket = socket()

# 目的信息
server_ip = input("请输入服务器ip:")
server_port = int(input("请输入服务器port:"))

if "" in server_ip:
    server_ip = "127.0.0.1"


# 链接服务器
tcp_client_socket.connect((server_ip, server_port))

while True:
    # 提示用户输入数据
    send_data = input("请输入要发送的数据：")

    tcp_client_socket.send(send_data.encode("utf-8"))

    # 接收对方发送过来的数据，最大接收1024个字节
    recvData = tcp_client_socket.recv(1024)
    print('接收到的数据为:', recvData.decode('utf-8'))

# 关闭套接字
tcp_client_socket.close()