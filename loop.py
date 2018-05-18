#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ==========while==============
count = 0
while count < 9:
    print "count = ", count
    count += 1
print "good bye"

count = 0
while count < 5:
    print count, " is  less than 5"
    count = count + 1
else:
    print count, " is not less than 5"

i = 1
while (i < 10):
    i += 1
    if i % 2 > 0:     # 非双数时跳过输出
        continue
    print "i=", i         # 输出双数2、4、6、8、10

i = 1
while True:            # 循环条件为1必定成立
    print i         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break

# ===========for===============
for item in 'Python':
    print "当前字母：",item

test = ["test1","test2","test3"]
for test in test:
    print test

#通过序列索引迭代
fruits = ['banana', 'apple',  'mango']
print "len(fruits)=",len(fruits)
for index in range(len(fruits)):
    print '当前水果 :', fruits[index]

for num in range(10,20):  # 迭代 10 到 20 之间的数字
    for i in range(2,num): # 根据因子迭代
        if num%i == 0:      # 确定第一个因子
            j=num/i          # 计算第二个因子
            print '%d 等于 %d * %d' % (num,i,j)
            break            # 跳出当前循环
    else:                  # 循环的 else 部分
            print num, '是一个质数'
'''三个单引号
多行注释1
多行注释1
多行注释1
多行注释1
'''
"""三个双引号
多行注释1
多行注释1
多行注释1
"""
i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j) : print  "%d 是素数" %(i)
    i = i + 1
