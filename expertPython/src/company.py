#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @date    : 2019-02-04 13:53:50
# @author  : maixiaochai
# @email   : maixiaochai@qq.com
# @Link    : https://github.com/MaiXiaochai
# @Version : 1.0


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


def main():
    company = Company(["tom", "bob", "jane"])
    for em in company:
        print(em)
    print(len(company))


if __name__ == "__main__":
    main()
