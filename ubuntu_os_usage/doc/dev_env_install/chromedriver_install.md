# 在 Ubuntu 上安装 ChromeDriver - Headless Chrome

> 和 Selenium 模块一起用于 Python 爬虫程序中.   
> pip3 install selenium  // 安装 selenium

## 1. 安装 Chrome 浏览器  

1) 安装依赖   

```bash
sudo apt-get install libxss1 libappindicator1 libindicator7
```

2) 下载 Chrome 安装包   

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

3) 安装 chrome    

```
sudo dpkg -i google-chrome*.deb
sudo apt-get install -f
```

## 2. 安装 ChromeDriver  

1) 安装 xvfb 以便我们可以无头运行 Chrome.  

```bash
sudo apt-get install xvfb
```

2) 安装依赖  

```bash
sudo apt-get install unzip
```

3) 下载安装包   

```bash
wget -N http://chromedriver.storage.googleapis.com/2.26/chromedriver_linux64.zip   
``` 

4) 解压缩 + 添加执行权限

```bash
unzip chromedriver_linux64.zip
```

5) 移动文件夹到系统目录下   

```bash
sudo mv -f chromedriver /usr/local/share/chromedriver
```

6) 建立应用程序软连接  

```bash
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```

## 3. 无头运行Chrome

1) 安装 Python 依赖   

```
pip3 install selenium

pip3 install pyvirtualdisplay
```

## 4. 使用示例   

```python
from pyvirtualdisplay import Display
from selenium import webdriver
 
display = Display(visible=0, size=(800, 600))　　# 初始化屏幕
display.start()　　
driver = webdriver.Chrome()　　# 初始化Chrome
driver.get('http://www.cnblogs.com/x54256/')
print (driver.title)
```

