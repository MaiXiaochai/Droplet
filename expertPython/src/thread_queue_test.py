#!/usr/bin/python
# -*- coding: utf-8 -*-

# @File    : thread_queue_test.py
# @Time    : 2019/2/15 1:11
# @Author  : MaiXiaochai
# @Site    : https://github.com/MaiXiaochai


import time
import threading
from queue import Queue


def get_detail_html(detail_url_list):
    # 文章详情页
    while True:
        if detail_url_list:
            url = detail_url_list.pop()

            print("get detail html started.")
            time.sleep(2)
            print("get detail html end.")


def get_detail_url(detail_url_list):
    # 文章列表页
    print("get detail url started.")
    time.sleep(4)
    for i in range(20):
        detail_url_list.append("http://projeect/{}".format(i))
    print("get detail url end.")


def main_var():
    thread_detail_url = threading.Thread(target=get_detail_url, args=variables.detail_url_list)
    thread_detail_url.start()

    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=variables.detail_url_list)
        html_thread.start()

    start_time = time.time()
    print("last time: {}".format(time.time() - start_time))