#!/usr/bin/python
# -*- coding: utf-8 -*-

# @File    : concurrent_futures.py
# @Time    : 2019/2/21 21:20
# @Author  : MaiXiaochai
# @Site    : https://github.com/MaiXiaochai


import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED


def get_html(times):
    time.sleep(times)
    print("get page cost {}s, success".format(times))
    return times


def main():
    executor = ThreadPoolExecutor(max_workers=2)

    """
    # 通过submit函数提交执行的函数到线程池中
    # submit 是立即返回，非阻塞的。
    task1 = executor.submit(get_html, 3)
    task2 = executor.submit(get_html, 2)

    # >>> 这种方法比较初级，需要穷举task
    # done判定某个任务是否完成
    print("task1 status: ", task1.done())
    # cancel 取消任务,只能在submit返回的方法上操作
    # 若任务状态是在执行中活着执行完成，是cancel不了的
    # 既，在task2没有得到线程的时候(比如两个task，但max_worker=1)可以取消
    print(task2.cancel())
    print("task2 status: ", task2.done())

    # result 可以获取task的执行结果
    # 阻塞的
    print(task1.result())
    """

    # 获取已经成功的task的返回值

    urls = [3, 2, 4]

    # ----------------------------------------------------------
    # 方法一：
    # submit 非阻塞，立即返回
    all_task = [executor.submit(get_html, url) for url in urls]

    # wait 阻塞指定的task
    wait(all_task, return_when=FIRST_COMPLETED)
    print('main')
    for future in as_completed(all_task):
        data = future.result()
        print("get {} page success".format(data))

    # out:
    # get page cost 2s, success
    # get page cost 3s, success
    # get page cost 4s, success
    # main
    # get 2 page success
    # get 4 page success
    # get 3 page success

    """
    FIRST_COMPLETED
    out:
    get page cost 2s, success
    main
    get 2 page success
    get page cost 3s, success
    get 3 page success
    get page cost 4s, success
    get 4 page success
    """
    """
    # 方法二：executor.map(),与Python中的关键词map类似
    
    # map返回的顺序和urls里边的顺序是一致的
    all_task = executor.map(get_html, urls)

    for data in all_task:
        print("get {} page success".format(data))

    
    # out:
    # get page cost 2s, success
    # get page cost 3s, success
    # get 3 page success
    # get 2 page success
    # get page cost 4s, success
    # get 4 page success
    """


if __name__ == "__main__":
    main()
