# -*- coding: utf-8 -*-

# @file:               python_thread.py
# @Author:             MaiXiaochai
# @Date:               2019-02-14 21:52:25
# @Last Modified by:   MaiXiaochai
# @Last Modified time: 2019-02-14 22:14:57
# @GitHub:             https://github.com/MaiXiaochai

import time
import threading


# 模拟小爬虫,一个线程爬取列表页，一个爬虫爬取详情页


def get_detail_html(url):
    print("get detail html started.")

    # 模拟网络请求的延迟
    time.sleep(2)
    print("get detail html end.")


def get_detail_url(url):
    print("get detail url started.")

    # 模拟网络请求的延迟
    time.sleep(4)
    print("get detail url end.")


def main1():
    thread1 = threading.Thread(target=get_detail_html, args=("",))
    thread2 = threading.Thread(target=get_detail_url, args=("",))
    start_time = time.time()

    # thread1.setDaemon(True)
    # thread2.setDaemon(True)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("last time: {}".format(time.time() - start_time))

    """
    out:
    get detail html started.
    get detail url started.last time: 0.0009963512420654297

    get detail html end.
    get detail url end.

    > 为什么是0秒（执行过程是怎样的）？
    因为在if下边有三个线程，剩下的其他代码是主线程，这里是print。
    在Thread1、2 sleep后print开始运行。
    print运行完成后，主线程并未退出。

    --------------------------------------------------------------------
    需求1：当主线程退出的时候，kill掉子线程

    >解决：将Thread1、2设置成守护线程setDaemon(True)
    setDaemon(True)的作用是：将线程设置为守护线程，当主线程退出后，守护线程会被关闭。

    out:
    get detail html started.
    get detail url started.
    last time: 0.0009615421295166016

    --------------------------------------------------------------------
    需求2：等待Thread1、2运行完成之后再运行print

    >解决： join方法
    join会阻塞在主线程print前，直到Thread1、2执行完成之后，print才执行

    out:
    get detail html started.
    get detail url started.
    get detail url end.
    get detail html end.
    last time: 4.001549005508423

    """


# ===========================================================
class GetDetailHtml(threading.Thread):
    # 这里给线程起个名字，如果run中用到参数，也可以在这里传入
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        # run方法下放逻辑
        print("get detail html started.")

        # 模拟网络请求的延迟
        time.sleep(2)
        print("get detail html end.")


class GetDetailUrl(threading.Thread):
    # 这里给线程起个名字，如果run中用到参数，也可以在这里传入
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started.")

        # 模拟网络请求的延迟
        time.sleep(4)
        print("get detail url end.")


def main2():
    thread1 = GetDetailHtml('get_detail_html')
    thread2 = GetDetailUrl('get_detail_url')

    start_time = time.time()
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("last time: {}".format(time.time() - start_time))


if __name__ == "__main__":
    # main1()

    main2()
    """
    get detail html started.
    get detail url started.
    get detail html end.
    get detail url end.
    last time: 4.002530574798584
    """
