

端口设置为 8000:80 最为合理, 因为其访问的默认设置端口就是8000

如果没有进行域名映射,应该将 SEAFILE_SERVER_HOSTNAME=192.168.1.32 设置为本地 ip 地址.  

上传文件需要开放: 8080:8080 8082:8082 端口


sudo docker-compose up -d
sudo docker-compose stop

**切记不能使用 docker-compose down!!!**   


添加开机启动:  

sudo vi  /etc/rc.local 

在文件中的 exit 0 之前添加下面的命令:  

```bash
# seafile
docker-compose -f /home/magic/Downloads/docker-compose.yml up -d 
```


注意, 不能将 docker-compose.yml 文件复制到其他目录后使用, 除非你新建一个 docker container.  


容器及云盘文件的备份


容器的使用方法.   

