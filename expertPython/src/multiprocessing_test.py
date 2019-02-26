#!/usr/bin/python
# -*- coding: utf-8 -*-

# @File    : multiprocessing_test.py
# @Time    : 2019/2/26 21:47
# @Author  : MaiXiaochai
# @Site    : https://github.com/MaiXiaochai

import time
import multiprocessing
from concurrent.futures import ProcessPoolExecutor


def get_html(n):
    time.sleep(n)
    print("sub process success")
    return n


def main_pool():
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # 异步提交任务
    # result = pool.apply_async(get_html, args=(3, ))
    #
    # # 等待所有任务执行完成，完成后就可以得到result数据了
    # pool.close()
    # pool.join()
    # print(result.get())
    """
    out:
    sub process success
    3
    """

    # # imap 与线程池中的map和Python中的map类似，结果按序返回
    # for result in pool.imap(get_html, [1, 5, 3]):
    #     print("{} sleep success".format(result))
    """
    out:
    sub process success
    1 sleep success
    sub process success
    sub process success
    5 sleep success
    3 sleep success
    """

    # imap_unordered 谁先完成，打印谁的结果
    for result in pool.imap_unordered(get_html, [1, 5, 3]):
        print("{} sleep success".format(result))
    """
    out:
    sub process success
    1 sleep success
    sub process success
    3 sleep success
    sub process success
    5 sleep success
    """


def main():
    process = multiprocessing.Process(target=get_html, args=(2, ))
    print(process.pid)
    process.start()
    print(process.pid)
    process.join()
    print("main progress end")
    """
    out:
    None
    10000
    sub process success
    main progress end
    """


if __name__ == "__main__":
    main_pool()


