# -*- coding: utf-8 -*-

# @file:               bisect_test.py
# @Author:             MaiXiaochai
# @Date:               2019-02-12 22:29:39
# @Last Modified by:   MaiXiaochai
# @Last Modified time: 2019-02-12 23:10:56
# @GitHub:             https://github.com/MaiXiaochai

import bisect


inter_list = []
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 6)
print(inter_list)

# 返回找到的元素的右边一个index
print(bisect.bisect(inter_list, 3))
print(inter_list)
