#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

"""
_title_ = ''
_author_ = '♞Demons♛'
_date_ = '2020-01-10'
"""
from xml.etree.ElementTree import PI

# python中的转义符
print('I\'m ok')
# \n 换行符
print('I\'m learning\nPython.')
# 转义 + 换行
print('\\\n\\')
# 如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义
print('\\\t\\')
print(r'\\\t\\')
# 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
print('''line1
line2
line3''')
# 布尔值注意区分大小写
print(True)
print(False)
print(False and True)
# and==&&(与) or==||(或) not==!(单目,非)
print(True and False)
print(True and True)
print(True or False)
print(False or True)
print(False or False)
print(not True)
print(not False)
age = int(input('please input your age:'))
if age > 18:
    print('成年人')
else:
    print('未成年人')
# None == null 注意不是0,而是无意义的特殊的空值
print(None)
# 变量的命名规则:必须是大小写字母,数字和_的组合,且不能是数字开头
t_332 = 'str'
Answer = 4
# 等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
# 这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。
# 静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言,不同类型不能直接赋值
num = 'str'
print(num)
num = 666
print(num)
# 常量:不可变的变量,通常使用大写字母表示
print(PI)
NUM = 100_000
print('自定义的常量:', NUM)
# python中有两种除法
# /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
print(10 / 3)
# //，称为地板除，两个整数的除法仍然是整数
print(10 // 3)
# 整数的地板除//永远是整数，即使除不尽。要做精确的除法，使用/就可以。
# 因为//除法只取结果的整数部分，所以Python还提供一个余数运算，可以得到两个整数相除的余数
print(10 % 3)
# 无论整数做//除法还是取余数，结果永远是整数，所以，整数运算结果永远是精确的
