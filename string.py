#!/usr/bin/env python
# -*- coding: utf-8 -*-
var = "hello"
var.capitalize()
print var
print var.capitalize() #第一个字母大写
print var.center(11,'#') #11个字符，将var居中，并用’c‘填充，默认不带此参数则用空格填充
print var.count('l',0,len(var))
print var.startswith('he')
print var.endswith('llo')

var = "hello    world"
print var
print var.expandtabs(4)
print var.find('lloo')
print "{t}{f}{g}".format(t='bright',f='Yang',g='test')

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

var = 'python'
print var.index('h')
print var.isalnum()
print var.istitle()

str = "This Is String Example...Wow!!!";
print str.istitle();
str = "This is string example....wow!!!";
print str.istitle();

print str.partition('string')
print str.split('e')

str = "   This is string example....wow!!!   ";
print str.strip()

