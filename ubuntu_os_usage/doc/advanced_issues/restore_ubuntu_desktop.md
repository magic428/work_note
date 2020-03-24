# 将 xubuntu 桌面系统恢复到 ubuntu 桌面系统

假定读者原来的系统为ubuntu桌面系统，并且根据如下命令更换到xubuntu桌面系统.  

```bash
sudo apt-get install xrdp
sudo apt-get install vnc4server
sudo apt-get install xubuntu-desktop
echo "xfce4-session" >~/.xsession
sudo service xrdp restart
```

在这个过程中，更改了桌面系统。如果需要恢复到原ubuntu桌面系统并将原来xubuntu桌面系统删除，需要更改的部分有  

1. 开关机动画  
2. 登录界面  

主要更改过程如下：  

## 1. 将原xubuntu桌面系统及配置文件删除  

```bash
sudo apt-get remove --purge xfce4*
sudo apt-get remove --purge xubuntu*
sudo apt-get autoremove
sudo apt-get clean
```
## 2. 更改开机动画

```bash
sudo update-alternatives --config default.plymouth
```

选择 ubuntu-logo.plymouth 对应的选项，比如这里选择1，然后回车。  

## 3. 更改登陆界面

输入如下命令可以恢复原来的登录界面  

```bash
sudo apt purge lightdm-gtk-greeter lightdm-gtk-greeter-settings
sudo systemctl restart lightdm
```

经过这三步操作，便可以由 xubuntu 桌面系统恢复至 ubuntu 桌面系统。  

## 参考文章

[在xubuntu-destory中怎么恢复到ubuntu原来的主题和登陆界面](https://blog.csdn.net/w746805370/article/details/50967133)  
[更改Ubuntu或Linux Mint开机启动画面](https://www.sysgeek.cn/change-boot-splash-screen-ubuntu/)  
[Ubuntu 16.04 美化——用户登录界面修改](https://blog.csdn.net/mutilcam_prince/article/details/78289664)  
