# 在 Ubuntu 中使用 Windows 字体集

## 1. 拷贝 Windows 字体集

将 Windows 系统下字体文件夹（C:\Windows\Fonts）打包为 Windows-Fonts.zip.    

宋体：simsunb.ttf 和 simsun.ttc

微软雅黑：msyhbd.ttf

Courier New：courbd.ttf、courbi.ttf、couri.ttf 和 cour.ttf

WPS Office 所需字体：wingding.ttf、webdings.ttf、symbol.ttf、WINGDNG3.TTF、WINGDNG2.TTF、MTExtra.ttf

## 2. 在 Ubuntu 中创建字体缓存  

```bash
sudo mkdir /usr/share/fonts/truetype/windows-font
sudo unzip Windows-Fonts.zip -d /usr/share/fonts/truetype/windows-font

#修改权限，并更新字体缓存
sudo chmod -R 777  /usr/share/fonts/truetype/windows-font
cd /usr/share/fonts/truetype/windows-font
sudo mkfontscale
sudo mkfontdir
```

## 刷新字体缓存  

```bash
sudo fc-cache -fv
```

重启后即可使用.  
