# Ubuntu 系统安装     

## Ubuntu 系统备份和恢复 

这篇文章给大家详细介绍了 `Ubuntu` 备份和恢复的方法,  使用 tar 工具就可以直接备份和恢复.  

**注意：**  

(1) 一定要重新备份下：`/boot`和`/etc/fstab`, 然后再执行恢复命令.    
(2) 在重新启动之前, 一定要将这两个这些文件更新.   

### 1. 清理缓存、回收站, 删除系统不再使用的孤立软件   

```bash  
# 将已经删除了的软件包的.deb安装文件从硬盘中删除掉
$ sudo apt-get autoclean   
# 类似上面的命令, 但它删除包缓存中的所有包.    
$ sudo apt-get clean
$ sudo apt-get autoremove
```
 
### 2. 使用 tar 备份  

1) 命令及参数解释    

v: 显示详细的压缩信息   
c： 创建 tar 包   
j： 使用 bzip2 压缩格式    
z： 使用 gzip 压缩格式    
p： 使用绝对路径    
f： 生成的压缩文件的路径    

2) 切换到 root 用户   

```bash
$ su - root
```

3) 使用 gzip 压缩格式 (压缩略低, 但是速度快)  

```bash
$ tar vzcpf /media/magic/SeagatePlus/work/ubuntu-sys-bak/ubuntu_`date +%Y%m%d_%H`.tar.gz --exclude=/proc --exclude=/dev --exclude=/mnt --exclude=/media --exclude=/boot --exclude=/lost+found --exclude=/cdrom --exclude=/tmp --exclude=/sys --exclude=/home/magic/.cache --exclude=/etc/fstab --exclude=/home/magic/work --exclude=/home/magic/share --exclude=/home/magic/data --exclude=/run  / > /media/magic/SeagatePlus/work/ubuntu-sys-bak/ubuntu_`date +%Y%m%d_%H`.log 2> /media/magic/SeagatePlus/work/ubuntu-sys-bak/ubuntu_`date +%Y%m%d_%H`.error
```

其中, `-exclude=` 表示这些目录并不会被打包. 这里有：/proc, /dev, /mnt, /media, /lost+found, /cdrom, /tmp, /sys, /home/magic/.cache, /run.     

- 如果你的硬盘已经分区了`/home`, 则应该对`/home`目录单独备份;   
- 不备份保存备份得到的镜像文件所在的目录.   

4) 使用 bzip2 压缩格式 (压缩略高, 但是速度慢)  

```bash
$ tar vjcpf /home/magic/data/ubuntu_`date +%Y%m%d`.tar.bz2 --exclude=/proc --exclude=/dev --exclude=/mnt --exclude=/media --exclude=/lost+found --exclude=/cdrom --exclude=/tmp --exclude=/sys --exclude=/home/magic/.cache --exclude=/home/magic/data --exclude=/home/magic/work --exclude=/etc/fstab --exclude=/boot --exclude=/run  / > /home/magic/data/ubuntu_`date +%Y%m%d`.log 2> /home/magic/data/ubuntu_`date +%Y%m%d`.error
```

### 3. 备份两个重要的文件    

备份 `/boot` 和 `/etc/fstab`.  其实上边的命令后来修改之后就不再备份这两个文件了.   

```bash
sudo cp -R /boot /home/magic/boot
sudo cp /etc/fstab /home/magic/fstab
```

同时更新系统的启动项.   

```bash
sudo update-grub
```

### 4. 删除不想要的备份文件和目录

如果发现一些本不想备份的目录已经备份到压缩镜像文件中, 可以使用下面的命令删除不想要的备份文件和目录.   

```bash
tar -cvf  ubuntu_20180907_21.tar.gz --remove-files /home/magic/data  
```

### 5. 恢复系统    

将备份文件拷贝到 / 目录, 执行恢复命令：   

1) 使用 gzip 格式   

```bash
$ su - root
$ tar vxzpf ubuntu*.tar.gz -C /
```

2) 使用 bzip2 格式   

```bash
$ tar vxjpf ubuntu*.tar.bz2 -C /
```

## 比较合理的备份方法

将常用的和稳定不变的文件夹分开备份.   

1) 备份系统  

```bash
tar vzcpf /media/magic/SeagatePlus/work/ubuntu-sys-bak/ubuntu_`date +%Y%m%d_%H`.tar.gz --exclude=/home/magic/work --exclude=/home/magic/data --exclude=/home/magic/opt --exclude="/opt/VirtualBox VMs" --exclude=/home/magic/.cache --exclude=/home/magic/.config --exclude=/proc --exclude=/dev --exclude=/mnt --exclude=/media --exclude=/lost+found --exclude=/cdrom --exclude=/tmp --exclude=/sys --exclude=/run --exclude=/etc/fstab / > /media/magic/SeagatePlus/work/ubuntu-sys-bak/ubuntu_`date +%Y%m%d_%H`.log
```

2) 备份 opt 中的稳定文件夹  

常用的文件夹位于 home/magic/opt/exclude 目录下.  

```bash
tar vzcpf /media/magic/SeagatePlus/work/ubuntu-sys-bak/opt_`date +%Y%m%d_%H`.tar.gz --exclude=/home/magic/opt/exclude /home/magic/opt/ > /media/magic/SeagatePlus/work/ubuntu-sys-bak/opt_`date +%Y%m%d_%H`.log
```

3) 备份 VirtualBox 中的镜像文件   

```bash
tar vzcpf /media/magic/SeagatePlus/work/ubuntu-sys-bak/virtualbox-windows10_`date +%Y%m%d_%H`.tar.gz "/opt/VirtualBox VMs" > /media/magic/SeagatePlus/work/ubuntu-sys-bak/virtualbox-windows10_`date +%Y%m%d_%H`.log  
```
