# 显卡驱动引起的启动失败   

## 1. /dev/nvem0: clean, 131838/991232 files, 1193255/3933482 blocks    

该错误通常是由于显卡驱动没有被构建到内核中而引起的.  

解决办法如下:  

对于无法使用 `Ctrl + Alt + F[1-7]` 进入命令行的情形, 先选择一个可以进入的内核版本, 然后执行下面的命令:   

```bash
# 删除原有的 xorg.conf 文件
sudo rm -rf /etc/X11/xorg.conf
sudo cp xorg.conf.failsafe xorg.conf 
```

如果这步不起作用, 则只运行 `sudo rm -rf /etc/X11/xorg.conf` 即可, 之后卸载掉系统中的 NVIDIA 驱动.  

然后进入到最新的内核版本后, 使用 `Ctrl + Alt + F[1-7]` 进入命令行, 重新安装 NVIDIA 官网下载的驱动.  

```bash
sudo service lightdm restart 
sudo ./NVIDIA-Linux-x86_64-418.74.run
```

所有的选项中全部选择 yes, 安装完成后重新启动即可.  

