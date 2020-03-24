# docker 方式部署 seafile  

> 环境: Ubuntu 16.04.  


## 1. 使用域名登录网盘.  

1 修改本地hosts文件   

首先在centos命令行中输入ip address，查询该centos的ip地址。


我的电脑是windows操作系统，修改hosts文件（路径为"C:\Windows\System32\drivers\etc\hosts"），末尾处添加

192.168.56.101 seafile.example.com

注意替换192.168.56.101为自己电脑虚拟机上centos的ip地址  



4.2 登录Seafile的web界面

地址栏输入服务器域名，例如之前模拟时设置的http://seafile.example.com，并输入刚才设置的用户名和密码，即可查看seafile的web界面。

## 1. 无法上传文件  

可以尝试更换端口映射.  

80:80

关于系统设置: 

SERVICE_URL http://192.168.1.183:80
FILE_SERVER_ROOT http://192.168.1.183/seafhttp

## 2. sudo docker-compose down 之后云盘数据丢失.  

引入本地卷存储云盘数据库文件, 这样可以解决删除容器后的数据丢失问题.  


## 3. seafile 路径与已有资料库冲突

这是 seafile 客户端工作路径中的某些文件出现读写权限问题.  

**解决方法：**

1、删除 C:\Users\${用户名}\ccnet\seafile.ini 配置文件.  
2、重新运行 seafile、设置新工作路径、添加账号，即可同步。  


## 4. docker 中使用本地卷保存配置信息时, 更改 ip 地址后并不会在配置中重新生成.   

如果 IP 地址更改之后, 需要更改本地卷 shared/seafile/conf/ccnet.conf 和 shared/seafile/conf/seahub_settings.py 中对应的服务器 IP 地址.  


## 5. Windows 部署 seafile  

使用 80 端口, 并需要关闭防火墙.  


服务器从 Windows 迁移到 Linux
假设你当前已经在使用 Windows 服务器(使用 SQLite 数据库)，现在希望把服务器迁移到 Linux 下。

1. 安装 Linux 服务器
第一步你需要安装全新一个 Linux 服务器。同样使用 SQLite 数据库。下面假设你把 Seafile 服务器默认安装在 /home/haiwen/ 目录下。

2. 替换数据和配置文件
删除 Linux 的配置文件和数据
rm /home/haiwen/seahub_settings.py

rm /home/haiwen/seahub.db

rm -r /home/haiwen/seafile-data

cp /home/haiwen/ccnet/seafile.ini /home/haiwen/seafile.ini

rm -r /home/haiwen/ccnet


其中 seafile.ini 指向 seafile-data 目录所在位置，等会需要用到，这里先拷贝出来。

拷贝配置文件和数据
将 Windows 中 seafile-server 文件夹下的 seahub_settings.py 文件，拷贝到 linux /home/haiwen/ 目录下

将 Windows 中 seafile-server 文件夹下的 seahub.db 文件，拷贝到 linux /home/haiwen/ 目录下；

将 Windows 中 seafile-server 的子文件夹 seafile-data，拷贝到 linux /home/haiwen/ 目录下；

将 Windows 中 seafile-server 的子文件夹 ccnet，拷贝到 linux /home/haiwen/ 目录下；

将  /home/haiwen/seafile.ini 拷贝到新 ccnet 目录中

1. 安装 Linux 服务器
2. 替换数据和配置文件
最近修改 Daniel Pan, a year ago


需要复制的文件  

shared/seafile/seafile-data 文件夹 

