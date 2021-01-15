#!/usr/bin/python
# -*- coding: utf-8 -*-

# @File    : thread_condition.py
# @Time    : 2019/2/16 19:39
# @Author  : MaiXiaochai
# @Site    : https://github.com/MaiXiaochai
# 2021-01-14 再次发现这些代码，深有感触

import threading
from threading import Condition


class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name='小爱')
        self.cond = cond
    
    def run(self):
        with self.cond:
            self.cond.wait()
            print("{}: 在".format(self.name))
            self.cond.notify()
            self.cond.wait()
            
            print("{}: 好啊".format(self.name))
            # 通知
            self.cond.notify()
            # 等待
            self.cond.wait()
            
            print("{}: 君住长江尾".format(self.name))
            # 通知
            self.cond.notify()
            # 等待
            self.cond.wait()
            
            print("{}: 共饮长江水".format(self.name))
            # 通知
            self.cond.notify()
            # 等待
            self.cond.wait()
            
            print("{}: 此恨何时已".format(self.name))
            # 通知
            self.cond.notify()
            # 等待
            self.cond.wait()
            
            print("{}: 定不负相思意".format(self.name))
            # 通知
            self.cond.notify()
            # 等待
            self.cond.wait()


class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name='天猫精灵')
        self.cond = cond
    
    def run(self):
        with self.cond:
            print("{}: 小爱同学".format(self.name))
            # 通知
            self.cond.notify()
            # 等待
            self.cond.wait()
            
            print("{}: 我们来对古诗吧".format(self.name))
            # 通知
            self.cond.notify()
            # 等待
            self.cond.wait()
            
            print("{}: 我住长江头".format(self.name))
            # 通知
            self.cond.notify()
            # 等待
            self.cond.wait()
            
            print("{}: 日日思君不见君".format(self.name))
            # 通知
            self.cond.notify()
            # 等待
            self.cond.wait()
            
            print("{}: 此水几时休".format(self.name))
            # 通知
            self.cond.notify()
            # 等待
            self.cond.wait()
            
            print("{}: 只愿君心似我心".format(self.name))
            # 通知
            self.cond.notify()
            # 等待
            self.cond.wait()


if __name__ == '__main__':
    cond = Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)
    
    # 这里注意启动顺序，先说话的先启动，否则容易出错
    # 关键在于天猫第一次print后，是cond.notify(),xiaoai是print前在wait，
    # wait需要由notify唤醒。
    # 若启动顺序相反，则会陷入都wait的僵局
    xiaoai.start()
    tianmao.start()
    
    """
    Out:
    天猫精灵: 小爱同学
    小爱: 在
    天猫精灵: 我们来对古诗吧
    小爱: 好啊
    天猫精灵: 我住长江头
    小爱: 君住长江尾
    天猫精灵: 日日思君不见君
    小爱: 共饮长江水
    天猫精灵: 此水几时休
    小爱: 此恨何时已
    天猫精灵: 只愿君心似我心
    小爱: 定不负相思意
    """
