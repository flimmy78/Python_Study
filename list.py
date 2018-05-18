#!/usr/bin/env python
# -*- coding: utf-8 -*-
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ] 
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]
print "sum = ",sum(list2)
list1 = []          ## 空列表
list1.append('Google')   ## 使用 append() 添加元素
list1.append('Runoob')
list1.extend(list2)
print list1
del list1[len(list1)-1] #最后一个元素
del list1[-1] #倒数第一个，就是最后一个
print max(list1)
