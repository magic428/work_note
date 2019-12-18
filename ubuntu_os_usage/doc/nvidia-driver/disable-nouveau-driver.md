# 禁用 Nouveau 驱动并安装 NVIDIA 显卡驱动

> 注意: 以下步骤一个都不能少.   

## (1) 首先添加一个 blacklist  

```bash
sudo gedit /etc/modprobe.d/blacklist-nouveau.conf
```

在这个文件中写入以下内容：  

```conf
blacklist nouveau
blacklist lbm-nouveau
options nouveau modeset=0
alias nouveau off
alias lbm-nouveau off
```

## (2) 在内核中直接禁用 Nouveau  

```bash
echo options nouveau modeset=0 | sudo tee -a /etc/modprobe.d/nouveau-kms.conf
``` 

## (3) 删除对应内核中 nouveau.ko  

```bash
cd /lib/modules/4.15.0-51-generic/kernel/drivers/gpu/drm/nouveau/
sudo mv nouveau.ko nouveau.ko.bak
```

之后，更新配置试生效：

```bash
update-initramfs -u
```

重启后再次进入系统, nouveau 驱动被禁用。 使用 NVIDIA 官网下载好的离线驱动安装包安装显卡驱动即可.    

## ubuntu 1804  
https://blog.csdn.net/kjopojd/article/details/99344672


