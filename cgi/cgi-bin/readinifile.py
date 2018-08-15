import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer) #以上两句解决中文乱码

import configparser as ConfigParser
import cgi

class myconf(ConfigParser.ConfigParser):
    def __init__(self,defaults=None):
        ConfigParser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr

readinihtml='''
<html>
<head>
    <meta charset="utf-8">
    <title>中石油配置文件修改</title>
    <style>
        /*.a{
            width: 300px;
            height: 30px;
             
        }*/
        #b{
            width: 300px;
            //border: 1px solid red;
            text-align: right;        /*右对齐*/·
        }
    </style>
</head>
<body>
	<script>
	function myFunction(){
	   alert("this window.onload");
	}
	</script>
	<noscript>抱歉，你的浏览器不支持 JavaScript!</noscript>
	<form action="/cgi-bin/inifile.py" method="post">	
		<b>[FS_EPS]</b><br>	
			<div id="b">
				FS节点:<input type="text" name="IFSF_Node" class="a" id="" value="%s"><br>
				FS IP:<input type="text" name="FS_IP" class="a" id="" value="%s"><br>			
			</div>
		<b>[Board_Info]</b><br>
			<div id="b">
				本机IP:<input type="text" name="My_IP" class="a" id="" value="%s"><br>
				本机EPS服务端口:<input type="text" name="My_EPS_Port" class="a" id="" value="%s"><br>			
			</div>
		<!--button type="button" onclick="myFunction()">读取</button--> <input type="submit" value="提交" /> 
	</form>   
</body>
</html>
'''

conf=myconf()
srcinipath = 'E:\杨朝旭\study\Python\cgi\sys.ini'
destinipath = 'E:/杨朝旭/study/Python/cgi/sys_myconf.ini'
conf.read(srcinipath,encoding="utf-8")	

print(readinihtml%(
	conf.get('FS_EPS','IFSF_Node'),
	conf.get('FS_EPS','FS_IP'),
	conf.get('Board_Info','My_IP'),
	conf.get('Board_Info','My_EPS_Port')))


