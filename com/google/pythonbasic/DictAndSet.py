#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

"""
_title_ = ''
_author_ = '♞Demons♛'
_date_ = '2020-01-12'
"""
# python内置了字典:dict的支持,dict全称dictionary,在其他语言中也成为map,使用key-value存储,具有极快的查找速度
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print('Bob\'s scores is:', d['Bob'])
# 可以通过in判断key是否存在
print('Jack' in d)
# 也可以通过dict提供的get()方法,如果key不存在,可以返回None,或者自己指定的value
print(d.get('Thoms'))
# 返回None时,python的交互环境不显示结果
print(d.get('Thomas', -1))
# 删除key,使用pop(key),对应的value也会从dict中删除
d.pop('Bob')
print(d)
# Notice:dict内部存放的顺序和key放入的顺序是没有关系的
# 和list比较，dict有以下几个特点：
#
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
#
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。
# dict的key必须是不可变对象,通过key计算位置的算法称为哈希算法(Hash)
# python中,字符串和整数都是不可变的,因此,可作为key,而list是可变的,就不能作为key

# set和dict类似,也是一组key的集合,但不存储value,由于key不能重复,所以,在set中,没有重复的key
s = {1, 2, 3}
print(s)
# add(key):添加元素到set中,可以重复添加,但不会有效果
s.add(3)
# remove(key):删除元素
s.remove(2)
# set可以看成数字意义上的无序和无重复元素的集合,因此,两个set可以做数学意义上的交集,并集等操作
s1 = {1, 5, 6}
s2 = {2, 5, 8}
print(s1 | s2)
print(s1 & s2)
