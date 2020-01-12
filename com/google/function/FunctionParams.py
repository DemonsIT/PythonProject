#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

"""
_title_ = ''
_author_ = '♞Demons♛'
_date_ = '2020-01-12'
"""
def power(x):
    return x * x
print(power(3))
# 求x的n次幂
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * n
    return s
print(pow(2, 4))
# 函数可以提供默认值,这样调用函数时不用重复传入

# *args是可变参数，args接收的是一个tuple；
#
# **kw是关键字参数，kw接收的是一个dict。

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(5))
