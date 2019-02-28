#!/usr/bin/python
# -*- coding: utf-8 -*-

# @File    : socket_client.py
# @Time    : 2019/2/28 23:19
# @Author  : MaiXiaochai
# @Site    : https://github.com/MaiXiaochai


import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 明确指明自己地址
client.connect(('127.0.0.1', 8000))

# 因为接收byte类型
client.send('bobby'.encode('utf8'))
data = client.recv(1024)
print(data.decode('utf8'))
client.close()
