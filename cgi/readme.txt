1、
python3启动自带http：
python -m http.server --cgi
2、
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer) #以上两句解决中文乱码