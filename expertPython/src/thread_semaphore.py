#!/usr/bin/python
# -*- coding: utf-8 -*-

# @File    : thread_semaphore.py
# @Time    : 2019/2/20 23:13
# @Author  : MaiXiaochai
# @Site    : https://github.com/MaiXiaochai

# semaphore 信号量

import threading
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        time.sleep(2)
        print("got html text success")


class UrlProducer(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(20):
            html_thread = HtmlSpider("https://baidu.com/{}".format(i))
            html_thread.start()


if __name__ == "__main__":
    url_producer = UrlProducer()
    url_producer.start()
