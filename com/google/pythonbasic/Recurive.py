#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

"""
_title_ = ''
_author_ = '♞Demons♛'
_date_ = '2020-01-12'
"""
print(1 + 2 + 3)
names = ['Jack', 'Tom', 'Rose']
for name in names:
    print(name)
count = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
    count = count + x
print('Result is:', count)
array = list(range(5))
print(array)
# range(x)可以生成0-(x-1)的整数序列
c = 0
for i in range(101):
    c += i
print('c final is:', c)
