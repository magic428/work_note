# VSCode 中使用 Python 补全  

安装 "python" 插件和 pylint.  

```bash
sudo pip3 install -U pylint --user
```

在 settings.json 配置文件中添加:  

```json
"python.pythonPath": "/usr/bin/python3", 

// python auto complete
"python.autoComplete.extraPaths": [
    "/usr/local/lib/python3.5/dist-packages/",
    "/home/magic/work/pyenv/dl/lib/python3.5/site-packages/"
],
```

最后一定要选择 Python 解释器.  
