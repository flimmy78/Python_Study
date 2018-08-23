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
srcinipath = '/JKJN/sys.ini'
destinipath = '/JKJN/sysold.ini'
conf.read(srcinipath,encoding="utf-8")
conf.write(open(destinipath,'w+'))

form = cgi.FieldStorage()
#[FS_EPS]
#IFSF_Node = form['IFSF_Node'].value
#FS_IP = form['FS_IP'].value
#print(header+debug%(items))
print(header)

def updateItemfromhtml(section,refsection):
	if section == "FS_EPS" or section == "Board_Info" or section == "Gun_Info1":
		end=''
	else: #Gun_Info2,Gun_Info3,Gun_Info4
		end=section[-1]
	if not refsection:	
		items = conf.items(section)	
	else:
		items = conf.items(refsection)
	for item in items: 
		formitem=item[0]+end 
		if formitem in form:
			value = form[formitem].value	
			oldvalue = '-1'	
			if value:
				if conf.has_option(section,item[0]):
					oldvalue=conf.get(section,item[0])
				if value != oldvalue:
					conf.set(section,item[0],value)				
					print(debug%(section)+"-")
					print(debug%(item[0])+": befor")
					print(debug%("<font size=5 color=\"blue\">"+oldvalue+"</font> new:"))
					print(debug%("<font size=5 color=\"red\">"+value+"</font><br>"))
				else:
					print(debug%(section)+"-")
					print(debug%(item[0])+":")
					print(debug%("old value and new value are equal!<br>"))
	return
	
def updateOrDeleteGuninfo234(section):		
	if section in form:
		if section not in conf.sections():
			conf.add_section(section)
			print("Add"+debug%(section)+"SECTION!<br>")
		updateItemfromhtml(section,"Gun_Info1")				
	elif section in conf.sections():
		conf.remove_section(section)
		print(debug%(section)+"delete all!<br>")
	return
	
for section in conf.sections():
	updateItemfromhtml(section,None)			

updateOrDeleteGuninfo234("Gun_Info2")#Gun_Info2	
updateOrDeleteGuninfo234("Gun_Info3")#Gun_Info3
updateOrDeleteGuninfo234("Gun_Info4")#Gun_Info4

conf.write(open(srcinipath,'w+'))


