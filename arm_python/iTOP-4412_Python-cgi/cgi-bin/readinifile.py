#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>中石油配置文件修改</title>
    <style>
        #b{
            width: 30%%;
			float:left;
			line-height:25px;
			padding:5px;
        }
		#c{			
            width: 35%%;	
			//text-align:right;	
			//margin-right:5px;			
        }
		#d{			
            width: 25%%;	
			//text-align:right;			
        }
		#e{			
            width: 30%%;	
			//text-align:right;			
        }
		/*
		#b,#c,#d{
			display: inline-block;
		}
		*/
		#footer {
			width: 79%%;
			height:100px;   /* footer的高度一定要是固定值*/ 
			text-align:right;	
			position:relative;
			bottom:0;				
		}
		
		#button_read{
			margin:10px;
		}
		#button_submit{
			margin:0px;			
		}
		#b,#c,#d,#e,#footer,#button_read,#button_submit{
			display: inline-block;
		}
    </style>
</head>
<body onload="checkboxOnclick()">
	<!--script type="text/javascript" src="jquery.js"></script-->  
    <script type="text/javascript"> 
	function myFunction(){
	   alert(document.getElementById("IFSF_Node").value);
	}
	function checkboxOnclick(){	/*检查是否选中，若没有选中，则不显示相关信息*/	
		if(document.getElementById("Gun_Info2").checked==true){
			document.getElementById("Gun_Info2_display").style.display = "block";			
		}else{
			document.getElementById("Gun_Info2_display").style.display = "none";
		}	
	
		if(document.getElementById("Gun_Info3").checked==true){
			document.getElementById("Gun_Info3_display").style.display = "block";			
		}else{
			document.getElementById("Gun_Info3_display").style.display = "none";			
		}
	
		if(document.getElementById("Gun_Info4").checked==true){
			document.getElementById("Gun_Info4_display").style.display = "block";			
		}else{
			document.getElementById("Gun_Info4_display").style.display = "none";			
		}
	}
	function checkForm(){/*submit时被调用，没选中的CheckBox则让其失效*/
		if(document.getElementById("Gun_Info2").checked==true){			
			document.getElementById("Gun_Info2").disabled=false;
			document.getElementById("Gun_num2").disabled=false;
			document.getElementById("My_Node2").disabled=false;
			document.getElementById("Pri_Ver2").disabled=false;
			document.getElementById("price2").disabled=false;
			document.getElementById("oilcode2").disabled=false;
			document.getElementById("Uart_NO2").disabled=false;
			document.getElementById("Uart_Speed2").disabled=false;
			document.getElementById("Uart_Data_Bits2").disabled=false;
			document.getElementById("Uart_Stop_Bits2").disabled=false;
			document.getElementById("Uart_Parity2").disabled=false;			
		}else{			
			document.getElementById("Gun_Info2").disabled=true;
			document.getElementById("Gun_num2").disabled=true;
			document.getElementById("My_Node2").disabled=true;
			document.getElementById("Pri_Ver2").disabled=true;
			document.getElementById("price2").disabled=true;
			document.getElementById("oilcode2").disabled=true;
			document.getElementById("Uart_NO2").disabled=true;
			document.getElementById("Uart_Speed2").disabled=true;
			document.getElementById("Uart_Data_Bits2").disabled=true;
			document.getElementById("Uart_Stop_Bits2").disabled=true;
			document.getElementById("Uart_Parity2").disabled=true;	
		}	
	
		if(document.getElementById("Gun_Info3").checked==true){			
			document.getElementById("Gun_Info3").disabled=false;
			document.getElementById("Gun_num3").disabled=false;
			document.getElementById("My_Node3").disabled=false;
			document.getElementById("Pri_Ver3").disabled=false;
			document.getElementById("price3").disabled=false;
			document.getElementById("oilcode3").disabled=false;
			document.getElementById("Uart_NO3").disabled=false;
			document.getElementById("Uart_Speed3").disabled=false;
			document.getElementById("Uart_Data_Bits3").disabled=false;
			document.getElementById("Uart_Stop_Bits3").disabled=false;
			document.getElementById("Uart_Parity3").disabled=false;	
		}else{			
			document.getElementById("Gun_Info3").disabled=true;
			document.getElementById("Gun_num3").disabled=true;
			document.getElementById("My_Node3").disabled=true;
			document.getElementById("Pri_Ver3").disabled=true;
			document.getElementById("price3").disabled=true;
			document.getElementById("oilcode3").disabled=true;
			document.getElementById("Uart_NO3").disabled=true;
			document.getElementById("Uart_Speed3").disabled=true;
			document.getElementById("Uart_Data_Bits3").disabled=true;
			document.getElementById("Uart_Stop_Bits3").disabled=true;
			document.getElementById("Uart_Parity3").disabled=true;	
		}
	
		if(document.getElementById("Gun_Info4").checked==true){			
			document.getElementById("Gun_Info4").disabled=false;
			document.getElementById("Gun_num4").disabled=false;
			document.getElementById("My_Node4").disabled=false;
			document.getElementById("Pri_Ver4").disabled=false;
			document.getElementById("price4").disabled=false;
			document.getElementById("oilcode4").disabled=false;
			document.getElementById("Uart_NO4").disabled=false;
			document.getElementById("Uart_Speed4").disabled=false;
			document.getElementById("Uart_Data_Bits4").disabled=false;
			document.getElementById("Uart_Stop_Bits4").disabled=false;
			document.getElementById("Uart_Parity4").disabled=false;	
		}else{			
			document.getElementById("Gun_Info4").disabled=true;
			document.getElementById("Gun_num4").disabled=true;
			document.getElementById("My_Node4").disabled=true;
			document.getElementById("Pri_Ver4").disabled=true;
			document.getElementById("price4").disabled=true;
			document.getElementById("oilcode4").disabled=true;
			document.getElementById("Uart_NO4").disabled=true;
			document.getElementById("Uart_Speed4").disabled=true;
			document.getElementById("Uart_Data_Bits4").disabled=true;
			document.getElementById("Uart_Stop_Bits4").disabled=true;
			document.getElementById("Uart_Parity4").disabled=true;	
		}
	}
	</script>
	<noscript>抱歉，你的浏览器不支持 JavaScript!</noscript>
	<form action="/cgi-bin/inifile.py" onsubmit="checkForm()" method="post">			
			<div id="b">	
				<b>[FS_EPS]设置:</b><br>	
				<div id="e">FS 节点:</div><input type="text" name="IFSF_Node" class="a"  value="%s"><br>				
				<div id="e">FS IP:</div><input type="text" name="FS_IP" class="a"  value="%s"><br>	
				<div id="e">FS TCP端口号:</div><input type="text" name="FS_Port" class="a"  value="%s"><br>				
				<div id="e">FS UDP端口号:</div><input type="text" name="FS_Udp_Port" class="a"  value="%s"><br>								
				<div id="e">EPS IP:</div><input type="text" name="EPS_IP" class="a"  value="%s"><br>
				<div id="e">EPS 端口号:</div><input type="text" name="EPS_Port" class="a"  value="%s"><br>				
				<div id="e">FS 心跳间隔:</div><input type="text" name="Time_Out" class="a"  value="%s"><br>
				<div id="e">FS 重连间隔:</div><input type="text" name="Time_Reconnect" class="a"  value="%s"><br>				
				<div id="e">OPT超时时间:</div><input type="text" name="OPT_IS_Online" class="a"  value="%s"><br>				
			</div>		
			<div id="b">
				<b>[Board_Info]设置:</b><br>
				<div id="c">本机IP:</div><input type="text" name="My_IP" class="a" id="" value="%s"><br>
				<div id="c">本机TCP服务端口 :</div><input type="text" name="My_FS_Port" class="a"  value="%s"><br>
				<div id="c">本机EPS服务端口:</div><input type="text" name="My_EPS_Port" class="a" id="" value="%s"><br>		
				<div id="c">本机掩码:</div><input type="text" name="My_Mask" class="a"  value="%s"><br>
				<div id="c">本机网关:</div><input type="text" name="My_Gateway" class="a"  value="%s"><br>				
				<div id="c">本机广播地址:</div><input type="text" name="My_Broadcast_IP" class="a"  value="%s"><br>
				<div id="c">本机广播端口:</div><input type="text" name="My_Broadcast_Port" class="a"  value="%s"><br>				
				<div id="c">心跳灯使能:</div><input type="text" name="Led_ON" class="a"  value="%s"><br>				
			</div>
			<div id="b">
				<b>[Gun_Info1]设置:</b><br>
				<div id="d">枪号:</div><input type="text" name="Gun_num" class="a" id="" value="%s"><br>
				<div id="d">节点号:</div><input type="text" name="My_Node" class="a" id="" value="%s"><br>		
				<div id="d">单价版本号:</div><input type="text" name="Pri_Ver" class="a"  value="%s"><br>
				<div id="d">单价:</div><input type="text" name="price" class="a"  value="%s"><br>								
				<div id="d">油品代码:</div><input type="text" name="oilcode" class="a"  value="%s"><br>
				<div id="d">串口号:</div><input type="text" name="Uart_NO" class="a"  value="%s"><br>								
				<div id="d">波特率:</div><input type="text" name="Uart_Speed" class="a"  value="%s"><br>
				<div id="d">数据位:</div><input type="text" name="Uart_Data_Bits" class="a"  value="%s"><br>
				<div id="d">停止位:</div><input type="text" name="Uart_Stop_Bits" class="a"  value="%s"><br>				
				<div id="d">校验位:</div><input type="text" name="Uart_Parity" class="a"  value="%s"><br><br>
			</div>	
			
		
			<div id="b">
			<b><input type="checkbox" name="Gun_Info2" value="[Gun_Info2]" id="Gun_Info2" onclick="checkboxOnclick()" %s/>[Gun_Info2]设置:</b><br>
				<label id="Gun_Info2_display" style="display:block;">
					<div id="c">枪号:</div><input type="text" name="Gun_num2" class="a" id="Gun_num2" value="%s"><br>
					<div id="c">节点号:</div><input type="text" name="My_Node2" class="a" id="My_Node2" value="%s"><br>		
					<div id="c">单价版本号:</div><input type="text" name="Pri_Ver2" class="a" id="Pri_Ver2"  value="%s"><br>
					<div id="c">单价:</div><input type="text" name="price2" class="a" id="price2"  value="%s"><br>				
					<div id="c">油品代码:</div><input type="text" name="oilcode2" class="a" id="oilcode2" value="%s"><br>
					<div id="c">串口号:</div><input type="text" name="Uart_NO2" class="a" id="Uart_NO2" value="%s"><br>									
					<div id="c">波特率:</div><input type="text" name="Uart_Speed2" class="a" id="Uart_Speed2" value="%s"><br>
					<div id="c">数据位:</div><input type="text" name="Uart_Data_Bits2" class="a" id="Uart_Data_Bits2" value="%s"><br>
					<div id="c">停止位:</div><input type="text" name="Uart_Stop_Bits2" class="a" id="Uart_Stop_Bits2" value="%s"><br>				
					<div id="c">校验位:</div><input type="text" name="Uart_Parity2" class="a" id="Uart_Parity2" value="%s"><br><br>
				</label>
			</div>
		
			<div id="b">
			<b><input type="checkbox" name="Gun_Info3" value="[Gun_Info3]" id="Gun_Info3" onclick="checkboxOnclick()" %s/>[Gun_Info3]设置:</b><br>
				<label id="Gun_Info3_display" style="display:block;">
					<div id="c">枪号:</div><input type="text" name="Gun_num3" class="a" id="Gun_num3" value="%s"><br>
					<div id="c">节点号:</div><input type="text" name="My_Node3" class="a" id="My_Node3" value="%s"><br>		
					<div id="c">单价版本号:</div><input type="text" name="Pri_Ver3" class="a" id="Pri_Ver3" value="%s"><br>
					<div id="c">单价:</div><input type="text" name="price3" class="a" id="price3" value="%s"><br>				
					<div id="c">油品代码:</div><input type="text" name="oilcode3" class="a" id="oilcode3"  value="%s"><br>
					<div id="c">串口号:</div><input type="text" name="Uart_NO3" class="a" id="Uart_NO3" value="%s"><br>									
					<div id="c">波特率:</div><input type="text" name="Uart_Speed3" class="a" id="Uart_Speed3" value="%s"><br>
					<div id="c">数据位:</div><input type="text" name="Uart_Data_Bits3" class="a" id="Uart_Data_Bits3" value="%s"><br>
					<div id="c">停止位:</div><input type="text" name="Uart_Stop_Bits3" class="a" id="Uart_Stop_Bits3" value="%s"><br>				
					<div id="c">校验位:</div><input type="text" name="Uart_Parity3" class="a" id="Uart_Parity3" value="%s"><br><br>
				</label>
			</div>
		
			<div id="b">
			<b><input type="checkbox" name="Gun_Info4" value="[Gun_Info4]" id="Gun_Info4" onclick="checkboxOnclick()" %s/>[Gun_Info4]设置:</b><br>
				<label id="Gun_Info4_display" style="display:block;">
					<div id="d">枪号:</div><input type="text" name="Gun_num4" class="a" id="Gun_num4" value="%s"><br>
					<div id="d">节点号:</div><input type="text" name="My_Node4" class="a" id="My_Node4" value="%s"><br>		
					<div id="d">单价版本号:</div><input type="text" name="Pri_Ver4" class="a" id="Pri_Ver4" value="%s"><br>
					<div id="d">单价:</div><input type="text" name="price4" class="a" id="price4" value="%s"><br>				
					<div id="d">油品代码:</div><input type="text" name="oilcode4" class="a" id="oilcode4" value="%s"><br>
					<div id="d">串口号:</div><input type="text" name="Uart_NO4" class="a" id="Uart_NO4" value="%s"><br>									
					<div id="d">波特率:</div><input type="text" name="Uart_Speed4" class="a" id="Uart_Speed4" value="%s"><br>
					<div id="d">数据位:</div><input type="text" name="Uart_Data_Bits4" class="a" id="Uart_Data_Bits4" value="%s"><br>
					<div id="d">停止位:</div><input type="text" name="Uart_Stop_Bits4" class="a" id="Uart_Stop_Bits4" value="%s"><br>				
					<div id="d">校验位:</div><input type="text" name="Uart_Parity4" class="a" id="Uart_Parity4" value="%s"><br><br>
				</label>
			</div>		
		<div id="footer">
			<!--button type="button" onclick="myFunction()">读取</button--> 
			<div id="button_read">
				<button type="button" style="background:#1E90FF;font-size:16px" onclick="window.location.href='./readinifile.py'">读取</button>											
			</div>
			<div id="button_submit">
				<input type="submit" style="background:#1E90FF;font-size:16px" value="提交" /> 
			</div>
		</div>		
	</form>   
</body>
</html>
'''

conf=myconf()
srcinipath = '/JKJN/sys.ini'
destinipath = '/JKJN/sysold.ini'
conf.read(srcinipath,encoding="utf-8")	

def readConf(section,key):
	try:
		return conf.get(section,key)
	except:
		return ''
print('Content-Type:text/html\n\n')
print(readinihtml%(
	#FS_EPS
	readConf('FS_EPS','IFSF_Node'),
	readConf('FS_EPS','FS_IP'),
	readConf('FS_EPS','FS_Port'),
	readConf('FS_EPS','FS_Udp_Port'),
	readConf('FS_EPS','EPS_IP'),
	readConf('FS_EPS','EPS_Port'),
	readConf('FS_EPS','Time_Out'),
	readConf('FS_EPS','Time_Reconnect'),
	readConf('FS_EPS','OPT_IS_Online'),
	
	#Board_Info
	readConf('Board_Info','My_IP'),
	readConf('FS_EPS','My_FS_Port'),
	readConf('Board_Info','My_EPS_Port'),
	readConf('Board_Info','My_Mask'),
	readConf('Board_Info','My_Gateway'),
	readConf('Board_Info','My_Broadcast_IP'),
	readConf('Board_Info','My_Broadcast_Port'),
	readConf('Board_Info','Led_ON'),	

	#Gun_Info1
	readConf('Gun_Info1','Gun_num'),
	readConf('Gun_Info1','My_Node'),
	readConf('Gun_Info1','Pri_Ver'),
	readConf('Gun_Info1','price'),
	readConf('Gun_Info1','oilcode'),
	readConf('Gun_Info1','Uart_NO'),
	readConf('Gun_Info1','Uart_Speed'),
	readConf('Gun_Info1','Uart_Data_Bits'),
	readConf('Gun_Info1','Uart_Stop_Bits'),
	readConf('Gun_Info1','Uart_Parity'),	
	
	#Gun_Info2
	"checked" if readConf('Gun_Info2','Gun_num') else '',#python三目运算符，判断是否存在Gun_Info2
	readConf('Gun_Info2','Gun_num'),
	readConf('Gun_Info2','My_Node'),
	readConf('Gun_Info2','Pri_Ver'),
	readConf('Gun_Info2','price'),
	readConf('Gun_Info2','oilcode'),
	readConf('Gun_Info2','Uart_NO'),
	readConf('Gun_Info2','Uart_Speed'),
	readConf('Gun_Info2','Uart_Data_Bits'),
	readConf('Gun_Info2','Uart_Stop_Bits'),
	readConf('Gun_Info2','Uart_Parity'),
	
	#Gun_Info3
	"checked" if readConf('Gun_Info3','Gun_num') else '',#python三目运算符，判断是否存在Gun_Info3
	readConf('Gun_Info3','Gun_num'),
	readConf('Gun_Info3','My_Node'),
	readConf('Gun_Info3','Pri_Ver'),
	readConf('Gun_Info3','price'),
	readConf('Gun_Info3','oilcode'),
	readConf('Gun_Info3','Uart_NO'),
	readConf('Gun_Info3','Uart_Speed'),
	readConf('Gun_Info3','Uart_Data_Bits'),
	readConf('Gun_Info3','Uart_Stop_Bits'),
	readConf('Gun_Info3','Uart_Parity'),
	
	#Gun_Info4
	"checked" if readConf('Gun_Info4','Gun_num') else '',#python三目运算符，判断是否存在Gun_Info4
	readConf('Gun_Info4','Gun_num'),
	readConf('Gun_Info4','My_Node'),
	readConf('Gun_Info4','Pri_Ver'),
	readConf('Gun_Info4','price'),
	readConf('Gun_Info4','oilcode'),
	readConf('Gun_Info4','Uart_NO'),
	readConf('Gun_Info4','Uart_Speed'),
	readConf('Gun_Info4','Uart_Data_Bits'),
	readConf('Gun_Info4','Uart_Stop_Bits'),
	readConf('Gun_Info4','Uart_Parity')
	))


