#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

"""
_title_ = ''
_author_ = '♞Demons♛'
_date_ = '2020-01-11'
"""
# 字符串和编码

print('包含中文的str')

# 对于单个字符的编码,python提供了ord()函数获取字符的整数表示,chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
# 如果知道字符的整数编码,还可以用十六进制这么写str
print('\u4e2d\u6587')
# 由于python的字符串类型是str,在内存中以Unicode表示,一个字符对应若干个字节.
# 如果要在网络上传输,或者保存到磁盘上,就需要把str变为以字节为单位的bytes
# python对bytes类型的数据用带b前缀的单引号或者双引号表示:
x = b'ABC'
print(x)
# 要计算str包含多少个字符,可以用len()函数
print(len('ABC'))
print(len('中文'))
# len()函数计算的是str的字符数,如果换成bytes,len()函数就计算字节数
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))
# python中的占位符 %d:整数 %f:浮点数 %s:字符串 %x:十六进制整数
print('Dear %s, your age is:%d, weight is:%f' % ('Tom', 18, 100.29))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('growth rate: %d %%' % 7)
