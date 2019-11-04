# Ubuntu 16.04 WPS 文字、表格、演示均不能输入中文 

原因：环境变量未正确设置。   

解决办法:  

## WPS文字

```bash
sudo vim /usr/bin/wps
```

添加一下文字到打开的文本中（添加到“#!/bin/bash”下面）：   

```
export XMODIFIERS="@im=fcitx"
export QT_IM_MODULE="fcitx"
```

## WPS表格

```bash
sudo vim /usr/bin/et
```

添加一下文字到打开的文本中（添加到“#!/bin/bash”下面）：  

```
export XMODIFIERS="@im=fcitx"
export QT_IM_MODULE="fcitx"
```
## WPS演示

```bash
sudo vim /usr/bin/wpp
```

添加一下文字到打开的文本中（添加到“#!/bin/bash”下面）：  
```bash
export XMODIFIERS="@im=fcitx"
export QT_IM_MODULE="fcitx"
```

修改完后保存，打开相应的程序切换输入法就可以输入中文了。  
