# -*- coding: utf-8 -*-

# @File:               python_gil.py
# @Author:             MaiXiaochai
# @Date:               2019-02-14 21:13:38
# @Last Modified by:   MaiXiaochai
# @Last Modified time: 2019-02-14 21:40:03
# @GitHub:             https://github.com/MaiXiaochai

# import dis


# def add(a):
#     a = a + 1
#     return a


# print(dis.dis(add))

"""
out:
 14           0 LOAD_FAST                0 (a)
              2 LOAD_CONST               1 (1)
              4 BINARY_ADD
              6 STORE_FAST               0 (a)

 15           8 LOAD_FAST                0 (a)
             10 RETURN_VALUE
None
"""
# ---------------------------------------------------------------------------
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

"""
222806
587642
-221358
结果不稳定，说明GIL会释放的
"""
# -------------------------------------------------------------------------
