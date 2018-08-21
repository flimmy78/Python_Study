### 1、下载python源码
我使用的是python3.4.3
### 2、解压后建立配置脚本build.sh
```
#!/bin/sh 
rm config.site
echo ac_cv_file__dev_ptmx=yes >> config.site 
echo ac_cv_file__dev_ptc=no >> config.site 
export CONFIG_SITE=config.site
./configure CC=/opt/arm-2009q3-4.4.1/bin/arm-none-linux-gnueabi-gcc CXX=/opt/arm-2009q3-4.4.1/bin/arm-none-linux-gnueabi-g++ AR=/opt/arm-2009q3-4.4.1/bin/arm-none-linux-gnueabi-ar RANLIB=/opt/arm-2009q3-4.4.1/bin/arm-none-linux-gnueabi-ranlib READELF=/opt/arm-2009q3-4.4.1/bin/arm-none-linux-gnueabi-readelf --host=arm-none-linux --build=i686-linux --disable-ipv6
```
根据交叉编译器具体位置进行修改。
### 3、此时如直接编译会导致很多模块没有进行交叉编译，需要修改`setup.py`
```
		# If a module has already been built statically,
		# don't build it here
		#if ext.name in sys.builtin_module_names:
		#    self.extensions.remove(ext)

```
### 4、此时可以`make`生成python，生成后再`strip`一下
### 5、拷贝python可执行文件到目标arm板，以及相应的库文件和模块文件
### 6、设置`PYTHONHOME`以及`PYTHONPATH`环境变量
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






