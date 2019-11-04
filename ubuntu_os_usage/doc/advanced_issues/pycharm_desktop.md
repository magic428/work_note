# 安装 PyCharm 的桌面快捷方式   


这个装起来还是挺简单的,一般装了ubuntu 之后,系统自己装了有python ,所以我们直接装上一个pycharm 就能方便的进行操作啦.

直接去官网下载community   社区版(小白用这个就够了)
下载完成后,会在下载(英文的话是在dowload 下面)目录里有个tar.gz文件,直接提取到原路径下.
双击打开,进入到bin 目录下,找到pycharm.sh 文件,开启终端,输入sh ./pycharm.sh,执行,就能运行pycharm 了
到第三步,pycharm 就已经能够正常的使用了,但是有点点不方便的是,总不能每次到bin目录下，然后写代码执行吧（当然，喜欢命令行操作的忽略）,所以我们现在在桌面上创建一个pycharm　的快捷方式，其实.sh　文件就相当于windows　下的.exe文件.但是可不要认为，双击.sh 文件就可以运行啦．还是需要改点东西的．．．
首先，输入：

```
sudo  gedit  /usr/share/applications/Pycharm.desktop  
```

将里面的内容替换成：其中

Exec=sh /home/magic/opt/pycharm-community-2018.2.4/bin/pycharm.sh　　　改成自己的路径下的.sh　　（相当于.exe文件）　
Icon=/home/magic/opt/pycharm-community-2018.2.4/bin/pycharm.png　　　同上方一样，改成自己路径下的.png　（桌面图标）

```conf
[Desktop Entry]
Type=Application
Name=Pycharm
GenericName=Pycharm3
Comment=Pycharm3:The Python IDE
Exec=sh /home/magic/opt/pycharm-community-2018.2.4/bin/pycharm.sh
Icon=/home/magic/opt/pycharm-community-2018.2.4/bin/pycharm.png
Terminal=pycharm
Categories=Pycharm;
```


７．最后在搜索里面(super键或者说window键都行)  搜索 pycharm　就能看到了，直接固定在 dock　上，这样就方便以后的使用了 
 