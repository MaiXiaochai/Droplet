#!/usr/bin/python
# -*- coding: utf-8 -*-

# @File    : thread_sync.py
# @Time    : 2019/2/16 0:27
# @Author  : MaiXiaochai
# @Site    : https://github.com/MaiXiaochai


import threading
from threading import Lock


lock = Lock()
total = 0


def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total += 1
        lock.release()


def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


def add1(a):
    """
    字节码执行过程如下，
    如果多线程同时执行 add1和desc1，
    每执行一行字节码之后，GIL都有可能释放，因为它的时间片已经用尽。
    add1的每行字节码与desc1的每行字节码交替运行，当都到达第4行时，
    赋值的先后顺序没有确定性，可能add1的值先赋给a，也可能desc的值先赋给a。
    最后a的值只能是add1或desc1中的一种（在一次操作中），而不是两者都操作过后的结果。

    1. load a
    2. load 1
    3. +
    4. 赋值给a
    """
    a += 1


def desc1(a):
    """
    1. load a
    2. load 1
    3. -
    4. 赋值给a
    """
    a -= 1


thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()

# 等有join的线程都退出后，主线程才退出
thread1.join()
thread2.join()
print(total)


if __name__ == "__main__":
    pass
