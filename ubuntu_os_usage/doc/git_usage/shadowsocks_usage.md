# 自建 ss/ssr (shadowsocks) 服务器教程  

> ss免费账号: https://gitlab.com/Alvin9999/free/wikis/ss%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7  

> https://gitlab.com/Alvin9999/free/wikis/%E8%87%AA%E5%BB%BAss%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B  

> 自由上网方法: https://github.com/Alvin9999/new-pac/wiki  

自建 ss/ssr 教程很简单, 整个教程分三步: 

- 第一步: 购买 VPS 服务器  

- 第二步: 一键部署 VPS 服务器  

- 第三步: 一键加速 VPS 服务器  


## 第一步: 购买 VPS 服务器

VPS 服务器需要选择国外的, 首选国际知名的 vultr, 速度不错、稳定且性价比高, 按小时计费, 能够随时开通和删除服务器, 新服务器即是新ip.  

vultr 注册地址: https://www.vultr.com/?ref=7777564-4F  (vultr 2019 年 1 月的活动, 新用户赠送 50 美元, 有效期1个月.  全球 15 个服务器位置可选, kvm 框架.  如果以后这个 vultr 注册地址被墙了, 那么就用翻墙软件打开, 或者用 ss/ssr 免费账号)   

虽然是英文界面, 但是现在的浏览器都有网页翻译功能, 鼠标点击右键, 选择网页翻译即可翻译成中文.    

注册并邮件激活账号, 充值后即可购买服务器.  充值方式是支持支付宝, vultr 提供的服务器套餐如下:  

- 2.5 美元/月的服务器配置信息: 单核 512M内存 20G SSD硬盘 带宽峰值100M 500G流量/月 (不推荐, 仅提供ipv6 ip)  
- 3.5 美元/月的服务器配置信息: 单核 512M内存 20G SSD硬盘 带宽峰值100M 500G流量/月 (推荐)  
- 5  美元/月的服务器配置信息:  单核 1G内存 25G SSD硬盘 带宽峰值100M 1000G流量/月 (推荐)  
- 10 美元/月的服务器配置信息:  单核 2G内存 40G SSD硬盘 带宽峰值100M 2000G流量/月  
- 20 美元/月的服务器配置信息:  2cpu 4G内存 60G SSD硬盘 带宽峰值100M 3000G流量/月  
- 40 美元/月的服务器配置信息:  4cpu 8G内存 100G SSD硬盘 带宽峰值100M 4000G流量/月  

注意: 2.5 美元套餐只提供 ipv6 ip, 一般的电脑用不了, 所以建议选择 3.5 美元及以上的套餐.  另外, 并非所有地区都有 3.5 美元的套餐, 需要自己去看.  由于资源的短缺, 有的地区有时候有 3.5 美元的套餐, 有时候没有.    

vultr 实际上是折算成小时来计费的, 比如服务器是 5 美元 1 个月, 那么每小时收费为 5/30/24=0.0069 美元 会自动从账号中扣费, 只要保证账号有钱即可.  如果你部署的服务器实测后速度不理想, 你可以把它删掉 (destroy) , 重新换个地区的服务器来部署, 方便且实用.  因为新的服务器就是新的 ip, 所以当 ip 被墙时这个方法很有用.  当 ip 被墙时, 为了保证新开的服务器 ip 和原先的 ip 不一样, 先开新服务器, 开好后再删除旧服务器即可.    

计费从你开通服务器开始算的, 不管你有没有使用, 即使服务器处于关机状态仍然会计费, 如果你没有开通服务器就不算.  比如你今天早上开通了服务器, 但你有事情, 晚上才部署, 那么这段时间是会计费的.  同理, 如果你早上删掉服务器, 第二天才开通新的服务器, 那么这段时间是不会计费的.  在账号的 Billing 选项里可以看到账户余额.    

温馨提醒: 同样的服务器位置, 不同的宽带类型和地区所搭建的账号的翻墙速度会不同, 这与中国电信、中国联通、中国移动国际出口带宽和线路不同有关, 所以以实测为准.  可以先选定一个服务器位置来按照教程进行搭建, 熟悉搭建方法, 当账号搭建完成并进行了bbr加速后, 测试下速度自己是否满意, 如果满意那就用这个服务器位置的服务器.  如果速度不太满意, 就一次性开几台不同的服务器位置的服务器, 然后按照同样的方法来进行搭建并测试, 选择最优的, 之后把其它的服务器删掉, 按小时计费测试成本可以忽略.  

账号充值如图:   

![](https://raw.githubusercontent.com/magic428/work_note/master/ubuntu_os_usage/doc/git_usage/snapshots/payment.png)  

开通服务器步骤如图:   

![](https://raw.githubusercontent.com/magic428/work_note/master/ubuntu_os_usage/doc/git_usage/snapshots/deploy-1.png)  
![](https://raw.githubusercontent.com/magic428/work_note/master/ubuntu_os_usage/doc/git_usage/snapshots/deploy-2.png)  
![](https://raw.githubusercontent.com/magic428/work_note/master/ubuntu_os_usage/doc/git_usage/snapshots/deploy-3.png)  

点击图中的 CentOS 几个字, 会弹出 centos6, 然后选中 centos6！  (不要选默认的 centos8, 脚本不支持 centos8！) 
开通服务器时, 当出现了 ip, 不要立马去 ping 或者用 xshell 去连接, 再等 5 分钟之后, 有个缓冲时间.  完成购买后, 找到系统的密码记下来, 部署服务器时需要用到.  vps 系统 (推荐 centos6) 的密码获取方法如下图:   

![](https://raw.githubusercontent.com/magic428/work_note/master/ubuntu_os_usage/doc/git_usage/snapshots/server_details.png)  

一个被墙 ip 的 vps 被删掉后, 其 ip 并不会消失, 会随机分配给下一个在这个服务器位置新建服务器的人, 这就是为什么开新服务器会有一定几率开到被墙的 ip.  被墙是指在国内地区无法 ping 通服务器, 但在国外是可以 ping 通的, vultr 是面向全球服务, 如果这个被墙 ip 被国外的人开到了, 它是可以被正常使用的, 半年或1年后这个被墙的 ip 可能会被国内防火墙解封, 那么这就是一个良性循环.    

## 第二步: 部署 VPS 服务器  

购买服务器后, 需要部署一下.  因为你买的是虚拟东西, 而且又远在国外, 我们可以使用 Xshell 或者 cmder 来远程部署.  Xshell windows 版下载地址:   

国外云盘下载: http://108.61.224.82/lib5/Xshell_setup_wm.exe

如果你是苹果电脑操作系统, 更简单, 无需下载 xshell, 系统可以直接连接 VPS.  打开终端 (Terminal) , 输入 ssh root@ip 其中“ip”替换成你 VPS 的 ip, 按回车键, 然后复制粘贴密码, 按回车键即可登录.  粘贴密码时有可能不显示密码, 但不影响正常登陆.  

xshell 的使用方法:  

- 下载 windows xshell 软件并安装后, 打开软件;  
- 选择 文件 | 新建, 随便取个名字, 然后把你的服务器 ip 填上;  
- 连接国外 ip 即服务器时, 软件会先后提醒你输入用户名和密码, 用户名默认都是 root, 密码是你购买的服务器系统的密码;  

如果 xshell 连不上服务器, 没有弹出让你输入用户名和密码的输入框, 表明你开到的 ip 是一个被墙的 ip, 遇到这种情况, 重新开新的服务器, 直到能用 xshell 连上为止, 耐心点哦！如果同一个地区开了多台服务器还是不行的话, 可以换其它地区.    

连接成功后, 会出现登陆成功信息, 之后就可以复制粘贴代码部署了.  

### 2.1 ShadowsocksR一键部署管理脚本  

> CentOS 6/7, Debian 6+ 和 Ubuntu 14+ 

1) 脚本一 (2018.11.20 更新)  

```bash
yum -y install wget

wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubi/doubi/master/ssr.sh && chmod +x ssr.sh && bash ssr.sh
```

2) 备用脚本二 (2018.11.21更新)  

如果上面的脚本暂时用不了, 可以用下面的备用脚本, 备用脚本没有单独做图文教程, 自己摸索下就会了.  

```
yum -y install wget

wget --no-check-certificate https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocksR.sh

chmod +x shadowsocksR.sh

./shadowsocksR.sh 2>&1 | tee shadowsocksR.log
```

备用脚本卸载命令:   

```bash
./shadowsocksR.sh uninstall
```

如果提示 `wget: command not found` 的错误, 这是你的系统精简的太干净了, wget 都没有安装, 所以需要安装 wget.  CentOS系统安装 wget 命令: `yum install -y wget` Debian/Ubuntu 系统安装wget命令: `apt-get install -y wget`.  


复制上面的脚本一代码到 VPS 服务器里, 复制代码用鼠标右键的复制, 然后在 vps 里面右键粘贴进去, 因为 ctrl+c 和 ctrl+v 无效.  接着按回车键, 脚本会自动安装, 以后只需要运行这个快捷命令就可以出现下图的界面进行设置, 快捷管理命令为:    

```bash
bash ssr.sh
```

![](https://raw.githubusercontent.com/magic428/work_note/master/ubuntu_os_usage/doc/git_usage/snapshots/install_ss-1.png)  

如上图出现管理界面后, 输入数字 1 来安装 SSR 服务端.  如果输入 1 后不能进入下一步, 那么请退出 xshell, 重新连接 vps 服务器, 然后输入快捷管理命令 bash ssr.sh 再尝试.    

依次输入自己想设置的端口和密码 (密码建议用复杂点的字母组合, 端口号为40-65535之间的数字), 回车键用于确认   

注: 关于端口的设置, 总的网络总端口有 6 万多个, 理论上可以任意设置, 但不要以 0 开头！但是有的地区需要设置特殊的端口才有效, 一些特殊的端口比如 80、143、443、1433、3306、3389、8080.   这里设置为 443.  

选择想设置的加密方式, 比如 10, 按回车键确认;   

接下来是选择协议插件为 auth_sha1_v4, 选择并确认后, 会提示你是否选择兼容原版, 这里的原版指的是 SS 客户端 (SS 客户端没有协议和混淆的选项) , 可以根据需求进行选择, 演示选择 y.   

之后进行混淆插件的设置.  注意: 如果协议是 origin, 那么混淆也必须是 plain；如果协议不是 origin, 那么混淆可以是任意的.  有的地区需要把混淆设置成 plain 才好用.  因为混淆不总是有效果, 要看各地区的策略, 有时候不混淆 (plain) 或者 (origin 和 plain 一起使用) , 让其看起来像随机数据更好.   (特别注意: tls 1.2_ticket_auth 容易受到干扰！请选择除 tls 开头以外的其它混淆！！！)   

进行混淆插件的设置后, 会依次提示你对设备数、单线程限速和端口总限速进行设置, 默认值是不进行限制, 个人使用的话, 选择默认即可, 即直接敲回车键.    
 
注意: 关于限制设备数, 这个协议必须是非原版且不兼容原版才有效, 也就是必须使用 SSR 协议的情况下, 才有效！  

之后输入: y 代码就正式自动部署了.  

耐心等待一会即可部署完成, 然后会打印出刚刚设置好的 SSR 的账号信息, 包括 IP、端口、密码、加密方式、协议插件、混淆插件, 之后 SSR 客户端会需要填入这些信息.  提醒一下: 二维码链接地址由于域名失效不可用, 所以部署好的账号需要自己在客户端里面手动填写信息.    

如果之后想修改账号信息, 直接输入快捷管理命令: `bash ssr.sh` 进入管理界面, 选择相应的数字来进行一键修改.   

至此, 脚本演示结束.    

此脚本是开机自动启动, 部署一次即可.  最后可以重启服务器确保部署生效 (一般情况不重启也可以) .  重启需要在命令栏里输入reboot , 输入命令后稍微等待一会服务器就会自动重启, 一般重启过程需要 2~5 分钟, 重启过程中 Xshell 会自动断开连接, 等VPS 重启好后才可以用 Xshell 软件进行连接.  如果部署过程中卡在某个位置超过 10 分钟, 可以用xshell软件断开, 然后重新连接你的 ip, 再复制代码进行部署.    

## 第三步: 一键加速 VPS 服务器

总共有 2 种加速方法, 锐速加速和 bbr 加速, 选择第 1 种 - 锐速加速.  

### 3.1 破解版锐速加速教程 

此加速教程为破解版锐速加速, Vultr 的服务器 centos6 系统官方进行了更新, 导致目前不支持 BBR 的部署, 但锐速应该是可以部署的, 故增加了此部署脚本, 加速后对速度的提升很明显, 所以推荐部署加速脚本.  该加速方法是开机自动启动, 部署一次就可以了.    

1) 第一步, 先更换服务器内核 (脚本只支持 centos 系统, 其它系统可以直接尝试第二步)   

```bash
yum -y install wget
wget --no-check-certificate https://blog.asuhu.com/sh/ruisu.sh && bash ruisu.sh
```

不动的时候敲回车键, 因为是进行内核更新, 所以需要多等一会儿.  

已成功替换内核后会提示 5 秒后服务器自动重启, 2 分钟后可以重新连接服务器, 连上后开始第二步的操作.    

2) 第二步, 一键安装锐速  

```bash
wget -N --no-check-certificate https://raw.githubusercontent.com/91yun/serverspeeder/master/serverspeeder-all.sh && bash serverspeeder-all.sh
```

卸载加速代码命令为:   

```bash
chattr -i /serverspeeder/etc/apx* && /serverspeeder/bin/serverSpeeder.sh uninstall -f
```

但有些内核是不适合的, 部署过程中需要手动选择推荐的, 当部署时提示没有完全匹配的内核,随便选一个内核就行,按照提示来输入数字, 按回车键即可.  

锐速安装成功标志如下:   

![](https://raw.githubusercontent.com/magic428/work_note/master/ubuntu_os_usage/doc/git_usage/snapshots/server_accelerate_success.png)  

出现 running 字样即可!  

## 3. SSR 客户端下载

第一次电脑系统使用 SSR/SS 客户端时, 如果提示你需要安装 NET Framework 4.0, 网上搜一下这个东西, 安装一下即可.  NET Framework 4.0 是 SSR/SS 的运行库, 没有这个 SSR/SS 客户端无法正常运行.  有的电脑系统可能会自带 NET Framework 4.0.  

Windows SSR 客户端: https://github.com/shadowsocksr-backup/shadowsocksr-csharp/releases  

Mac SSR 客户端: https://github.com/shadowsocksr-backup/ShadowsocksX-NG/releases  

Linux 客户端一键安装配置使用脚本 (使用方法见注释): https://github.com/the0demiurge/CharlesScripts/blob/master/charles/bin/ssr  

安卓 SSR 客户端: https://github.com/shadowsocksr-backup/shadowsocksr-android/releases/download/3.4.0.8/shadowsocksr-release.apk  

iOS: 目前大陆 App Store 商店很多 SS/SSR 软件都被下架了, 我们需要美区的 ID, 然后到美区的商店就可以自由下载软件了.  关于美区 ID 的申请方法网上有很多, 可以自己搜一下.  如果不想自己注册, 可以去淘宝购买或者网上找别人共享的 ID.  SS/SSR 软件有很多, 比如: Potatso Lite、Potatso、wingy 等.  或者用爱思助手 PC 端安装 Shadowrocket 的 ipa 文件, Shadowrocket IPA 文件下载及教程地址: https://github.com/gfw-breaker/guides/wiki/iPhone%E4%BD%BF%E7%94%A8Shadowsocks%E7%BF%BB%E5%A2%99.    

有了账号后, 打开 SSR 客户端, 填上信息, 这里以 windows 版的 SSR 客户端为例子:   

![](https://raw.githubusercontent.com/magic428/work_note/master/ubuntu_os_usage/doc/git_usage/snapshots/login_ssr.png)  

在对应的位置, 填上服务器 ip、服务器端口、密码、加密方式、协议和混淆, 最后将浏览器的代理设置为 (http) 127.0.0.1和1080 即可.  账号的端口号就是你自己设置的, 而要上网的浏览器的端口号是 1080, 固定的, 谷歌浏览器可以通过 SwitchyOmega 插件来设置.  

启动 SSR 客户端后, 右键 SSR 客户端图标, 选择第一个“系统代理模式”, 里面有 3 个子选项, 选择"全局模式“, 之后就可以用浏览器设置好了的代理模式 (http) 127.0.0.1 和 1080 翻墙, 此模式下所有的网站都会走 SSR 代理.    

![](https://raw.githubusercontent.com/magic428/work_note/master/ubuntu_os_usage/doc/git_usage/snapshots/ssr-client.png)  

## 常见问题参考解决方法  

1、用了一段时间发现ssr账号用不了了?  

首先ping一下自己的ip, 看看能不能ping的通, ping不通那么就是ip被墙了, ip被墙时, xshell也会连接不上服务器, 遇到这种情况重新部署一个新的服务器, 新的服务器就是新的ip.  关于怎么ping ip的方法, 可以自行网上搜索, 或者用xshell软件连接服务器来判断, 连不上即是被墙了.  vultr开通和删除服务器非常方便, 新服务器即新ip, 大多数vps服务商都没有这样的服务, 一般的vps服务商可能会提供免费更换1次ip的服务.  

当外部网络环境封锁很严重的时候, 如果你的ip没有被墙, 那么有可能是端口被封了, 所以可以换端口, 5位数的端口优先考虑.  加密方式也可以更换.  

2、刚搭建好的ssr账号, ip能ping通, 但是还是用不了?  

首选排除杀毒软件的干扰, 尤其是国产杀毒软件, 比如360安全卫生、360杀毒软件、腾讯管家、金山卫生等.  这些东西很容易干扰翻墙上网, 如果你的电脑安装了这样的东西, 建议至少翻墙时别用, 最好卸载.  其次, 检查下SSR信息是否填写正确.  浏览器的代理方式是否是ssr代理, 即 (HTTP) 127.0.0.1 和1080.  如果以上条件都排除, 还是用不了, 那么可以更换端口、加密方式、协议、混淆, 或者更换服务器位置.  另外, 如果你的vps服务器配置的是SSR账号, 即有协议和混淆且没有兼容原版(SS版) , 那么你必须使用SSSR客户端来使用账号, 因为SS客户端没有填写协议和混淆的选项.  

3、有的地区需要把混淆参数设置成plain才好用.  因为混淆不总是有效果, 要看各地区的策略, 有时候不混淆 (plain) 让其看起来像随机数据更好.  

4、电脑能用但手机用不了?  

如果你的手机用的是SS客户端, SS客户端没有填协议和混淆的地方, 如果你部署的协议和混淆的时候没有选择兼容原版 (SS版) , 因此手机是用不了的.  这个时候你把协议弄成兼容原版、混淆也设置成兼容原版即可.  或者直接将协议设置成origin且混淆设置成plain.  

5、vps的服务器操作系统不要用的太高, 太高可能会因为系统的防火墙问题导致搭建的SSR账号连不上.  如果某个系统不好用, 可以选择其它的系统来尝试.  

6、vultr服务商提供的vps服务器是单向流量计算, 有的vps服务商是双向流量计算, 单向流量计算对于用户来说更实惠.  因为我们是在vps服务器上部署SSR服务端后, 再用SSR客户端翻墙, 所以SSR服务端就相当于中转, 比如我们看一个视频, 必然会产生流量, 假如消耗流量80M, 那么VPS服务器会产生上传80M和下载80M流量, vultr服务商只计算单向的80M流量.  如果是双向计算流量, 那么会计算为160M流量.  

7、如果你想把搭建的账号给多人使用, 不用额外设置端口, 因为一个账号就可以多人使用.  一般5美元的服务器可以同时支持40人在线使用.  

如果想实现支持每个用户(端口)不同的加密方式/协议/混淆等, 并且管理流量使用, 可以参考多用户配置脚本:  

```bash
wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubi/doubi/master/ssrmu.sh && chmod +x ssrmu.sh && bash ssrmu.sh
# 安装后管理命令为: 
bash ssrmu.sh
```

注意: 这个多用户配置脚本和教程内容的脚本无法共存！要想用这个脚本, 把之前的脚本卸载, 输入管理命令`bash ssr.sh` , 选择3, 卸载 ShadowsocksR 即可卸载原脚本.  

8、vultr 服务器每月有流量限制, 超过限制后服务器不会被停止运行, 但是超出的流量会被额外收费.  北美和西欧地区的服务器超出流量后, 多出的部分收费为 0.01 美元/G.  新加坡和日本东京 (日本) 为 0.025 美元/G, 悉尼 (澳大利亚) 为 0.05 美元/G.  **把 vultr 服务器删掉, 开通新的服务器, 流量会从 0 开始重新计算**.  

9、vultr 怎样才能申请退款呢?  

vultr 和其他的国外商家一样, 都是使用工单的形式与客服联系, 如果需要退款, 直接在后台点击 support, 选择 open ticket 新开一个工单, 选择 billing question 财务问题, 简单的在文本框输入你的退款理由.  比如: Please refund all the balance in my account.  工单提交以后一般很快就可以给你确认退款, 若干个工作日后就会退回你的支付方式. (全额退款结束后, 账号可能会被删除) 

如果英语水平不好, 但是想和客服进行交流, 可以用百度在线翻译, 自动中文转英文和英文转中文.  

10、路由器也可以配置 ss/ssr 账号, 详见 openwrt-ssr 项目地址: https://github.com/ywb94/openwrt-ssr

11、如果电脑想用搭建的 ss/ssr 账号玩游戏, 即实现类似 VPN 全局代理, 可以用 SSTAP, 具体方法可以网上搜索.  

12、配置 bbr 加速脚本, 重启电脑后 xshell 无法连接服务器.  如果你遇到这样的问题, 只能把服务器删除了, 重新搭建个新的, 可以先配置 bbr 加速脚本再配置 ss/ssr 脚本.  

# 参考资料  

[1] https://github.com/Alvin9999/new-pac/wiki/%E8%87%AA%E5%BB%BAss%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B  
