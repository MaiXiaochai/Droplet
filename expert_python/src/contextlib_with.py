#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @date    : 2019-02-06 16:21:31
# @author  : maixiaochai
# @email   : maixiaochai@qq.com
# @Link    : https://github.com/MaiXiaochai
# @Version : 1.0

import contextlib


@contextlib.contextmanager
def file_open(file_name):
    print("file open")
    # contextlib.contextmanager修饰的函数必须是一个生成器,
    # 这里yield一个空字典
    # 在之前用类实现的上下文管理器中，__enter__下的内容，放到这个函数yield之前。
    # __exit__下的内容放到yield之后
    yield {}
    print("file end")


with file_open('bobby.txt') as f:
    print("file processing")
