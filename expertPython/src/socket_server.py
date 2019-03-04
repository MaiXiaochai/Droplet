#!/usr/bin/python
# -*- coding: utf-8 -*-

# @File    : socket_server.py
# @Time    : 2019/2/28 23:19
# @Author  : MaiXiaochai
# @Site    : https://github.com/MaiXiaochai


import socket
import threading

# socket.AF_INET IPV4
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 参数为数组
server.bind(('0.0.0.0', 8000))
server.listen()


def handle_sock(sock, addr):
    # 一次获取1K的数据
    data = sock.recv(1024)
    print(data.decode('utf8'))
    re_data = input()
    # byte -> decode -> str -> encode -> byte
    sock.send(re_data.encode('utf8'))


# 这里的server端只能接收一个请求,因为后边是while循环
# 那么如何才能实现多用户连接?
# 多线程。

while True:
    # 获取从客户端发送的数据
    sock, addr = server.accept()
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

