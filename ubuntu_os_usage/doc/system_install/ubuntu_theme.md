# Ubuntu 1804 系统美化  

## 安装 gnome-tweak-tool  

调整 gnome 桌面环境，还是推荐使用 Gnome Tweak Tool，这是一个非常好用的图形化管理工具，可以修改工作区数量、热区等。  

在 Unity 桌面环境下, 有一个类似的软件: Unity Tweak Tool, 注意区分使用.  
 
```bash
sudo apt-get install gnome-tweak-tool
```

安装字体  

Ubuntu 自带的字体不太好看，所以采用文泉译微米黑字体替代，效果会比较好，毕竟是国产字体！  

下载 GitHub 上的[字体](powerline/fonts)到目标目录并解压，进入解压目录，打开终端执行：  

```bash
sudo apt-get install fonts-wqy-microhei
sudo apt-get install fonts-powerline
# clone
git clone https://github.com/powerline/fonts.git --depth=1
# install
cd fonts
./install.sh
# clean-up a bit
cd ..
rm -rf fonts
```


## 系统主题  

推荐我比较喜欢的主题和图标，附上 Github 链接：  

```bash
- 桌面主题：vinceliuice/vimix-gtk-themes: https://github.com/vinceliuice/vimix-gtk-themes.git  
- 图标主题：vinceliuice/vimix-icon-theme: https://github.com/vinceliuice/vimix-icon-theme.git  
```

桌面主题安装：  

进入 GitHub，下载源文件，解压到目标目录并进入，右键点击空白处选择在终端打开，执行： 

```bash
git clone https://github.com/vinceliuice/vimix-gtk-themes.git
sudo ./Vimix-installer
```

按提示输入 i，y，等待安装完成后，在 Gnome-tweak-tool 里选择主题。  

```bash
git clone https://github.com/vinceliuice/vimix-icon-theme.git
./install.sh
```

壁纸推荐网站：Awesome Wallpapers - wallhaven.cc  

## 美化配置 - 切换到类似 Windows 的任务栏 

1) 切换到类似 Windows 的任务栏 - User theme / Dash to dock  

安装 User theme 和 Dash to dock 插件. User theme 使 shell 主题可以使用桌面主题; 更改 dock 的样式，可以使图标居中。  

输入下面的命令开始安装:  

```bash
sudo apt install gnome-shell-extensions gnome-shell-extension-dash-to-panel gnome-tweaks adwaita-icon-theme-full
```

安装完成后，注销系统并登录，以便系统完全识别新安装的工具。在 Gnome-tweak-tool 里可以在扩展里对下载安装的插件进行设置管理。  

- 重新登录后，在 Ubuntu Dash 中输入 gnome-tweaks 以访问 Tweaks 工具.   
- 单击左侧面板中的 Extensions 选项，然后打开 Dash to panel 按钮。  

可以自定义 Dash to Panel 扩展的更多功能。 右键单击“应用程序”按钮，然后单击 “Dash to Panel Settings” 选项， 其中可以设置图标的大小, 是否合并打开的标签, 日期格式的显示, 打开标签的宽度等等.  
