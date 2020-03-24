# dpkg-warning

每次使用 apt 安装软件的时候都会打印以下信息:   

```bash
dpkg: warning files list file for package '...' missing, assuming package has no files currently installed.
```

## 解决办法  


新建一个 dpkg_warning.sh, 写入以下内容.  

```bash
#!/bash/sh

for package in $(apt-get install --reinstall cmake 2>&1 |\
                 grep "warning: files list file for package '" |\
                 grep -Po "[^'\n ]+'" | grep -Po "[^']+"); do
    apt-get install --reinstall "$package";
done
```

或者直接拷贝到命令行执行: 

```bash
for package in $(apt-get install --reinstall cmake 2>&1 | grep "warning: files list file for package '" | grep -Po "[^'\n ]+'" | grep -Po "[^']+"); do apt-get install --reinstall "$package"; done
```

这个命令需要在 root 用户下运行, 同时会花费很长时间.   

## issues 

1. dpkg error while process package foomatic-filters libpaper1:amd64  

```bash
dpkg: error processing package libpaper-utils (--configure):
 dependency problems - leaving unconfigured
Processing triggers for libc-bin (2.23-0ubuntu10) ...
Errors were encountered while processing:
 foomatic-filters
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

可使用以下办法解决：

```bash
sudo apt purge foomatic-filters
```

如果卸载时提示有配置文件无法删除, 则手动删除:  

```bash
Purging configuration files for foomatic-filters (4.0.17-8) ...
dpkg: warning: while removing foomatic-filters, directory '/usr/lib/cups/filter' not empty so not removed
Processing triggers for man-db (2.7.5-1) ...
```

然后到 /var/lib/dpkg/info 目录下，删除以上出现包名字开头的文件，然后重新执行:  

```bash
sudo apt install foomatic-filters
```

**Note:** 一定要检查软件源地址是否包含安装的软件.   

