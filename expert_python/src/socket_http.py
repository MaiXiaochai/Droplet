#!/usr/bin/python
# -*- coding: utf-8 -*-

# @File    : socket_http.py
# @Time    : 2019/3/4 23:26
# @Author  : MaiXiaochai
# @Site    : https://github.com/MaiXiaochai

import socket
from urllib.parse import urlparse


def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        # http的一种请求方式
        path = '/'

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 注意这里是80端口
    client.connect((host, 80))

    # 注意数据格式
    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf8'))

    # 注意这里如何接收所有数据
    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break

    # 这里注意编码不一定是utf8，视网站而定
    data = data.decode('utf8')
    print(data)
    client.close()


if __name__ == "__main__":
    url = 'http://www.baidu.com'
    get_url(url)
