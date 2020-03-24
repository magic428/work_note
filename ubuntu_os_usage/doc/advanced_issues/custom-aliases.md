# 配置命令别名 - alias 总结

打开 .bashrc，发现：  

```
# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
```

所以，假如要配置仅对个人生效的 alias, 将命令别名写入 ~/.bash_aliases 文件就可以了。  

假如要针对所有人生效的 alias, 将命令别名写入 /etc/profile 文件的结尾即可.  

最后要想使命令生效, 需要重新读取配置文件, 使用 source 命令.  

```bash
source ~/.bashrc
# 或 
source /etc/profile
```
