# Windows 10下怎么远程连接 Ubuntu 16.0.4（小白级教程）

## 前言   

公司因为用 Ruby 做开发，所有适用了Ubuntu系统，但是自己笔记本是W10，又不想装双系统，搭建开发环境，便想到倒不如自己远程操控公司电脑，这样在家的时候也可以处理一些问题。故此便有了下面的安装步骤。

环境：

　　  Windows 10 ,Ubuntu 16.0.4

安装步骤：

　　  Ubuntu下：

　　　　　1.右击桌面打开终端，或快捷键Ctrl+Shift+T打开终端

　　　　　　1.1 输入ifconfig查看电脑ip地址

　　　　　　　　

　　　　　　　1.2 enp2s0下的inet6是你的IP地址，比如我的ip是 192.168.11.134 

　　　　　　　1.3鼠标选中右击复制下来，记住，下面到windows会用到

　　　　　2.终端继续输入以下命令，安装XRDP协议跟VNCServer监听服务

```bash
sudo apt-get install xrdp vnc4server xbase-clients
```
　　　　　3.Ubuntu搜索栏搜索桌面共享工具desktop sharing(Ubuntu16.04下是默认安装的)

　　　　　　　　

　　　　　4.打开，并按以下选择：

　　　　　　　　4.1 勾选允许他人查看桌面，默认是关闭的

　　　　　　　　

　　　　　　　　4.2记住输入的密码，在Windows下要用到

　　　　  5.安装注册表编辑器

```bash
sudo apt-get install dconf-editor
```
 　　　　　　5.1 搜索栏输入dconf,打开

　　　　　　　　　　

　　　　　　 5.2 双击打开，并根据路径选择  org > gnome > desktop > remote-access，取消 “require-encryption”和“view-only”，如果你只想在windows远程端观看，则勾选“view-only”，否则取消

　　　　　　

　　　　　　到此为止，Ubuntu下的准备工作就结束了。

　　　Windows下：

　　　　　　　1.左下角搜索栏输入 远程桌面连接

　　　　　　　　　根据要求输入Ubuntu的ip，就是上面ubuntu下1.2步骤叫你记住的ip

　　　　　　　2.然后会看到下面图形界面，

　　　　　　　　　　 Module下拉选择vnc-any,

　　　　　　　　　　 ip填入刚刚ubuntu的ip地址，

　　　　　　　　　　 port端口保持5900不变，

　　　　　　　　　　password是在ubuntu下4.2步骤输入的密码

　　　　　　　　　　　　　　　　　　输入完毕后点击OK

　　　　　　　　　 

 到此为止，就结束了，然后就可以为所欲为了。好了，开始你的玩法吧！

 