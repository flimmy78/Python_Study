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
<BODY>%s
</BODY></HTML>
'''
conf=myconf()
srcinipath = 'E:\杨朝旭\study\Python\cgi\sys.ini'
destinipath = 'E:\杨朝旭\study\Python\cgi\sysold.ini'
conf.read(srcinipath,encoding="utf-8")
conf.write(open(destinipath,'w+'))#备份源文件
#开始处理表单数据
form = cgi.FieldStorage()
#[FS_EPS]
#IFSF_Node = form['IFSF_Node'].value
#FS_IP = form['FS_IP'].value
#print(header+debug%(items))
print(header)

def updateItemfromhtml(section,refsection):
	if section == "FS_EPS" or section == "Board_Info" or section == "Gun_Info1": #这些section中的从form表单传过来的name不需要更改
		end=''
	else: #处理Gun_Info2,Gun_Info3,Gun_Info4
		end=section[-1]#得到数字2,3,4
	if not refsection:	
		items = conf.items(section)	
	else:
		items = conf.items(refsection)#这里refsection=Gun_Info1,由于至少需要一条枪，所以按照第一条枪的元素去解析和添加
	for item in items: 
		formitem=item[0]+end #得到form中的name
		if formitem in form:
			value = form[formitem].value		
			if value:
				oldvalue=conf.get(section,item[0])
				if value !=oldvalue:#传过来的值与原来的值不相等，则更新
					conf.set(section,item[0],value)				
					print(debug%(section)+"下:")
					print(debug%(item[0])+"由")
					print(debug%("<font size=5 color=\"blue\">"+oldvalue+"</font> 更新为"))
					print(debug%("<font size=5 color=\"red\">"+value+"</font><br>"))
				else:
					print(debug%(section)+"下:")
					print(debug%(item[0]))
					print(debug%("旧值与新值相同，未做任何改变<br>"))
	return
	
def updateOrDeleteGuninfo234(section):		
	if section in form:#form中有相关section
		if section not in conf.sections():#但是ini文件中没有，需要添加
			conf.add_section(section)
			print("增加"+debug%(section)+"节!<br>")
			updateItemfromhtml(section,"Gun_Info1")				
	elif section in conf.sections(): #原始文件中有，但是form传过来的表单没有，需要删除
		conf.remove_section(section)
		print(debug%(section)+"下所有键值删除成功!<br>")
	return
	
for section in conf.sections(): 	#处理源配置文件中所含有的section			
	updateItemfromhtml(section,None)			

updateOrDeleteGuninfo234("Gun_Info2")#处理Gun_Info2，添加或删除	
updateOrDeleteGuninfo234("Gun_Info3")#处理Gun_Info3，添加或删除
updateOrDeleteGuninfo234("Gun_Info4")#处理Gun_Info4，添加或删除

conf.write(open(srcinipath,'w+'))#最后写入ini文件


