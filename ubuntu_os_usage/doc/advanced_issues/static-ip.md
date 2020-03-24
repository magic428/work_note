

## Ubuntu 18.04 设置固定IP和DNS

最近Ubuntu 18.04已经成为Ubuntu用户的首选版本之一，但是Ubuntu 18.04采用了netplan和systemd-resolve接管了原有的传统IP/DNS配置，一下很让人无可适从，这里记录一下如何在Ubuntu 18.04上修改IP和DNS。

一. 最顺利的情况：
1. ip addr看到网卡地址。
2. nano /etc/netplan/下面的yaml文件

network:
    ethernets:
        ens160:
            addresses: [10.10.10.150/24]
            gateway4: 10.10.10.254
            dhcp4: no
            optional: true
            nameservers:
                addresses: [114.114.114.114,114.114.115.115]
    version: 2
1
2
3
4
5
6
7
8
9
10
network:
    ethernets:
        ens160:
            addresses: [10.10.10.150/24]
            gateway4: 10.10.10.254
            dhcp4: no
            optional: true
            nameservers:
                addresses: [114.114.114.114,114.114.115.115]
    version: 2
3. 执行netplan apply生成，如果不报错则为成功。
4. 如果提示报错，一般是因为不支持optional的nameservers，将其删去即可。
5. 那么需要手工对resolved进行修改，执行nano /etc/systemd/resolved.conf
6. 将#DNS去掉，改为DNS=114.114.114.114 114.114.115.115，保存后执行以下命令即可

root@user:~# systemd-resolve --flush-caches
root@user:~# systemd-resolve --reset-server-features
1
2
root@user:~# systemd-resolve --flush-caches
root@user:~# systemd-resolve --reset-server-features


## ubuntu16.0.4 设置固定ip地址
 发表评论
 313
A+
所属分类：PHP源码
由于Ubuntu重启之后，ip很容易改变，可以用以下方式固定ip地址

1.设置ip地址

vi /etc/network/interface

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
auto ens32
iface ens32 inet static
address 192.168.159.130
netmask 255.255.255.0
gateway 192.168.2.1
2.设置dns

vi /etc/resolvconf/resolv.conf.d/base
nameserver 8.8.8.8
nameserver 8.8.4.4

3.刷新配置文件

resolvconf -u

4.重启网络服务

/etc/init.d/networking restart

如果上述命令重启网卡失败，可以手动关闭网卡，再打开网卡，这是ip已经改过来了，变成你设置的固定的ip了

最新发布的ubuntu18.04 server，启用了新的网络工具netplan，对于命令行配置网络参数跟之前的版本有比较大的差别，现在介绍如下：
1.其网络配置文件是放在/etc/netplan/50-cloud-init.yaml, 缺省是用dhcp方式，如果要配置静态地址，则需要修改此文件的想关内容，见如下的例子：
network:
ethernets:
ens33:
addresses: [192.168.1.20/24]
dhcp4: false
gateway4: 192.168.1.1
nameservers:
addresses: [192.168.1.1]
optional: true
version: 2
2.使其生效的方法：
sudo netplan apply
如果配置有问题会报错，如果没问题，则会新的配置会立即生效。
注意：本帖子只是针对ubuntu18.04 Server版，对于18.04 desktop它缺省是使用NetworkManger来进行管理，可使用图形界面进行配置，其网络配置文件是保存在：/etc/NetworkManager/system-connections目录下的，跟Server版区别还是比较大的。

netplan 工具还有其它比较丰富的功能，详细可参见其的说明文档，man netplan.


