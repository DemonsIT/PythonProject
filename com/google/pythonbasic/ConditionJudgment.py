#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

"""
_title_ = ''
_author_ = '♞Demons♛'
_date_ = '2020-01-12'
"""
# if-else使用时注意必须写冒号:
age = 2
if age >= 18:
    print('your age is:', age)
    print('adult')
# if语句执行的特点:从上往下判断,如果在某个判断上成立,执行并忽略剩下的elif和else
elif age < 20:
    print('age is 20.')
else:
    print('your age is:', age)
    print('teenager')
# x是非零数值,非空字符串,非空list等,就判断为true,否则为false
x = 's'
if x:
    print('test if-else simple write')
#
birth = input('birth:')
birth2 = int(birth)
if birth2 < 2000:
    print('00前')
else:
    print('00后')
