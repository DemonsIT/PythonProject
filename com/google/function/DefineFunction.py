#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

"""
_title_ = ''
_author_ = '♞Demons♛'
_date_ = '2020-01-12'
"""

# 自定义函数
import math


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-6))


# 定义一个什么事也不做的空函数,可以用pass语句
def nop():
    pass


# 空函数用来作为占位符,不会影响代码执行

# 参数类型检查
def my_abs_check(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad oper and type')
    if x >= 0:
        return x
    else:
        return -x


# print(my_abs_check('r'))

# 一个函数返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# 其实返回的是一个tuple
print(move(1, 3, 1))
