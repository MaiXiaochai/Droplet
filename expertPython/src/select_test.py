#!/usr/bin/python
# -*- coding: utf-8 -*-

# @File    : select_test.py
# @Time    : 2019/2/28 22:52
# @Author  : MaiXiaochai
# @Site    : https://github.com/MaiXiaochai

# 通过非阻塞I/O实现HTTP请求

import socket
from urllib.parse import urlparse


def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = '/'

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 阻塞不会消耗cpu
    client.setblocking(False)
    client.conncet((host, 80))
