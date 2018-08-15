#!/usr/bin/env python
#!/usr/bin/python 
# -*- coding: UTF-8 -*-

import configparser as ConfigParser
import cgi
import cgitb
cgitb.enable(format='text')
import sys
#import traceback
#print("Content-Type: text/plain")
#print()

class myconf(ConfigParser.ConfigParser):
    def __init__(self,defaults=None):
        ConfigParser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr

header = 'Content-Type: text/html\n\n'
debug = '''
<HTML><HEAD><TITLE>
Debug</TITLE></HEAD>
<BODY> %s<br>
</BODY></HTML>
'''
conf=myconf()
srcinipath = 'E:\杨朝旭\study\Python\cgi\sys.ini'
destinipath = 'E:/杨朝旭/study/Python/cgi/sys_myconf.ini'
conf.read(srcinipath,encoding="utf-8")

#开始处理表单数据
form = cgi.FieldStorage()
#[FS_EPS]
#IFSF_Node = form['IFSF_Node'].value
#FS_IP = form['FS_IP'].value
#print(header+debug%(items))
#print(header)
for section in conf.sections(): 			
	items = conf.items(section)		
	if section == "FS_EPS" or section == "Board_Info" or section == "Gun_Info1": #这些section中的从form表单传过来的name不需要更改
		end=''
	else: #处理Gun_Info2,Gun_Info3,Gun_Info4
		end=section[-1]#得到数字2,3,4
	for item in items: 
		formitem=item[0]+end #得到form中的name
		if formitem in form:
			value = form[formitem].value		
			if value:
				conf.set(section,item[0],value)
				print(debug%("over2"))
conf.write(open(destinipath,'w+'))#写入ini文件


