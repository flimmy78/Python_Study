### 1、下载python源码
我使用的是python3.4.3
### 2、解压后建立配置脚本build.sh
```
#!/bin/sh 
rm config.site
echo ac_cv_file__dev_ptmx=yes >> config.site 
echo ac_cv_file__dev_ptc=yes >> config.site 
export CONFIG_SITE=config.site
./configure CC=/opt/arm-2009q3-4.4.1/bin/arm-none-linux-gnueabi-gcc CXX=/opt/arm-2009q3-4.4.1/bin/arm-none-linux-gnueabi-g++ AR=/opt/arm-2009q3-4.4.1/bin/arm-none-linux-gnueabi-ar RANLIB=/opt/arm-2009q3-4.4.1/bin/arm-none-linux-gnueabi-ranlib READELF=/opt/arm-2009q3-4.4.1/bin/arm-none-linux-gnueabi-readelf --host=arm-none-linux --disable-ipv6 --build=i686-linux-gnu --prefix=/opt/python/Python-3.4.3/build --silent --target=arm-none-linux-gnueabi --enable-shared
```
根据交叉编译器具体位置进行修改。
### 3、此时如直接编译会导致很多模块没有进行交叉编译，需要修改`setup.py`
```
		# If a module has already been built statically,
		# don't build it here
		#if ext.name in sys.builtin_module_names:
		#    self.extensions.remove(ext)

```
#### 3.1修改`Modules/Setup`文件，主要打开`zlib模块`和`readline模块`	
### 4、此时可以`make&make install`
### 5、拷贝`build`文件夹下面的`bin`,`lib`,`include`三个文件夹到目标arm板下的`/usr`文件夹下
### 6、若路径完全正确，则可以跳过这一步，(设置`PYTHONHOME`以及`PYTHONPATH`环境变量)
参考：
```
export PYTHONHOME=/usr/lib
export PYTHONPATH=$PYTHONHOME/python3.4:$PYTHONHOME/python3.4/lib.linux-arm-3.4
```
`python3.4`下面放的各种`.py`结尾的模块文件，`lib.linux-arm-3.4`下面放的各种`.so`结尾的动态库文件
### 7、设置好后，就可以测试python是否能够正常工作。
### 8、移植`readline`模块
#### 8.1 下载`readline`模块源码，进行交叉编译
[下载地址](https://ftp.gnu.org/gnu/readline/)<br>
再修改`build.sh`文件`，在最后几行位置处找到`./configure`，然后参考如下修改
```
./configure CPPFLAGS='-DNEED_EXTERN_PC -fPIC' CC=/opt/arm-2009q3-4.4.1/bin/arm-none-linux-gnueabi-gcc RANLIB=/opt/arm-2009q3-4.4.1/bin/    arm-none-linux-gnueabi-ranlib AR=/opt/arm-2009q3-4.4.1/bin/arm-none-linux-gnueabi-ar --host=arm
```
#### 8.2 执行`sh built.sh`，在`readline-lib/shlib`下生成`libhistory.so.6`和`libreadline.so.6`，后者就是我们需要的
再做一个符号链接：`ln -s libreadline.so.6 libreadline.so`
#### 8.3 下载`termcap`源码，再进行交叉编译
[下载地址](https://ftp.gnu.org/gnu/termcap/)<br>
`./configure`后直接修改修改`Makefile`就行了，so easy。
#### 8.4、修改Setup文件`vi Modules/Setup`
找到`#readline readline.c -lreadline -ltermcap`修改为：`readline readline.c -L/opt/python/ycxadd/readline-6.2.4.1/rl/readline-lib/shlib -lreadline -L/opt/python/ycxadd/termcap-1.3.1 -ltermcap`
#### 8.5重新make后就新生成的`python`文件考到目标板，并将`libreadline.so.6`也拷贝到目标板，并做相应的符号链接。

## Python For ARM 裁剪
可以不将以下文件拷贝到目标板，主要是几个大文件夹
```
__pycache__  doctest.py   idlelib      sqlite3      turtle.py    wsgiref
asyncio      ensurepip    lib2to3      test         turtledemo   xml
curses       http         pydoc_data   tkinter      unittest     xmlrpc
```
最后整个arm上python占用空间只有20多兆。

## ARM安装第三方包
1、首先下载源码包，[地址1](https://pypi.org/simple/macholib/)，[地址2](https://pypi.org/)；<br>
2、解压后执行`python setup.py install`；<br>
3、若提示需要其他依赖包，重复步骤1和步骤2，直到成功。<br>

## ARM安装PyInstaller
##### 1、首先`Building the Bootloader`，[参考](https://pyinstaller.readthedocs.io/en/v3.3.1/bootloader-building.html)；<br>
* 将linux机器上的`gcc`，`strip`等命令修改为交叉编译工具所使用的；<br>
* 修改`wscript`文件，屏蔽`#ctx.env.append_value('CFLAGS', '-m32')`和`#ctx.env.append_value('LINKFLAGS', '-m32')`，有两处；
* 执行`python ./waf all -v`，参数`-v`显示详细信息，可以去掉，生成`run`和`run_d`；
##### 2、拷贝整个文件夹到ARM板，再在ARM板上按照安装第三方包一样安装`PyInstaller`
* 修改`setup.py`，主要查看相关路径，需要拷贝BootLoader`run`文件到指定目录，参考：
```
exe = os.path.join(HOMEPATH, 'PyInstaller', 'bootloader', PLATFORM, exe)
print("============="+HOMEPATH+PLATFORM)
print(exe)
```
##### 3、拷贝完成后，再次安装，期间可能根据具体情况，需要安装好几个第三方包




