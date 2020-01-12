#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

"""
_title_ = ''
_author_ = '♞Demons♛'
_date_ = '2020-01-12'
"""
listArray = ['Michael', 'Bob', 'Tracy']
print(listArray)
# 获取数组的长度
print(len(listArray))
# 获取数组中单个元素,下标从0开始
print(listArray[0])
print(listArray[1])
print(listArray[2])
# 获取数组最后一个元素,使用下标-1
print(listArray[-1])
# 获取数组倒数第二个元素,使用下标-2,以此类推
print(listArray[-2])
# list是一个可变的有序表,所以,可以往list中追加元素到末尾
listArray.append('Admin')
print(listArray)
# 也可以把元素插入到指定的位置,比如索引号为1的位置
listArray.insert(1, 'Jack')
print(listArray)
# 要删除list末尾的元素,用pop()方法
listArray.pop()
print(listArray)
# 要删除指定位置的元素,用pop(i)方法,其中i是索引位置
listArray.pop(1)
print(listArray)
# 要把某个元素替换成别的元素,可以直接赋值给对应的索引位置
listArray[1] = 'replace'
print(listArray)
# list里面的元素的数据类型也可以不同
multiEle = ['str', 18, 1.234, True]
print(multiEle)
# list中也可以嵌套list
multiEle[1] = [18, 'jay', False]
print(multiEle)
print('empty list size:', len([]))

# tuple:元组,有序列表,和list类似,但是tuple一旦初始化就不能修改
person = ('jack', 1, True)
print('tuple person:', person)
print('single tuple size:', len((19,)))
print('empty tuple size:', len(()))
# tuple所谓的'不变'是说,tuple的每个元素,指向永远不变
# 即指向'a',就不能改为指向'b',指向一个list,就不能改成指向其他对象,但指向的这个list本身是可变的!
