
# vim 添加 python3 支持   

ubuntu 自带的 vim 只支持 python2, 通过 `vim -V`

## 首先删除旧的的 vim   

```bash
sudo apt-get purge vim vim-tiny
```

## 使用源码编译   

### 1. 下载源码   

```bash
git clone https://github.com/vim/vim.git

# 预安装
sudo apt-get install python3-dev ncurses-dev libsm6:i386 libsm-dev libICE-dev
```

### 2. 配置模块以及 vim 安装路径      

**Note**: python2 和 python3 一起运行会不稳定, 因此这里只选择 python3.   

```bash
cd vim/src
./configure --with-features=huge \
            --enable-perlinterp  \
            --enable-rubyinterp \ 
            --enable-multibyte \
            --enable-python3interp  \
            --with-python3-config-dir=/usr/lib/python3.5/config-3.5m-x86_64-linux-gnu \
            --enable-perlinterp=yes \
            --enable-luainterp=yes \
            --enable-gui=gtk2  \
            --enable-cscope \ 
            --with-x        \
            --with-compiledby="asd"   \
            --prefix=/usr/local/vim8  
```

整合为一行就是:  

对于 python3.5, 运行下面的命令:   

```bash
./configure --with-features=huge --enable-perlinterp  --enable-rubyinterp  --enable-multibyte --enable-python3interp  --with-python3-config-dir=/usr/lib/python3.5/config-3.5m-x86_64-linux-gnu --enable-perlinterp=yes --enable-luainterp=yes --enable-gui=gtk2 --enable-cscope  --with-x --with-compiledby="asd" --prefix=/usr/local/vim8  
```

各个参数的含义是:  

--with-features=huge：支持最大特性     
--enable-rubyinterp：启用Vim对ruby编写的插件的支持     
--enable-pythoninterp：启用Vim对python编写的插件的支持     
--enable-luainterp：启用Vim对lua编写的插件的支持   
--enable-perlinterp：启用Vim对perl编写的插件的支持   
--enable-multibyte：多字节支持 可以在Vim中输入中文   
--enable-cscope：Vim对cscope支持   
--enable-gui=gtk2：gtk2支持,也可以使用gnome，表示生成gvim   
--with-python-config-dir=/usr/lib/python3.5/config-3.4m-x86_64-linux-gnu 指定 python 路径   
--prefix=/usr：编译安装路径   

### 3. 编译安装

```bash
sudo make
sudo make install

## 清除安装  
make clean
make distclean
```

### 4. 添加系统环境变量   

编译安装后, vim 的运行路径还没有进入到环境变量中。按照下面的步骤添加：   

```bash
sudo update-alternatives --install /usr/bin/editor editor /usr/local/vim8/bin/vim 1  && sudo update-alternatives --set editor /usr/local/vim8/bin/vim && sudo update-alternatives --install /usr/bin/vim vim /usr/local/vim8/bin/vim 1 && sudo update-alternatives --set vim /usr/local/vim8/bin/vim
```

## 5. 添加 vi 命令 

```bash
sudo ln -s /usr/bin/vim /usr/bin/vi
```

## 问题&解决方案 

(1) 找不到 tgetent()  

```
checking for tgetent in -ltinfo... (cached) yes
tinfo library is not usable
checking for tgetent in -lncurses... no
checking for tgetent in -ltermlib... no
checking for tgetent in -ltermcap... no
checking for tgetent in -lcurses... no
no terminal library found
checking for tgetent()... configure: error: NOT FOUND!
      You need to install a terminal library; for example ncurses.
      Or specify the name of the library with --with-tlib.

```

解决方法:   

```bash
sudo apt-get install ncurses-dev
```

(2) /usr/bin/ld: cannot find -lSM
/usr/bin/ld: cannot find -lICE

```bash
sudo apt-get install libsm6:i386 libsm-dev libICE-dev 
```

(3) Python.h: No such file or directory   

```
sudo apt-get install  python3-dev
```