#!/usr/bin/python
# -*- coding: utf-8 -*-

# @File    : socket_server.py
# @Time    : 2019/2/28 23:19
# @Author  : MaiXiaochai
# @Site    : https://github.com/MaiXiaochai


import socket

# socket.AF_INET IPV4
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 参数为数组
server.bind(('0.0.0.0', 8000))
server.listen()
sock, add = server.accept()

# 获取从客户端发送的数据
# 一次获取1K的数据
data = sock.recv(1024)
print(data.decode('utf8'))

# byte -> decode -> str -> encode -> byte
sock.send("hello, {}".format(data.decode('utf8')).encode('utf8'))
server.close()
sock.close()
