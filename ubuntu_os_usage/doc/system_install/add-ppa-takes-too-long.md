# PPA 源添加的时间很长 

执行下面类似的命令时会花费很长时间.   

```bash
sudo add-apt-repository ppa:noobslab/icons
```

SOLVED - I disabled temporarily IPv6 system-wide   

It seems to be a DNS routing issue. I was able to use the hotspot on my phone to troubleshoot and the problems went away.  

```bash
sudo sysctl net.ipv6.conf.all.disable_ipv6=1
```

disables IPv6 until reboot.  
