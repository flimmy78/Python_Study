#!/usr/bin/env python
# -*- coding: utf-8 -*-
num = -5
if num == 3:
    print "boss"
elif num == 2:
    print "user"
elif num == 1:
    print "worker"
elif num < 0:
    print "error"
else:
    print "hello"

num = 9
if num >= 0 and num <= 10:
    print "num>=0 and num<=10"

num = 10
if num <=0 or num >10:
    print "num <=0 or num >10"
else:
    print num

num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):    
    print 'hello'
else:
    print 'undefine'
# 输出结果: undefine

