# MATLAB 安装后的启动问题  

MATLAB 安装完成之后, 只能进入到安装目录启动 matlab 程序, 可以通过安装一个小插件解决任意位置启动。  

```bash
sudo apt-get install matlab-support
```

安装之后根据它的指示输入 matlab 的 bin 文件夹所在的目录！   

在提示用户权限的那里, 可以填写自己的用户名.  

## issues 

(1) 如果打开 matlab 后在控制台显示桌面文件保存失败或者其他语

一般接着会打印出什么原因造成的，很大可能时由于权限问题造成的.  

此时只要修改 MATLAB 安装目录的权限即可.  

命令行找到你的安装文件夹，查看其所属用户及所属用户组，看是否为当前用户，如果为 root 用户，需要修改为当前用户:   

```bash
sudo chown -R [user-name] /path/to/matlab/bin/
sudo chgrp -R [user-name] /path/to/matlab/bin/
```
更改文件夹拥有者和用户组，-R：进行递归，连同子目录下的所有文件、目录均会修改.  

(2) 如果遇到提示 no writting permission on directory: home/xxx/.matlab

更改 ~/.matlab 文件夹的用户属性,   

或者删除掉文件夹后再次启动就 OK 了。

```bash
sudo chown -R [user-name] ~/.matlab
# 或者
sudo rm -rf ~/.matlab
```
