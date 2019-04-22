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
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("got html text success")
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            # 每调用一次acquire方法，sem内部计数减1
            # acquire和release方法成对儿使用
            # 这个release要在Spider内部主代码执行完成后再释放，才是准确的
            self.sem.acquire()
            html_thread = HtmlSpider("https://baidu.com/{}".format(i), self.sem)
            html_thread.start()


if __name__ == "__main__":
    sem = threading.Semaphore(3)
    url_producer = UrlProducer(sem)
    url_producer.start()
