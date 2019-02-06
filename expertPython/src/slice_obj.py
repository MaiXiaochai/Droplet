#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @date    : 2019-02-06 22:44:40
# @author  : maixiaochai
# @email   : maixiaochai@qq.com
# @Link    : https://github.com/MaiXiaochai
# @Version : 1.0


class Group:
    # 支持切片操作
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self, item):
        # Group中的切片参数会传到__getitem__中
        # return self.staffs[item]

        # 改造：回一个Group，也就是可切片对象，然后继续切片操作
        # 获取当前self对象的class，其实是Group，不推荐硬编码
        cls = type(self)
        if isinstance(item, slice):
            return cls(self.group_name, self.company_name, self.staffs[item])

        elif isinstance(item, int):
            # 注意这里的[self.staffs[item]]才是list
            return cls(self.group_name, self.company_name, [self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        # 迭代器在以后章节会重点说明
        return iter(self.staffs)

    def __contains__(self, item):
        return item in self.staffs


staffs = ['bobby1', 'imooc', 'bobby2', 'bobby3']
group = Group('imooc', 'user', staffs)
# print(group[:2])
# reversed(group)
# print(group.staffs)
