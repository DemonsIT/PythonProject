#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

"""
_title_ = ''
_author_ = '♞Demons♛'
_date_ = '2020-01-10'
"""
print('first python print')
# 括号中有多个参数时默认使用空格分隔
print('first', 'second', 'third')
# 支持多种类型参数的拼接
print('string', 2, 8.6)
print(2)
print(3 + 5)
print(3 + 5.80)
print('100 + 200 =', 100 + 200)
# 从控制台接收输入值,赋值给变量name
a = input()
print(a)
# 可以给出提示信息
name = input('please input your name:')
print('get input from console:', name)
# 控制台输入默认是str,可以强转成数值类型
m = int(input("please input m:"))
n = int(input('please input n:'))
print('m * n =', m * n)
