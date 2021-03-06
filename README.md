### 字符串处理参考文档
1、[python常用的十进制、16进制、字符串、字节串之间的转换（长期更新帖）](https://blog.csdn.net/crylearner/article/details/38521685)<br>
2、[Python中struct.pack()和struct.unpack()用法详细说明](http://www.php.cn/python-tutorials-356984.html)<br>
3、[字符串和编码](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000)<br>
### 正则表达式参考文档
1、[Python中正则表达式的详细教程](https://www.jb51.net/article/65286.htm)<br>
2、[Python正则表达式指南](https://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html)<br>
### 一、列表
#### 1.1 列表类型
列表值看起来像这样： ['cat', 'bat', 'rat', 'elephant']。就像字符串值用引号来标记字符串的起止一样， 列表用左方括号开始，右方括号结束，即`[]`。<br>
#### 1.2 列表下标
列表也可以包含其他列表值。这些列表的列表中的值， 可以通过多重下标来访问， 像这样：<br>	
```
>>> spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
>>> spam[0]
['cat', 'bat']
>>> spam[0][1]
'bat'
>>> spam[1][4]
50
```
#### 1.3 负数下标
虽然下标从`0`开始并向上增长，但也可以用负整数作为下标。整数值`−1`指的是列表中的最后一个下标，`−2`指的是列表中倒数第二个下标，以此类推。
#### 1.4 列表切片
在一个切片中，第一个整数是切片开始处的下标，第二个整数是切片结束处的下标。切片向上增长，直至第二个下标的值，但不包括它。切片求值为一个新的列表值。
```
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[0:4]
['cat', 'bat', 'rat', 'elephant']
>>> spam[1:3]
['bat', 'rat']
>>> spam[0:-1]
['cat', 'bat', 'rat']
```
#### 1.5 用 len()取得列表的长度
`len(listname)`函数将返回传递给它的列表中值的个数。
#### 1.6 列表连接和列表复制
`+`操作符可以连接两个列表,得到一个新列表，就像它将两个字符串合并成一个新字符串一样。`*`操作符可以用于一个列表和一个整数，实现列表的复制。
#### 1.7 用 del 语句从列表中删除值
`del`语句将删除列表中下标处的值， 表中被删除值后面的所有值，都将向前移动一个下标。
#### 1.8 列表用于循环
一个常见的 Python 技巧，是在` for `循环中使用` range(len(someList))`，迭代列表的每一个下标。
#### 1.9 in 和 not in 操作符
利用` in `和` not in `操作符，可以确定一个值否在列表中。
#### 1.10 多重赋值技巧
多重赋值技巧是一种快捷方式，让你在一行代码中，用列表中的值为`多个变量`赋值，`变量的数目`和`列表的长度`必须严格相等，否则 Python 将给出`ValueError：`错误
#### 1.11 用 index()方法在列表中查找值
列表值有一个` index()`方法，可以传入一个值，如果该值存在于列表中，就返回它的下标。如果列表中存在重复的值，就返回它`第一次`出现的下标。
#### 1.12 用 append()和 insert()方法在列表中添加值
`append()`方法将参数添加到列表`末尾`，`insert()`方法可以在列表`任意下标`处插入一个值。
#### 1.13 用 remove()方法从列表中删除值
* 给` remove() `方法传入一个值，它将从被调用的列表中删除。如果该值在列表中出现多次，只有`第一次`出现的值会被删除。
* 如果知道想要删除的值在列表中的下标，` del `语句就很好用，如果知道想要从列表中删除的值，` remove() `方法就很好用。
#### 1.14 用 sort()方法将列表中的值排序
数值的列表或字符串的列表， 能用` sort() `方法排序。也可以指定` reverse `关键字参数为` True `， 让` sort(reverse=True) `按逆序排序。
##### 注意
* 首先，` sort() `方法当场对列表排序。不要写出` spam = spam.sort() `这样的代码，试图记录返回值。
* 其次，不能对既有数字又有字符串值的列表排序，因为 Python 不知道如何比较它们。 
* 第三，` sort() `方法对字符串排序时，使用`“ASCII 字符顺序”`，而不是实际的字典顺序。这意味着大写字母排在小写字母之前。因此在排序时，小写的` a `在大写的` Z `之后。如果需要按照普通的字典顺序来排序， 就在` sort() `方法调用时，将关键字参数` key `设置为` str.lower `，如：`listName.sort(key=str.lower)`
### 二、类似列表的类型：字符串和元组
* 列表并不是唯一表示序列值的数据类型。例如， 字符串和列表实际上很相似，只要你认为字符串是单个文本字符的列表。对列表的许多操作， 也可以作用于字符串：按下标取值、 切片、 用于 for 循环、 用于 len()， 以及用于 in 和 not in 操作符。
* 但列表和字符串在一个重要的方面是不同的。列表是` “可变的” `数据类型，它的值可以添加、 删除或改变。但是， 字符串是`“不可变的”`， 它不能被更改。尝试对字符串中的一个字符重新赋值， 将导致` TypeError `错误。“改变” 一个字符串的正确方式， 是`使用切片和连接`。
* `“元组” `数据类型几乎与列表数据类型一样。首先， 元组输入时用圆括号`()`， 而不是用方括号`[]`。但元组与列表的主要区别还在于，元组像字符串一样，`是不可变的`。元组`不能让它们的值被修改、添加或删除`。
### 三、用 list()和 tuple()函数来转换类型
正如` str(42) `将返回`'42'`，即`整数 42 的字符串表示形式`， 函数` list()和 tuple() `将返回传递给它们的值的列表和元组版本。
### 四、copy 模块的 copy()和 deepcopy()函数
* 在处理列表和字典时，尽管传递引用常常是最方便的方法， 但如果函数修改了传入的列表或字典， 你可能不希望这些变动影响原来的列表或字典。要做到这一点，Python 提供了名为 copy 的模块， 其中包含` copy() 和 deepcopy()`函数。第一个函数copy.copy()， 可以用来复制列表或字典这样的可变值， 而不只是复制引用。
* 如果要复制的列表中包含了列表， 那就使用` copy.deepcopy() `函数来代替。deepcopy()函数将同时复制它们内部的列表。
### 五、字典
#### 5.1 字典数据类型
* 像列表一样，“字典”是许多值的集合。但不像列表的下标，字典的索引可以使用许多不同数据类型，不只是整数。字典的索引被称为“键”，键及其关联的值
称为`“键-值”对`。在代码中， 字典输入时带花括号{}。
* 字典仍然可以用整数值作为键，就像列表使用整数值作为下标一样，但它们不必从 0 开始，可以是任何数字。
* 不像列表， 字典中的表项是不排序的。虽然确定两个列表是否相同时，表项的顺序很重要，但在字典中，`“键-值”对`输入的顺序并不重要。
* 因为字典是不排序的，所以不能像列表那样切片。
* 用` in `关键字，可以看看输入的名字是否作为键存在于字典中，就像查看列表一样。
#### 5.2 keys()、 values()和 items()方法
* 有 3 个字典方法，它们将返回类似列表的值，分别对应于字典的键、值和键-值对：`keys()、 values()和 items()`。这些方法返回的值不是真正的列表，它们不能被修改，没有append()方法。但这些数据类型（分别是 dict_keys、 dict_values 和 dict_items）可以用于for循环。
* 如果希望通过这些方法得到一个真正的列表，就把类似列表的返回值传递给`list()`函数。`list(listName.keys())`代码行接受keys()函数返回的 dict_keys 值，并传递给list()，然后返回一个列表。
* 也可以利用多重赋值的技巧，在 for 循环中将键和值赋给不同的变量，如：
```
>>> spam = {'color': 'red', 'age': 42}
>>> for k, v in spam.items():
        print('Key: ' + k + ' Value: ' + str(v))
Key: age Value: 42
Key: color Value: red
```
* 如果想要检查一个值是否为字典中的键，就可以用关键字 in（或 not in），作用于该字典本身
#### 5.3 get()方法
字典有一个` get() `方法，它有两个参数：要取得其值的键，以及如果该键不存在时，返回的备用值。
#### 5.4 setdefault()方法
* `setdefault()`方法提供了一种方式，在一行中完成这件事。传递给该方法的第一个参数，是要检查的键。第二个参数，是如果该键不存在时要设置的值。如果该键确实存在，方法就会返回键的值。<br>
* `setdefault()`方法是一个很好的快捷方式，可以确保一个键存在。下面有一个小程序， 计算一个字符串中每个字符出现的次数。
```
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)
```
#### 5.5 漂亮打印
* 如果程序中导入` pprint `模块， 就可以使用` pprint()和 pformat() `函数，它们将“漂亮打印”一个字典的字。
* 如果希望得到漂亮打印的文本作为字符串， 而不是显示在屏幕上， 那就调用`pprint.pformat()`。下面两行代码是等价的：
```
pprint.pprint(someDictionaryValue)
print(pprint.pformat(someDictionaryValue))
```
##### 打印参考文档
1、[Python 3 print 函数用法总结](http://www.runoob.com/w3cnote/python3-print-func-b.html)<br>
2、[Python 打印和输出](https://blog.csdn.net/liang19890820/article/details/72887227)<br>
3、[python2的print和python3的print()](https://www.cnblogs.com/kaitoex/p/6085606.html)<br>
4、[python 中 print 函数用法总结](https://blog.csdn.net/xuhaikun123/article/details/54646141)<br>
### 六、字符串操作
#### 6.1 双引号
字符串可以用双引号开始和结束，就像用单引号一样。使用双引号的一个好处，就是字符串中可以使用单引号字符。
#### 6.2 转义字符
* “转义字符” 让你输入一些字符，它们用其他方式是不可能放在字符串里的。转义字符包含一个倒斜杠`（\）`， 紧跟着是想要添加到字符串中的字符。
* 转义字符`\'`和`\"`让你能在字符串中加入单引号和双引号。
#### 6.3 原始字符串
可以在字符串开始的引号之前加上` r `， 使它成为原始字符串。“原始字符串” 完全忽略所有的转义字符， 打印出字符串中所有的倒斜杠。
#### 6.4 用三重引号的多行字符串
虽然可以用`\n`转义字符将换行放入一个字符串， 但使用多行字符串通常更容易。在 Python 中，多行字符串的起止是` 3 个单引号或 3 个双引号`。“三重引号” 之间的`所有引号、 制表符或换行， 都被认为是字符串的一部分`。 
#### 6.5 字符串方法 upper()、 lower()、 isupper()和 islower()
* upper()和 lower()字符串方法返回一个`新字符串`，其中原字符串的所有字母都被相应地转换为大写或小写。字符串中非字母字符保持不变。
* 请注意，这些方法没有改变字符串本身，而是返回一个新字符串。如果你希望改变原来的字符串，就必须在该字符串上调用 upper()或lower()，然后将这个新字符串赋给保存原来字符串的变量。如：spam = spam.upper()
* 如果字符串至少有一个字母，并且所有字母都是大写或小写，isupper()和islower()方法就会相应地返回布尔值 True，否则，该方法返回 False。
#### 6.6 isX 字符串方法
除了 islower()和 isupper()， 还有几个字符串方法，它们的名字以 is 开始。
* `isalpha()`返回 True， 如果字符串`只包含字母`， 并且非空；
* `isalnum()`返回 True，如果字符串`只包含字母和数字`，并且非空；
* `isdecimal()`返回 True，如果字符串`只包含数字字符`，并且非空；
* `isspace()`返回 True，如果字符串`只包含空格、制表符和换行`，并且非空；
* `istitle()`返回 True，如果字符串`仅包含以大写字母开头、后面都是小写字母的单词`，并且非空。
#### 6.7 字符串方法 startswith()和 endswith()
`startswith()和 endswith()`方法返回 True， 如果它们所调用的字符串以该方法传入的字符串开始或结束。否则，方法返回 False。
#### 6.8 字符串方法 join()和 split()
* 如果有一个字符串列表， 需要将它们连接起来，成为一个单独的字符串， join()方法就很有用。 如：
```
>>> ', '.join(['cats', 'rats', 'bats'])
'cats, rats, bats'
>>> ' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'
>>> 'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimon'
```
* split()方法做的事情正好相反：它针对一个字符串调用， 返回一个字符串列表。如：
```
>>> 'My name is Simon'.split()
['My', 'name', 'is', 'Simon']
```
默认情况下，字符串`'My name is Simon'`按照各种空白字符分割，诸如空格、制表符或换行符。这些空白字符不包含在返回列表的字符串中，也可以向 split()方法传入一个分割字符串，指定它按照不同的字符串分割。
#### 6.9 用 rjust()、 ljust()和 center()方法对齐文本
* `rjust()和 ljust()`字符串方法返回调用它们的字符串的填充版本，通过插入空格来对齐文本。这两个方法的第一个参数是一个整数长度，用于对齐字符串，第二个可选参数将指定一个填充字符，取代空格字符，不填第二个参数即默认为填充空格。
* center()字符串方法与 ljust()与 rjust()类似， 但它让文本居中，而不是左对齐或右对齐。
#### 6.10 用 strip()、 rstrip()和 lstrip()删除空白字符
有时候你希望删除字符串左边、右边或两边的空白字符（空格、制表符和换行符）。`strip()`字符串方法将返回一个新的字符串，它的开头或末尾都没有空白字符。`lstrip()和 rstrip()`方法将相应删除左边或右边的空白字符。
#### 6.11 用 pyperclip 模块拷贝粘贴字符串
pyperclip 模块有 copy()和 paste()函数， 可以向计算机的剪贴板发送文本，或从它接收文本。

### 七、正则表达式
#### 7.1 匹配符
* `?`匹配零次或一次前面的分组。
* `*`匹配零次或多次前面的分组。
* `+`匹配一次或多次前面的分组。
* `{n}`匹配 n 次前面的分组。
* `{n,}`匹配 n 次或更多前面的分组。
* `{,m}`匹配零次到 m 次前面的分组。
* `{n,m}`匹配至少 n 次、至多 m 次前面的分组。
* `{n,m}?`或`*?`或`+?`对前面的分组进行非贪心匹配。
* `^spam`意味着字符串必须以 spam 开始。
* `spam$`意味着字符串必须以 spam 结束。
* `.`匹配所有字符，换行符除外。
* `\d、\w 和\s `分别匹配数字、单词和空格。
* `\D、\W 和\S `分别匹配出数字、单词和空格外的所有字符。
* `[abc]`匹配方括号内的任意字符（诸如 a、 b 或 c）。
* `[^abc]`匹配不在方括号内的任意字符。
#### 7.2 不区分大小写的匹配
向 re.compile()传入`re.IGNORECASE 或 re.I`，作为第二个参数。
#### 7.3 忽略正则表达式字符串中的空白符和注释
向 re.compile()传入`re.VERBOSE`， 作为第二个参数。
#### 7.4 点-星(`.*`)将匹配除换行外的所有字符
向 re.compile()传入`re.DOTALL`，作为 re.compile()的第二个参数， 可以让`.*`匹配所有字符，包括换行字符
### 八、读写文件
#### 8.1 文件与文件路径
Windows 上的倒斜杠`\`以及 OS X 和 Linux 上的正斜杠`/`，`os.path.join()`就会返回一个文件路径的字符串，包含正确的路径分隔符。在交互式环境中输入以下代码：
```
>>> import os
>>> os.path.join('usr', 'bin', 'spam')
'usr\\bin\\spam'
```
__请注意__，倒斜杠有两个，因为每个倒斜杠需要由另一个倒斜杠字符来转义。如果我在 OS X 或 Linux 上调用这个函数， 该字符串就会是`'usr/bin/spam'`。
#### 8.2 当前工作目录
利用`os.getcwd()`函数，可以取得当前工作路径的字符串，并可以利用`os.chdir()`改变它。
#### 8.3 创建新文件夹
用`os.makedirs()`可以创建新文件夹。
#### 8.4 os.path 模块
* 调用`os.path.abspath(path)`将返回参数的绝对路径的字符串。这是将相对路径转换为绝对路径的简便方法。
* 调用`os.path.isabs(path)`，如果参数是一个绝对路径，就返回 True，如果参数是一个相对路径，就返回 False。
* 调用`os.path.relpath(path, start)`将返回从 start 路径到 path 的相对路径的字符串。如果没有提供 start，就使用当前工作目录作为开始路径。
* 调用`os.path.dirname(path)`将返回一个字符串，它包含 path 参数中最后一个斜杠`之前`的所有内容(可以理解为文件路径)。
* 调用`os.path.basename(path)`将返回一个字符串，它包含 path 参数中最后一个斜杠`之后`的所有内容(可以理解为文件名)。
* 调用`os.path.split()`，如果同时需要一个路径的目录名称和基本名称， 就可以调用 os.path.split()，获得这两个字符串的元组。
* `os.path.split()`不会接受一个文件路径并返回每个文件夹的字符串的列表。如果需要这样，请使用 split()字符串方法，并根据 os.path.sep 中的字符串进行分割。
```
>>> calcFilePath = 'C:\\Windows\\System32\\calc.exe'
>>> os.path.split(calcFilePath)
('C:\\Windows\\System32', 'calc.exe')
>>> (os.path.dirname(calcFilePath), os.path.basename(calcFilePath))
('C:\\Windows\\System32', 'calc.exe')
>>> calcFilePath.split(os.path.sep)
['C:', 'Windows', 'System32', 'calc.exe']
```
* 调用`os.path.getsize(path)`将返回 path 参数中文件的字节数。
* 调用`os.listdir(path)`将返回文件名字符串的列表，包含 path 参数中的每个文件（请注意，这个函数在 os 模块中，而不是 os.path）。
##### 8.4.1 检查路径有效性
* 如果 path 参数所指的文件或文件夹存在， 调用`os.path.exists(path)`将返回 True，否则返回 False。
* 如果 path 参数存在，并且是一个文件， 调用`os.path.isfile(path)`将返回 True， 否则返回 False。
* 如果 path 参数存在， 并且是一个文件夹， 调用`os.path.isdir(path)`将返回 True，否则返回 False。
#### 8.5 用 shelve 模块保存变量
利用` shelve `模块， 你可以将 Python 程序中的变量保存到二进制的` shelf 文件`中。这样， 程序就可以从硬盘中恢复变量的数据。 shelve 模块让你在程序中添加“保存”和“打开” 功能。
```
>>> import shelve
>>> shelfFile = shelve.open('mydata')
>>> cats = ['Zophie', 'Pooka', 'Simon']
>>> shelfFile['cats'] = cats
>>> shelfFile.close()
```
读取保存的变量
```
>>> shelfFile = shelve.open('mydata')
>>> type(shelfFile)
<class 'shelve.DbfilenameShelf'>
>>> shelfFile['cats']
['Zophie', 'Pooka', 'Simon']
>>> shelfFile.close()
```







