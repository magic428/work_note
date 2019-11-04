# Windows 下 VS Code Remote-Development(ssh) 的配置和使用   

本文主要介绍如何通过 ssh 的方法链接到远程机器（必须是 Linux 系统）上，另外插件还提供了连接到 WSL 和容器的功能。 配置的过程如下：  


## 1. 远程主机安装 ssh-server

```bash
# ubuntu 系统
sudo apt-get install openssh-server
```

## 2. 本地主机安装 ssh-client

windows 系统中下载安装 OpenSSH，下载地址： https://github.com/PowerShell/Win32-OpenSSH/releases/  

下载完成后解压即完成安装， 然后配置该目录到系统环境变量 Path 中。 最后在 Cmd 终端中打开输入 `ssh` 测试是否安装成功。  

## 3. 安装 vscode insiders 版本 

注意： 一定是 insiders 测试版本，因为当前 Remote Development 插件只能用于测试版。

## 4. 安装插件  

在 vscode insiders 中安装 Remote Development 插件。  

## 5. 设置 Show Login Terminal  

在 VSC 的 settings 中搜索 "remote.SSH.showLoginTerminal"， 将其设置为 true。  

## 6. 设置无密码登陆服务器  

```bash
# 生成本地密钥， 该命令在本地电脑端完成
ssh-keygen -t rsa -b 4096 -f %USERPROFILE%\.ssh\id_rsa-remote-ssh

# 将本地公钥上传到服务器，并添加到 authorized_keys 文件中。
scp %USERPROFILE%\.ssh\id_rsa-remote-ssh.pub %REMOTEHOST%:~/tmp.pub  # 将本地公钥上传到服务器
ssh %REMOTEHOST%    # 登陆服务器
cat ~/tmp.pub >> ~/.ssh/authorized_keys  # 添加到 authorized_keys 文件中
rm -f ~/tmp.pub
```

注意， 需要将命令行中的变量替换为具体的内容： 

- %USERPROFILE%  C:\Users\xxx  
- %REMOTEHOST% username@192.168.1.xxx

## 7. 连接远程主机  

安装完插件后左下角会出现一个绿色的图标，点击选择会在命令窗口弹出几个选项。 选择 SSH | Remote-SSH：Connect to Host | Configure SSH Hosts... | C:\Users\xxx\config。   

然后配置 config 信息，Host 是自己给这份配置文件起的名字，HostName 是远程主机的 IP 地址，User 是服务器系统的用户名。  

```conf
Host ubuntu-server
    HostName 192.168.1.xxx
    User username
    IdentityFile ~/.ssh/id_rsa-remote-ssh
```

注意， 最后一行是不需要修改的。   

输入完毕后保存，VS Code 左侧会出现配置好服务器信息，右键登陆即可。 
