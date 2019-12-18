# 
BCD 编辑 

http://tieba.baidu.com/p/5003454493?pid=104792401528&cid=0&referer=www.cnblogs.com&pn=0&&red_tag=s0145650392

使用老毛桃的 UEFI GPT 引导, 设置系统磁盘和引导所在磁盘.  


## Ubuntu 中手动添加 windows 启动项

前提: Ubuntu 安装为 UEFI 引导, Windows 安装也为 UEFI 引导.   

```
menuentry "Windows 10 Profession" {
    insmod part_msdos
    insmod ntfs
    set root=(hd1,msdos1)
    search --no-floppy --fs-uuid --set=root 9A087D21087CFE17
    chainloader ($root)/Windows/Boot/EFI/bootmgfw.efi
}
```

如果 Ubuntu 安装为 UEFI 引导, Windows 安装为 BIOS 引导, 则这个添加项并不起作用.  
