#!/usr/bin/python
# -*- coding: utf-8 -*-

# @File    : thread_queue_test.py
# @Time    : 2019/2/15 1:11
# @Author  : MaiXiaochai
# @Site    : https://github.com/MaiXiaochai


import time
import threading
from queue import Queue


def get_detail_html(queue):
    # 文章详情页
    while True:
        # get取数据，是一种阻塞的方法，即，若queue为空，会一直停在这儿
        url = queue.get()

        print("get detail html started.")
        time.sleep(2)
        print("get detail html end.")


def get_detail_url(queue):
    # 文章列表页
    print("get detail url started.")
    time.sleep(4)

    for i in range(20):
        # put向队列里放数据
        queue.put("http://projeect/{}".format(i))
    print("get detail url end.")


def main_var():
    # 这里如果Queue过大的话会对内存有影响，所以设置一个最大值
    detail_url_queue = Queue(1000)

    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue, ))
    thread_detail_url.start()

    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue, ))
        html_thread.start()

    start_time = time.time()
    print("last time: {}".format(time.time() - start_time))


if __name__ == '__main__':
    main_var()
