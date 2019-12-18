# ROS Melodic 环境搭建
 
> Ubuntu 18.04  
> ROS Melodic 官网：http://wiki.ros.org/melodic/Installation/Ubuntu  

## 1. 配置软件安装源   

1) 配置 Ubuntu 的软件更新的资源库："restricted"，"universe"和"multiverse";  

2) 使用下面命令添加软件下载源.  

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

## 2. 设置 keys

为了处理最近一起安全事件，旧密钥已被撤销。所以在执行 apt-get update 时会提示密钥错误，更换密钥即可。  
新的密钥和旧的密钥如下:

old key: 421C365BD9FF1F717815A3895523BAEEB01FA116
new key: C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

```bash
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```

如果无法连接上述服务器，可以尝试 hkp://pgp.mit.edu:80 或者 hkp://keyserver.ubuntu.com:80.  

```bash
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```

首先要删除旧的密钥：  

sudo apt-key del 421C365BD9FF1F717815A3895523BAEEB01FA116  

## 3. 安装

```bash
$ sudo apt-get update
```

如果源在更新的时候出现问题, 可以尝试下面的原地址:  

```
sudo sh -c '. /etc/lsb-release && echo "deb http://mirrors.ustc.edu.cn/ros/ubuntu/ $DISTRIB_CODENAME main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```

```bash
sudo apt-get install ros-melodic-desktop
```

注意不要安装 full 版，Gazebo2 不能与更新版本的 Gazebo 共存，需要单独安装所需功能包即可。  
然后，安装 ros-gazebo 接口库等，以 7 为例如下:    

```
sudo apt-get install ros-melodic-gazebo7-  
```

安装完毕后, ROS (melodic) 就可以和 Gazebo7 一起使用了。

**安装功能包**:  

```bash
sudo apt-get install ros-melodic-PACKAGE

# 例如:  
sudo apt-get install ros-melodic-slam-gmapping
```

**如果不知道确切的 ros 包名, 可以使用下面的命令查找在 melodic 中可以使用的功能包**:  

```bash
apt-cache search ros-melodic
```

## 4. 初始化 rosdep  

在使用 ROS 之前必须要初始化 rosdep.  

```bash
sudo rosdep init && rosdep update
```

输出信息如下:   

```bash
reading in sources list data from /etc/ros/rosdep/sources.list.d
Hit https://raw.githubusercontent.com/ros/rosdistro/master/rosdep/osx-homebrew.yaml
Hit https://raw.githubusercontent.com/ros/rosdistro/master/rosdep/base.yaml
Hit https://raw.githubusercontent.com/ros/rosdistro/master/rosdep/python.yaml
Hit https://raw.githubusercontent.com/ros/rosdistro/master/rosdep/ruby.yaml
Hit https://raw.githubusercontent.com/ros/rosdistro/master/releases/fuerte.yaml
Query rosdistro index https://raw.githubusercontent.com/ros/rosdistro/master/index-v4.yaml
Skip end-of-life distro "ardent"
Skip end-of-life distro "bouncy"
Add distro "crystal"
Add distro "dashing"
Add distro "eloquent"
Skip end-of-life distro "groovy"
Skip end-of-life distro "hydro"
Skip end-of-life distro "indigo"
Skip end-of-life distro "jade"
Add distro "kinetic"
Skip end-of-life distro "lunar"
Add distro "melodic"
Add distro "noetic"
updated cache in /home/magic/.ros/rosdep/sources.cache
```

## 5. 配置 ROS 启动环境

```bash
$ echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
```

注意当安装多个ROS发行版，使用 melodic 需要用到下面命令:  

```bash
$ source /opt/ros/melodic/setup.bash
```

## 6. 安装 building package 的依赖包

```bash
sudo apt-get install python-rosinstall python-rosinstall-generator python-wstool build-essential
```

## 7. 测试 roscore 是否安装成功

1) 打开 Termial，输入以下命令，初始化ROS环境:  

```bash
roscore
```

2) 打开新的 Termial，输入以下命令，弹出一个小乌龟窗口:  

```bash
rosrun turtlesim turtlesim_node
```

3) 打开新的 Termial，输入以下命令，可以在 Termial 中通过方向键控制小乌龟的移动:  

```bash
rosrun turtlesim turtle_teleop_key
```

4) 打开新的 Termial，输入以下命令，弹出新的窗口查看 ROS 节点信息:  

```bash
rosrun rqt_graph rqt_graph
```
