#!/usr/bin/python
# -*- coding: utf-8 -*-

# @File    : thread_sync.py
# @Time    : 2019/2/16 0:27
# @Author  : MaiXiaochai
# @Site    : https://github.com/MaiXiaochai


import threading


total = 0


def add():
    global total
    for i in range(1000000):
        total += 1


def desc():
    global total
    for i in range(1000000):
        total -= 1


thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)
