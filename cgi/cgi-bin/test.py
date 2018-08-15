#!/usr/bin/python
# -*- coding: UTF-8 -*-
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer) #以上两句解决中文乱码

print("Content-type:text/html\n\n")
print('<html>')
print('<head>')
print('<title>Hello World-我的第一个 CGI 程序！</title>')
print('</head>')
print('<body>')
print('<h2>Hello World!\n我是来自菜鸟教程的第一CGI程序</h2>' )
print('</body>')
print('</html>')