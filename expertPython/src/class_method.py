#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @date    : 2019-02-05 20:34:38
# @author  : maixiaochai
# @email   : maixiaochai@qq.com
# @Link    : https://github.com/MaiXiaochai
# @Version : 1.0


class Date:
    # 构造函数
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def vaild_year(date_str):
        year = int(date_str.split('-')[0])
        if year < 2019:
            return False

        return True

    @staticmethod
    def parse_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))

    @classmethod
    def parse_string_cls(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return "{}/{}/{}".format(self.year, self.month, self.day)


if __name__ == "__main__":
    # staticmethod
    date_str = "2019-2-5"
    new_day = Date.parse_string(date_str)
    print(new_day)

    # classmethod
    new_day = Date.parse_string_cls(date_str)
    print(new_day)

    # vaild_year
    print(Date.vaild_year(date_str))
