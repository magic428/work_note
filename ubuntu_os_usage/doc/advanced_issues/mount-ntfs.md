# ubuntu开机自动挂载的ntfs硬盘的权限问题


在linux操作系统中， 挂载是一个非常重要的功能，使用非常频繁。 它指将一个设备（通常是存储设备）挂接到一个已存在的目录上。 （这个目录可以不为空，但挂载后这个目录下以前的内容将不可用。） 需要理解的是， linux操作系统将所有的设备都看作文件， 它将整个计算机的资源都整合成一个大的文件目录。 我们要访问存储设备中的文件，必须将文件所在的分区挂载到一个已存在的目录上， 然后通过访问这个目录来访问存储设备。
挂载条件：
　　1、挂载点必须是一个目录。
　　2、一个分区挂载在一个已存在的目录上，这个目录可以不为空，但挂载后这个目录下以前的内容将不可用。对于其他操作系统建立的文件系统的挂载也是这样。

Ctrl + Alt + T 打开终端，输入以下命令：sudo fdisk -l
查看硬盘的分区情况，如下（本人的，仅作为实例）
Disk /dev/sda: 320.1 GB, 320072933376 bytes
255 heads, 63 sectors/track, 38913 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x624aa2e0

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *           1        2612    20980858+   7  HPFS/NTFS
/dev/sda2            2613        7834    41945715    7  HPFS/NTFS
/dev/sda3            7835       12795    39849232+   7  HPFS/NTFS
/dev/sda4           12796       38913   209792835    7  HPFS/NTFS
使用 sudo gedit /etc/fstab 打开fstab文件，编辑fatab文件，加入相关代码。
Ubuntu自动挂载的Windows分区无法正常显示中文，在etc/fstab里面加上utf8就可以了，例如：
代码:
/dev/sda3       /media/program     ntfs    defaults,utf8        0       0

但是挂载的分区默认是没有写权限的，必须有root权限才能写，如何更改这个设置呢？
用man mount查看手册页，发现里面有几个有用的选项：
umask, fmask, dmask, uid, gid
首先看umask, 这个是用来指定挂载windows分区后文件的默认权限（事实上，是默认没有的权限，即umask参数指出的值挂载后的文件将不具有），
因为Windows分区里面的文件是没有权限这个概念的，所以要手动指定默认权限，于是，指定umask为000,就是不排除任何，即具有所有权限，例如：

代码:
/dev/hda1       /media/hda1     ntfs    defaults,utf8,umask=000        0       0

就可以了，但是这样即使一个文本文件也具有可执行权限，在文件管理器里面双击也要选择是查看还是执行，很不方便，于是想屏蔽掉可执行权限：

代码:
/dev/hda1       /media/hda1     ntfs    defaults,utf8,umask=111        0       0

这样问题又来了，对于目录来说，可执行权限又有另外的意义，没有该权限根本无法进入该目录（但是可以读，即列出目录下的文件列表，也可以写，
即可以在该目录下增加和删除文件，和重命名文件。哈哈！Linux的文件权限真是奇怪呀），于是就使用fmask和dmask参数，他们分别是对应文件和
目录的"umask",于是，将目录设为可执行，文件不可执行（一般Windows分区下都不会有可以直接在Linux下执行的文件吧？）：

代码:
dmask=022,fmask=133

关于权限的8进制表示就不需要多说了吧？
上边的意思是
对目录：
所有用户可执行（进入），其他人可读可执行（进入），只有自己可写（修改、添加、删除里面的文件（名））
对文件：
所有用户可读，自己可写，其他人不可写。
之后在uid和gid为自己的就好了，可以用

代码:
id username

来查看username的gid和uid，例如：

代码:
id pluskid
uid=1000(pluskid) gid=1000(pluskid) groups=4(adm),20(dialout),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),104(lpadmin),105(scanner),106(admin),1000(pluskid)

如果不设的话，上面的“自己可写”那个“自己”就不是你罗。
于是，最后就变成了这样：

代码:
/dev/sda3      /media/program    ntfs    defaults,utf8,uid=1000,gid=1000,dmask=022,fmask=133     0       0

就OK了！
最后，提醒大家，不要改错了，改到非Windows分区上了，我实验的时候就不小心改到root分区了，提供了不能识别的参数，用于 Windows分区的参数ext3分区当然不能识别罗，于是root分区在出现错误的情况下被挂载成只读了，连root也无法修改里面的文件，而 fstab又是放在root分区的，就是个悲剧。（能用livecd修复一下）



## Ubuntu 之开机自动挂载NTFS 解决 chmod 对 NTFS 失效的问题
[日期：2013-01-13]	来源：Linux社区  作者：icegoly	[字体：大 中 小]
Ubuntu 之开机自动挂载NTFS 解决 chmod 对 NTFS 失效的问题。

今天在用C 语言编写了一个程序挂载在 E 盘，准备去执行的时候发现没有执行的权限。

然后  用 chmod  777  hello  然后没有命令执行成功然后用  ls -l 查看权限 并没有改变和之气一样 。。很郁闷。。。。

通过一些搜索。 思考和整理。。  解决该问题。。

下面是解决方法：

1  查看自己的  磁盘分析信息

UUID      UGD    GID    信息

如  查看 UUID  如下

ls -l /dev/disk/by-uuid

lrwxrwxrwx 1 root root 10  1月 12 21:45 0001AC6D000973C1 -> ../../sda5
lrwxrwxrwx 1 root root 10  1月 12 21:45 0003A300000D437F -> ../../sda6
lrwxrwxrwx 1 root root 10  1月 12 21:45 000ACA5D000CE1C1 -> ../../sda8
lrwxrwxrwx 1 root root 10  1月 12 21:45 000E08DD00019CAA -> ../../sda7
lrwxrwxrwx 1 root root 11  1月 12 21:45 158c8fbb-a3d4-4cb9-a7a5-1ecf13586280 -> ../../sda10
lrwxrwxrwx 1 root root 10  1月 12 21:45 18354ee2-3c44-405a-af87-7c2316c45983 -> ../../sda1
lrwxrwxrwx 1 root root 10  1月 12 21:45 f233ebb4-8c6e-48ca-832c-08ceb567f928 -> ../../sda9
lrwxrwxrwx 1 root root 10  1月 12 21:45 FE14E80014E7BA33 -> ../../sda3
lrwxrwxrwx 1 root root 10  1月 12 21:45 FE3438FC3438BA0B -> ../../sda2

查看自己的  磁盘是在sda?  可以通过  sudo fdisk -l 查询  我推荐一个图形化的工具 

GParted 工具  你可以一眼看出

如图：



2 超看GID  （组ID ） 和UID （用户ID ）

可以通过  查看 该文件  查看

vim /etc/passwd

如图：



2 修改  /etc/fstab 文件  (让系统启动的时候 自动挂载 )

sudo gedit /etc/fstab

其中  umask  是权限的  屏蔽  用  777-000 就是你的权限

其中  uid  和 gia  就是 你上面查询的用户 ID 组ID

# windows ntfs  software D
UUID=0001AC6D000973C1 /media/SoftWare          ntfs    defaults,nls=utf8,umask=000,uid=1000,gid=1000        0      0
# windows ntfs  student  E
UUID=0003A300000D437F /media/Student          ntfs    defaults,nls=utf8,umask=000,uid=1000,gid=1000        0      0
# windows ntfs  Media  F
UUID=000E08DD00019CAA /media/Medai            ntfs    defaults,nls=utf8,umask=000,uid=1000,gid=1000        0      0
# windows ntfs  Else  G
UUID=000ACA5D000CE1C1 /media/Else            ntfs    defaults,nls=utf8,umask=000,uid=1000,gid=1000        0      0

3 保存重启即可