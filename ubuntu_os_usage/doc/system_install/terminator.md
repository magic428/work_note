# 安装终端分屏：Terminator - 终端终结者  

本文所指的 Terminator 不是 Ubuntu 18.04 默认自带的命令行终端, 而是 GNOME 图形化界面下的 gnome-termina.  

> 目的：可以将终端分屏, 这样我们在练习程序和编写或者对比文件的时候非常有用.   

对 Linux 系统进行管理时, 我们经常需要通过终端窗口输入各种操作命令. 在 GNOME 集成桌面环境下, GNOME 终端 (gnome-terminal) 是我们经常使用的终端程序, 每次运行该程序都将打开一个单独的终端窗口. 当我们进行命令行操作时, 有时需要打开多个终端窗口, 并且希望这些窗口能同时平铺显示, 那该怎么办呢?其实, 借助一款小巧而实用的软件—— Terminator 就可以轻松实现这一功能.  

使用 Terminator 可以在一个窗口中显示多个 GNOME 终端窗口, 并且可以按照用户的要求对窗口进行任意分割.  

## 安装 Terminator

打开终端, 输入以下命令：

```bash
sudo apt-get install terminator
```

安装终端程序 terminator, 安装完毕后按 ctrl+alt+t 打开终端.  

## 在系统中添加右键打开 Terminator  

```bash
sudo add-apt-repository ppa:daniel-marynicz/filemanager-actions

sudo apt-get install filemanager-actions-nautilus-extension # Nautilus
sudo apt-get install filemanager-actions-caja-extension # Caja
sudo apt-get install filemanager-actions-nemo-extension # Nemo

sudo apt-get install filemanager-actions* # simply all filemanagers
```

修改右键

fma-config-tool

配置Action

1)新建action
命名：Open in Terminator
在Action标签页勾选"Display item in location context menu"
在Command标签页填写Path:/usr/bin/terminator，parameters:--working-directory=%d/%b

2)配置Preferences
勾选"Create a root 'FileManager-Action' menu"
————————————————
版权声明：本文为CSDN博主「Flying_Motor」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Flying_Motor/article/details/97800781

## Terminator 快捷键

这个终端程序可以分屏, 常用操作快捷键如下：

| Ctrl+Shift+O        | 上下开新窗口     |
| Ctrl+Shift+E        | 垂直开新窗口     |
| Ctrl+Shift+Right    | 向右放大当前窗口 |
| Ctrl+Shift+Left     | 向左放大当前窗口 |
| Ctrl+Shift+Up       | 向上放大当前窗口 |
| Ctrl+Shift+Down     | 向下放大当前窗口 |
| Ctrl+ D             | 关闭当前终端窗口 |


Alt+Up  |    Move to the terminal above the current one.（切换当前窗口）
Alt+Down    |    Move to the terminal below the current one.
Alt+Left|    Move to the terminal left of the current one.
Alt+Right|    Move to the terminal right of the current one.
Ctrl+Shift+S|    Hide/Show Scrollbar.（隐藏滚动条）
Ctrl+Shift+F|    Search within terminal scrollback
Ctrl+Shift+N or Ctrl+Tab|    Move to next terminal within the same tab, use Ctrl+PageDown to move to the next tab. If cycle_term_tab is False, cycle within the same tab will be disabled
Ctrl+Shift+P or Ctrl+Shift+Tab|    Move to previous terminal within the same tab, use Ctrl+PageUp to move to the previous tab. If cycle_term_tab is False, cycle within the same tab will be disabled

Ctrl+Shift+C|    Copy selected text to clipboard
Ctrl+Shift+V|    Paste clipboard text
Ctrl+Shift+Q|    Quits Terminator
Ctrl+Shift+X （最大化当前窗口）|    Toggle between showing all terminals and only showing the current one (maximise).
Ctrl+Shift+Z|    Toggle between showing all terminals and only showing a scaled version of the current one (zoom).
Ctrl+Shift+T|    Open new tab
Ctrl+Shift+Alt+T|    Open new tab at root level, if using extreme_tabs.
Ctrl+PageDown|    Move to next Tab
Ctrl+PageUp|    Move to previous Tab
Ctrl+Shift+PageDown|    Swap tab position with next Tab
Ctrl+Shift+PageUp|    Swap tab position with previous Tab
Ctrl+Shift+F|    Open buffer search bar to find substrings in the scrollback buffer. Hit Escape to cancel.


Ctrl+Plus (+)|    Increase font size. Note: this may require you to press shift, depending on your keyboard
Ctrl+Minus (-)|    Decrease font size. Note: this may require you to press shift, depending on your keyboard
Ctrl+Zero (0)|    Restore font size to original setting.

F11|    Toggle fullscreen（放大当前窗口）
Ctrl+Shift+R|    Reset terminal state
Ctrl+Shift+G|    Reset terminal state and clear window
