#!/usr/bin/python
# -*- coding: utf-8 -*-

# @File    : process_test.py
# @Time    : 2019/2/21 23:13
# @Author  : MaiXiaochai
# @Site    : https://github.com/MaiXiaochai

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

range_list = range(25, 40)


# ------------------------> 计算类操作 <-----------------------------
def fib(n):
    if n <= 2:
        return 1

    return fib(n - 1) + fib(n - 2)


def thread_fib():
    with ThreadPoolExecutor(3) as executor:
        all_task = [executor.submit(fib, num) for num in range_list]

        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("executor result: {}".format(data))

        print("Last time: {}".format(time.time() - start_time))
        """
        out:
        Last time: 42.44472026824951
        """


def process_fib():
    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(fib, num) for num in range_list]

        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("executor result: {}".format(data))

        print("Last time: {}".format(time.time() - start_time))
        """
        out:
        Last time: 26.16935896873474
        """


# -------------------------> IO；类操作 <--------------------------------
io_list = [2] * 30


def random_sleep(n):
    time.sleep(n)
    return n


def thread_io():
    with ThreadPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, num) for num in io_list]

        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("executor result: {}".format(data))

        print("Last time: {}".format(time.time() - start_time))


def process_io():
    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, num) for num in io_list]

        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("executor result: {}".format(data))

        print("Last time: {}".format(time.time() - start_time))


if __name__ == "__main__":
    # 计算操作
    # thread_fib()
    # Last time: 42.44472026824951
    # process_fib()
    # Last time: 26.16935896873474

    # IO操作
    # thread_io()
    # Last time: 20.008029222488403
    # process_io()
    # Last time: 20.382468461990356
    pass
