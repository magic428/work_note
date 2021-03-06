# ubuntu 系统遇到的问题及解决方法   

## 系统开发环境搭建  

### 1. 安装 OpenCV  


- [ Thunderbird 邮件客户端配置 - tdmarco/qq/126 ](doc/dev_env_install/thunderbirdMail.md)
- [ Ubuntu 16.04 安装 boost 库 ](doc/dev_env_install/boost_install.md)
- [ 在 Ubuntu 上安装 ChromeDriver](doc/dev_env_install/chromedriver_install.md)
- [ 在 Ubuntu 14.04 安装和使用 Docker](doc/dev_env_install/docker_install.md)


## 开发工具   
- [ sublime-text 环境配置相关](doc/sublime-text3/README.md)   
- [ git 使用 skills ](doc/git_usage/README.md)  
- [ vi 使用教程](doc/vi_usage/README.md)  
 
## 常用命令   
- [ ubuntu 常用命令 cheatsheet](doc/advanced_issues/quick_cmd.md)  
- [ grep 用法](doc/advanced_issues/grep_usage.md)   
- [ nohup 的使用](doc/advanced_issues/nohup.md)   
 
## 安装系统必备    
- [Ubuntu 1404 更换软件下载源](doc/system_install/sourceslist.md)  
- [安装 Ubuntu/Windows 双系统中出现的问题](doc/system_install/os_install.md)  
- [修改系统默认启动 ubuntu 或 windows](doc/system_install/default_grub.md)  
- [pip install 更换源](doc/system_install/pip_install_source.md)  
- [搜狗输入法的安装和卸载](doc/system_install/sogou_install.md)  
- [.bashrc 文件的配置](doc/system_install/bashrc_config.md)  
- [鼠标右键添加'在当前位置打开终端'](doc/system_install/open_termials.md)  
- [配置 shadowsocks](doc/system_install/shadowsocks_install.md)  
- [ssh-keygen 生成步骤](doc/system_install/ssh_keygen.md)  
- [jupyter-python2.7 安装问题](doc/system_install/jupyter_python2.7_install.md) 
- [Ubuntu 16.04 系统备份和恢复](doc/system_install/system_backup_recover.md)  
- [在 virtual box 中安装 windows10](doc/system_install/install_windows_in_virtualbox.md)  
- [在 ubuntu 中同时安装 opencv 3 和 opencv 2](doc/system_install/install_opencv2_and_opencv3.md)  
- [在 ubuntu 中安装 meshLab](doc/system_install/meshlab.md)  
- [ubuntu 清理内存](doc/system_install/ubuntu_memory_cleanup.md)  
- [vs code 用户配置](doc/system_install/vs_code_user_settings.md)  
- [安装最新版本的 Nodejs ](doc/system_install/nodejs_install.md)  
 
## 系统使用中的坑   

- [chrome 提示无法正确打开您的个人资料](doc/advanced_issues/chrome.md)  
- [ubuntu 14.04 状态栏不显示时间](doc/advanced_issues/timedate_bar.md)  
- [ubuntu 14.04 设置程序启动快捷键](doc/advanced_issues/shortcuts.md)  
- [更改 ubuntu 启动等待时间](doc/advanced_issues/grub_timeout.md)  
- [ubuntu 安装 Java1.7](doc/advanced_issues/java1.7_install.md)  
- [如何让普通用户访问 /dev/ttyUSB0 ](doc/advanced_issues/minicom_permision.md)  
- [搭建 iTop4412 使用的 NFS 环境 ](doc/advanced_issues/nfs.md)  
- [NVIDIA GeForce 720M 驱动安装](doc/advanced_issues/nouveau_nvidia.md)  
- [修改命令提示符 PS1 ](doc/advanced_issues/ps1_modify.md)  
- [ubuntu ss5 polipo 全局代理](doc/advanced_issues/ss5-polipo_proxy.md)  
- [system settings 里面选项丢失](doc/advanced_issues/system_setting.md)  
- [ubuntu 终端闪退](doc/advanced_issues/terminals_crash.md)  
- [python-apt 出错](doc/advanced_issues/no_module_named_apt_pkg.md)  
- [改变系统中的默认的 python 版本](doc/advanced_issues/change_python_version_in_system.md)   
- [ubuntu 查看内核版本](doc/advanced_issues/ubuntu_kernel_version.md)  
- [chrome 推送网页内容到 kindle ](doc/advanced_issues/send_chrome_to_kindle.md)  
- [安装和使用 Docker ](doc/advanced_issues/docker_install.md)  
- [查看目录占用的磁盘空间](doc/advanced_issues/disk_space_usage.md)   
- [qt 无法使用搜狗输入法](doc/advanced_issues/qt_sogou.md)   
- [将 pip3 指向 python3.5](doc/advanced_issues/pip3_5.md)   
- [Chrome 浏览器无法调用 GPU 进程](doc/advanced_issues/chrome_launch_gpu.md)   
- [ubuntu 连接投影仪失败或显示不正常](doc/advanced_issues/projector.md)   
- [在 Ubuntu 上安装 ChromeDriver](doc/advanced_issues/chromedriver_install.md)   
- [配置 Fiddler 抓包工具](doc/advanced_issues/mono_fiddler.md)   
- [gitbook 安装 / 配置 ](doc/advanced_issues/gitbook_install.md)   
- [清理 ubuntu 系统](doc/advanced_issues/clean_ubuntu_system.md)   
- [安装 mayavi 模块](doc/advanced_issues/install_mayavi.md)   
- [将 xubuntu 桌面系统恢复到 ubuntu 桌面系统](doc/advanced_issues/restore_ubuntu_desktop.md)   




正则表达式转换python2的print为python3风格: 直接查找 print ([^\n\(]*)替换为 print($1).   