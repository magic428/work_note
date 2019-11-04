# Ubuntu 14.04 更换软件下载源	 

>  ubuntu 14.04: trusty.    
>  ubuntu 16.04: xenial.    

## 163 网易源  

使用下面的行直接替换原来的地址:    

```bash
# Ubuntu 1404
deb http://mirrors.163.com/ubuntu/ trusty main universe restricted multiverse
deb-src http://mirrors.163.com/ubuntu/ trusty main universe restricted multiverse
deb http://mirrors.163.com/ubuntu/ trusty-security universe main multiverse restricted
deb-src http://mirrors.163.com/ubuntu/ trusty-security universe main multiverse restricted
deb http://mirrors.163.com/ubuntu/ trusty-updates universe main multiverse restricted
deb http://mirrors.163.com/ubuntu/ trusty-proposed universe main multiverse restricted
deb-src http://mirrors.163.com/ubuntu/ trusty-proposed universe main multiverse restricted
deb http://mirrors.163.com/ubuntu/ trusty-backports universe main multiverse restricted
deb-src http://mirrors.163.com/ubuntu/ trusty-backports universe main multiverse restricted
deb-src http://mirrors.163.com/ubuntu/ trusty-updates universe main multiverse restricted
```

## 阿里云  

```bash
# Ubuntu 1604
#deb包
deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
##测试版源  
deb http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse
# 源码  
deb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
##测试版源  
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse

# Ubuntu 1404
deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
```
