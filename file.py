#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
fo = open("1.txt",'a+')
fo.write("1-nihao ==== ====\n")
fo.write("2-nihao ==== ====\n")
fo.write("3-nihao ==== ====\n")
print "filename:",fo.name
print "filemode:",fo.mode
print fo.tell()
fo.seek(0,os.SEEK_SET)
str = fo.read(10)
print "read str: ",str
fo.close()
print "fileclose:",fo.closed

print "pwd:",os.getcwd()
