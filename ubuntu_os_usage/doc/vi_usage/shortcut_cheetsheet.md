# 快捷键操作  

## 编辑 

修改: 
u 是撤销你刚才做的动作;  
ctrl+r 是恢复你刚才撤销的动作;   

删除当前行后面所有的行：

,$d

2.删除第一行到当前行：


## 光标定位 

删除当前光标之后的内容: shift+d;   
shift+i 是定位到行首， shift+a 是定位到行末。 
shift+g 转到文本结尾 
9G 跳转转到第9行
:1,.d 删除所有内容(先用G转到文件尾), “.” 表示当前行, “1,.” 表示从第一行到当前行，“d” 表示删除   
3dd 删除三行   
:9,.d 或者删除第9行到第200行的内容(先用200G转到第200行) 
x 删除光标所在处字符
shift+x 删除光标所在前字符（大写 X ）
dw 删除到下一个单词开头
de 删除到本单词末尾
d+shift+e删除到本单词末尾包括标点在内
db 删除到前一个单词
dB 删除到前一个单词包括标点在内
dd 删除一整行
D 或 d$ 删除光标位置到本行结尾
d0 删除光标位置到本行开头


## 选中字符的复制,剪切, 粘贴    

进入vim中visual模式，visual模式进入，可以有三种方式：   

（1）在普通模式（normal）下，直接按键 v  就可以进入默认visual模式，可以使用v+j/k/h/l 进行文本选择     

对于选中的文本进行如下按键：

- d   ------ 剪切操作

- y   -------复制操作

- p   -------粘贴操作

- ^  --------选中当前行，光标位置到行首（或者使用键盘的HOME键）

- $  --------选中当前行，光标位置到行尾（或者使用键盘的END键）

（2） Visual Line模式  按键 V 可以进入
 
按键 V 之后，进入Visual Line模式，使用 j/k键可以选中一行或者多行

（3） Visual Block 模式，按键 Ctrl + V 可以进入   

按键 Ctrl+V 之后，进入 Visual Block 模式，使用 j/k/h/l 键可以选中一块.   

在块模式下，可以进行多列的同时修改，修改方法是：

- 首先进入块模式 Ctrl+ v

- 使用按键j/k/h/l进行选中多列

- 按键Shift + i 进行 块模式下的插入

## 列编辑模式   

### 1. 删除列

1. 光标定位到要操作的地方。

2. CTRL+v 进入“可视 块”模式，选取这一列操作多少行。

3. d 删除。
 
### 2. 插入列

插入操作的话知识稍有区别。例如我们在每一行前都插入"() "：

1. 光标定位到要操作的地方。

2. CTRL+v 进入“可视 块”模式，选取这一列操作多少行。

3. SHIFT+i(I) 输入要插入的内容。

4. ESC 按两次，会在每行的选定的区域出现插入的内容。