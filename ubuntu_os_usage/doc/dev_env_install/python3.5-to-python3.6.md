#  Ubuntu 将 python 3.5 更新至 python 3.6

## 安装 Python 3.6  

在命令行输入 ``python3 -V``，发现是 `python3.5`. 接下来然后我们在保留 Python3.5 的前提下安装 Python3.6

```bash
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6 python3.6-dev
```

然后再次命令行输入 ``python3 -V``, 发现还是 python3.5 的. 这是因为 python3 的软连接指向没有被改变.  

## 改变 python3 的软连接指向   

1). 输入 `which python3` 查看快捷键的路径.  

```
$ which python3

/usr/bin/python3
```

2) 进到 `/usr/bin/` 目录   

```bash
sudo rm python3
sudo ln -s python3.6 python3
```

然后再次命令行输入 ``python3 -V``, 发现此时已经是 python3.6.  

## 收尾工作 

```bash
sudo apt install python3-pip
sudo apt remove --purge python3-apt
sudo python3 -m pip install --upgrade pip
```

最后, 后面可能会出现 pip unsupported local setting, 设置编码.    

```bash
export LC_ALL=C
```

## 后遗症 - issues  

1) 终端无法正常打开.  

```bash
$ gnome-terminal

Traceback (most recent call last):
File “/usr/bin/gnome-terminal”, line 9, in 
from gi.repository import GLib, Gio
File “/usr/lib/python3/dist-packages/gi/init.py”, line 42, in 
from . import _gi

ImportError: cannot import name ‘_gi’
```

解决办法:  进入路径 `/usr/lib/python3/dist-packages/gi/`:  

```bash
sudo cp _gi_cairo.cpython-35m-x86_64-linux-g cp _gi_cairo.cpython-36m-x86_64-linux-g
sudo cp _gi.cpython-35m-x86_64-linux-gnu.so _gi.cpython-36m-x86_64-linux-gnu.so
```

以上两份文件需要重命名或复制后更名,就是把 35 改成 36.  

修改完成以后,再打开终端,应该就正常了.   

2) 将 /usr/lib/python3/dist-packages/ 下所有 python3.5 的包复制为 python 3.6   

```bash
cd /usr/lib/python3/dist-packages/  
find ./ -name "*35m*"

./pcardext.cpython-35m-x86_64-linux-gnu.so
./apt_inst.cpython-35m-x86_64-linux-gnu.so
./scanext.cpython-35m-x86_64-linux-gnu.so
./_dbus_bindings.cpython-35m-x86_64-linux-gnu.so
...
./PyQt5/QtDesigner.cpython-35m-x86_64-linux-gnu.so
./PyQt5/QtTest.cpython-35m-x86_64-linux-gnu.so
./PyQt5/QtGui.cpython-35m-x86_64-linux-gnu.so
./apt_pkg.cpython-35m-x86_64-linux-gnu.so
```

```
sudo cp ./pcardext.cpython-35m-x86_64-linux-gnu.so ./pcardext.cpython-36m-x86_64-linux-gnu.so && sudo cp ./apt_inst.cpython-35m-x86_64-linux-gnu.so ./apt_inst.cpython-36m-x86_64-linux-gnu.so && sudo cp ./scanext.cpython-35m-x86_64-linux-gnu.so ./scanext.cpython-36m-x86_64-linux-gnu.so && sudo cp ./_dbus_bindings.cpython-35m-x86_64-linux-gnu.so ./_dbus_bindings.cpython-36m-x86_64-linux-gnu.so && ... && sudo cp ./PyQt5/QtDesigner.cpython-35m-x86_64-linux-gnu.so ./PyQt5/QtDesigner.cpython-36m-x86_64-linux-gnu.so && sudo cp ./PyQt5/QtTest.cpython-35m-x86_64-linux-gnu.so ./PyQt5/QtTest.cpython-36m-x86_64-linux-gnu.so && sudo cp ./PyQt5/QtGui.cpython-35m-x86_64-linux-gnu.so ./PyQt5/QtGui.cpython-36m-x86_64-linux-gnu.so && sudo cp ./apt_pkg.cpython-35m-x86_64-linux-gnu.so ./apt_pkg.cpython-36m-x86_64-linux-gnu.so
```

3) 另外一种不太有效的办法  

```bash
# 先卸载所有安装到 python3.5 的包
pip3 freeze | xargs pip3 uninstall -y
```

其中, pip3 freeze 是导出所有的依赖; xargs 连接两个命令; -y 的命令是不要询问，每次回答都是 yes.   
