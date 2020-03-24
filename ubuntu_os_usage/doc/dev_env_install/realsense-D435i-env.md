# Realsense D435i 深度相机环境搭建 

- Realsense D435i 在 ubuntu 上安装 SDK 与 ROS Wrapper;  
- 运行 ORB-SLAM2、RTAB 和 VINS-Mono.

sudo apt-get install ros-kinetic-cv-bridge ros-kinetic-tf ros-kinetic-message-filters ros-kinetic-image-transport

## 前言

D435i 相机正面有四个圆孔，从左向右，第一和第三个是红外传感器（IR Stereo Cameral）；第二个是红外激光发射器（IR Projector），第四个是彩色相机（色彩传感器）。  

D435i 在 D435 的基础上, 另外搭载了博世的惯性测量单元（IMU）, 可以作为研究 VIO 及其他 SLAM 算法的良好传感器组. 本文将介绍自己一步步搭建 D435i 环境, 并成功跑通ORB-SLAM2、RTAB和VINS-Mono的过程, 供大家参考.   

安装环境  

- 系统: ubuntu 18.04 内核 5.0.0-23-generic   
- ROS: Melodic  
- 传感器: intel realsense D435i   

环境上已经成功搭建并使用 dateset 跑过 ORB-SLAM2、VINS-Mono 与 RTAB.   

## 1. 安装 Realsense SDK

github: https://github.com/IntelRealSense/librealsense  

安装可以参考文档: https://github.com/IntelRealSense/librealsense/blob/master/doc/installation.md  

1、下载 source  

```bash
git clone https://github.com/IntelRealSense/librealsense
cd librealsense/
```

2、安装依赖项  

```bash
sudo apt-get install libudev-dev pkg-config libgtk-3-dev libusb-1.0-0-dev pkg-config libglfw3-dev libssl-dev
```

3 安装 Realsense 设备权限脚本文件  

该文件位于 librealsense 源码目录内.  

```bash
sudo cp config/99-realsense-libusb.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && udevadm trigger 
```

4、为 realsense 构建内核补丁模块.  

脚本会根据不同的 ubuntu 版本 (Ubuntu 14/16/18 LTS) 安装内核模块:  

注意, 这一步需要把 realsense 相机拔下来.    

```bash
./scripts/patch-realsense-ubuntu-lts.sh
```

安装完成后打印消息如下:  

```bash
Reading package lists... Done
Building dependency tree       
Reading state information... Done
bc is already the newest version (1.07.1-2).
build-essential is already the newest version (12.4ubuntu1).
git is already the newest version (1:2.17.1-1ubuntu0.4).
linux-headers-generic is already the newest version (4.15.0.68.70).
0 upgraded, 0 newly installed, 0 to remove and 150 not upgraded.
Package required libusb-1.0-0-dev:  - found
Package required libssl-dev:  - found
Create patches workspace in ubuntu-bionic-hwe folder

Package required libelf-dev:  - found
Package required elfutils:  - found
Package required bison:  - found
Package required flex:  - found
Cloning into './ubuntu-bionic-hwe'...
...

Patched kernels modules were created successfully

Replacing videodev  -
	Applying the patched module ...  succeeded
Replacing uvcvideo  -
	Applying the patched module ...  succeeded
Replacing hid_sensor_accel_3d  -
	Applying the patched module ...  succeeded
Replacing hid_sensor_gyro_3d  -
	Applying the patched module ...  succeeded

Script has completed. Please consult the installation guide for further instruction.
```

使用下面的命令可以查看 UVC 是否安装成功了.  

```bash
sudo dmesg | tail -n 50

[28215.093013] usbcore: deregistering interface driver uvcvideo
[28215.585837] media: Linux media interface: v0.10
[28215.598429] videodev: Linux video capture interface: v2.00
[28215.653726] uvcvideo: Found UVC 1.00 device Integrated_Webcam_HD (0bda:565a)
[28215.659452] uvcvideo 1-5:1.0: Entity type for entity Realtek Extended Controls Unit was not initialized!
[28215.659454] uvcvideo 1-5:1.0: Entity type for entity Extension 4 was not initialized!
[28215.659455] uvcvideo 1-5:1.0: Entity type for entity Extension 7 was not initialized!
[28215.659456] uvcvideo 1-5:1.0: Entity type for entity Processing 2 was not initialized!
[28215.659458] uvcvideo 1-5:1.0: Entity type for entity Camera 1 was not initialized!
[28215.659631] input: Integrated_Webcam_HD: Integrate as /devices/pci0000:00/0000:00:14.0/usb1/1-5/1-5:1.0/input/input34
[28215.659812] usbcore: registered new interface driver uvcvideo
[28215.659813] USB Video Class driver (1.1.1)
```

插上 realsense 相机之后打印信息如下:  

```bash
[28483.882956] sd 1:0:0:0: [sda] Synchronizing SCSI cache
[28484.137010] sd 1:0:0:0: [sda] Synchronize Cache(10) failed: Result: hostbyte=DID_ERROR driverbyte=DRIVER_OK
[28484.293130] usb 2-2: USB disconnect, device number 2
[28495.465864] usb 2-2: new SuperSpeed Gen 1 USB device number 4 using xhci_hcd
[28495.486779] usb 2-2: New USB device found, idVendor=8086, idProduct=0b3a, bcdDevice=50.bb
[28495.486784] usb 2-2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[28495.486787] usb 2-2: Product: Intel(R) RealSense(TM) Depth Camera 435i
[28495.486790] usb 2-2: Manufacturer: Intel(R) RealSense(TM) Depth Camera 435i
[28495.486792] usb 2-2: SerialNumber: 915323050719
[28495.491315] uvcvideo: Found UVC 1.50 device Intel(R) RealSense(TM) Depth Camera 435i (8086:0b3a)
[28495.494739] uvcvideo: Unable to create debugfs 2-4 directory.
[28495.495033] uvcvideo 2-2:1.0: Entity type for entity Intel(R) RealSense(TM) Depth Ca was not initialized!
[28495.495038] uvcvideo 2-2:1.0: Entity type for entity Processing 2 was not initialized!
[28495.495041] uvcvideo 2-2:1.0: Entity type for entity Camera 1 was not initialized!
[28495.495197] input: Intel(R) RealSense(TM) Depth Ca as /devices/pci0000:00/0000:00:14.0/usb2/2-2/2-2:1.0/input/input35
[28495.495966] uvcvideo: Found UVC 1.50 device Intel(R) RealSense(TM) Depth Camera 435i (8086:0b3a)
[28495.498177] uvcvideo: Unable to create debugfs 2-4 directory.
[28495.498462] uvcvideo 2-2:1.3: Entity type for entity Processing 7 was not initialized!
[28495.498466] uvcvideo 2-2:1.3: Entity type for entity Extension 8 was not initialized!
[28495.498469] uvcvideo 2-2:1.3: Entity type for entity Camera 6 was not initialized!
[28495.621590] hid-sensor-hub 0003:8086:0B3A.0008: No report with id 0xffffffff found
```

5、基于 cmake 的编译 librealsense SDK 库.  

前面的都是准备工作, 到这里才真正的开始编译 librealsense sdk.  

```bash
mkdir build
cd build
cmake ../ -DBUILD_EXAMPLES=true -DBUILD_PYTHON_BINDINGS:bool=true
make -j8
sudo make install
```

`-DBUILD_EXAMPLES=true` 表示这个选项表示带演示和教程的.  

安装的输出信息如下:  

```bash
Install the project...
-- Installing: /usr/local/lib/librealsense2.so.2.28.0
-- Installing: /usr/local/lib/librealsense2.so
-- Installing: /usr/local/include/librealsense2
-- Installing: /usr/local/include/librealsense2/rs_advanced_mode.h
-- Installing: /usr/local/include/librealsense2/hpp
-- Installing: /usr/local/include/librealsense2/hpp/rs_types.hpp
-- Installing: /usr/local/lib/librealsense2-gl.so
-- Installing: /usr/local/lib/cmake/realsense2/realsense2-glTargets.cmake
-- Installing: /usr/local/lib/cmake/realsense2/realsense2-glTargets-noconfig.cmake
-- Installing: /usr/local/lib/cmake/realsense2/realsense2-glConfig.cmake
-- Installing: /usr/local/lib/cmake/realsense2/realsense2-glConfigVersion.cmake
-- Installing: /usr/local/lib/pkgconfig/realsense2-gl.pc
-- Installing: /usr/local/bin/rs-hello-realsense
-- Installing: /usr/local/bin/rs-software-device
-- Installing: /usr/local/bin/rs-capture
-- Installing: /usr/local/lib/libfw.a
-- Installing: /usr/local/lib/libtm.a
-- Installing: /usr/local/lib/libuvc_fw.a
```

6、进入 librealsense/build/examples/capture, 试一下效果.  

```bash
./rs-capture 
```

致此, librealsense SDK.  

## 2. 安装 ROS Wrapper  

直接按照 github 上的教程 (https://github.com/intel-ros/realsense) 安装即可:  

1) 安装依赖包  

```bash
sudo apt-get install ros-melodic-ddynamic-reconfigure ros-melodic-rgbd-launch
```

2) 建立 workspace, 已经有的可以跳过  

```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src/
catkin_init_workspace 
cd ..
catkin_make
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

3) 下载源程序到 ~/catkin_ws/src 目录  

```bash
cd ~/catkin_ws/src
git clone https://github.com/intel-ros/realsense.git  
```

4) 开始编译  

```bash
cd ..
catkin_make
```

5) 如果没有错误说明, 已经安装好了. 可以启动相机节点:  

```bash
$ roslaunch realsense2_camera rs_rgbd.launch

started roslaunch server http://G7:46125/

SUMMARY
========

PARAMETERS
 * /camera/realsense2_camera/accel_fps: 250
 * /camera/realsense2_camera/accel_frame_id: camera_accel_frame
 ...
 * /camera/realsense2_camera/unite_imu_method: none
 * /camera/realsense2_camera/usb_port_id: 
 * /rosdistro: melodic
 * /rosversion: 1.14.3

[ INFO] [1573204811.743764205]: Initializing nodelet with 12 worker threads.
[ INFO] [1573204811.892224246]: RealSense ROS v2.2.9
[ INFO] [1573204811.892255078]: Running with LibRealSense v2.30.0
[ INFO] [1573204813.093866071]: RealSense Node Is Up!
```

6) 看一下发布的 topic  

```bash
$ rostopic list

/camera/accel/imu_info
/camera/accel/sample
/camera/aligned_depth_to_color/camera_info
/camera/aligned_depth_to_color/image_raw
/camera/aligned_depth_to_infra1/camera_info
/camera/aligned_depth_to_infra1/image_raw
/camera/color/camera_info
/camera/color/image_raw
/camera/color/image_rect_color
/camera/color_rectify_color/parameter_descriptions
/camera/color_rectify_color/parameter_updates
/camera/depth/camera_info
/camera/depth/image_rect_raw
/camera/depth_registered/points
/camera/extrinsics/depth_to_color
/camera/extrinsics/depth_to_infra1
/camera/extrinsics/depth_to_infra2
/camera/gyro/imu_info
/camera/gyro/sample
/camera/infra1/camera_info
/camera/infra1/image_rect_raw
/camera/infra2/camera_info
/camera/infra2/image_rect_raw
/camera/motion_module/parameter_descriptions
/camera/motion_module/parameter_updates
/camera/realsense2_camera_manager/bond
/camera/rgb_camera/auto_exposure_roi/parameter_descriptions
/camera/rgb_camera/auto_exposure_roi/parameter_updates
/camera/rgb_camera/parameter_descriptions
/camera/rgb_camera/parameter_updates
/camera/stereo_module/auto_exposure_roi/parameter_descriptions
/camera/stereo_module/auto_exposure_roi/parameter_updates
/camera/stereo_module/parameter_descriptions
/camera/stereo_module/parameter_updates
/diagnostics
/rosout
/rosout_agg
/tf
/tf_static
```

7) 打开 RVIZ 看看效果  

通过选取不同的 rostopic, 来观察相机是否正常工作.  

例如 /camera/color/image_raw 和 /camera/depth/image_rect_raw.  

```bash
rqt_image_view
```

8) 内参获取

若不进行标定, 可以先从 Realsense ROS Wrapper 发布的 topic 中获得相机的内参.   

```bash
rostopic echo /camera/color/camera_info 
rostopic echo /camera/aligned_depth_to_color/camera_info
```

解释一下 topic 中所有 aligned_depth_to_color 是指已经将深度信息通过相机到 RGBD 的外参映射到彩色图像上了.  

```bash
header: 
  seq: 0
  stamp: 
    secs: 1573206565
    nsecs: 655053798
  frame_id: "camera_color_optical_frame"
height: 480
width: 640
distortion_model: "plumb_bob"
D: [0.0, 0.0, 0.0, 0.0, 0.0]
K: [613.3822021484375, 0.0, 322.447509765625, 0.0, 613.2175903320312, 232.54379272460938, 0.0, 0.0, 1.0]
R: [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
P: [613.3822021484375, 0.0, 322.447509765625, 0.0, 0.0, 613.2175903320312, 232.54379272460938, 0.0, 0.0, 0.0, 1.0, 0.0]
binning_x: 0
binning_y: 0
roi: 
  x_offset: 0
  y_offset: 0
  height: 0
  width: 0
  do_rectify: False
```

致此, realsense 的 SDK 和 ROS Wrapper 已经安装好了.  

## ORB-SLAM 配置  

1) 源码下载:  

```bash
git clone https://github.com/raulmur/ORB_SLAM2.git
```

2) 在 ORB-SLAM2/Examples/ROS/ORB_SLAM2/src 中修改 ros_rgbd.cc 的 topic 订阅:   

```cpp
message_filters::Subscriber<sensor_msgs::Image> rgb_sub(nh, "/camera/color/image_raw", 1);
message_filters::Subscriber<sensor_msgs::Image> depth_sub(nh, "/camera/aligned_depth_to_color/image_raw", 1);
```

3) 重新编译 ORB-SLAM2

### Building the nodes for mono, monoAR, stereo and RGB-D  

a) 将 *Examples/ROS/ORB_SLAM2* 路径添加到 ROS_PACKAGE_PATH 环境变量中.  

```bash
sudo gedit ~/.bashrc 
# 在文件结尾添加:  
export ROS_PACKAGE_PATH=${ROS_PACKAGE_PATH}:PATH/ORB_SLAM2/Examples/ROS
```

将其中的  PATH 替换为 git clone 代码时所在的路径.  

b) 编译 ORB_SLAM.so 和 ROS 包  

```bash
chmod +x build.sh
./build.sh

chmod +x build_ros.sh
./build_ros.sh
```

4) 连接 realsense  D435i , 启动 ROS realsense2_camera:   

```bash
roslaunch realsense2_camera rs_rgbd.launch
```

5) 先用 TUM1.yaml 的参数运行一下试试看:   

```bash
rosrun ORB_SLAM2 RGBD Vocabulary/ORBvoc.txt Examples/RGB-D/TUM1.yaml 
```

在这里插入图片描述程序正常运行！

6) 修改 yaml 文件中的部分参数再试试看！  

修改后的参数如下:  

```yaml
%YAML:1.0

#--------------------------------------------------------------------------------------------
# Camera Parameters. Adjust them!
#--------------------------------------------------------------------------------------------

# Camera calibration and distortion parameters (OpenCV) 
Camera.fx: 517.306408
Camera.fy: 516.469215
Camera.cx: 318.643040
Camera.cy: 255.313989

Camera.k1: 0
Camera.k2: 0
Camera.p1: 0
Camera.p2: 0
Camera.k3: 0
```

```bash
rosrun ORB_SLAM2 RGBD Vocabulary/ORBvoc.txt Examples/RGB-D/realsense_D435i.yaml 
```

在这里插入图片描述


## ORB_SLAM2 Issues
 
1) error: usleep is not declared in this scope #337  

An easier way is to add #include <unistd.h> in ORB_SLAM2/include/System.h.  

2) /usr/lib/x86_64-linux-gnu/libboost_system.so: error adding symbols: DSO missing from command line
collect2: error: ld returned 1 exit status  

这是因为程序需要链接 boost 库, 但是在编译文件中没有指定.  

3) rgbd_tum.cc:(.text.startup+0x55b): undefined reference to `cv::imread(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int)'  

分两步排查:  
 
- 确定是否显式指定 OpenCV 链接库;  
- 如果指定后仍然报错, 则说明 OpenCV 版本有问题, 需要重新指定其他版本或重新编译;  

有时需要显式指定 OpenCV 头文件的路径, 

include_directories(${OpenCV_INCLUDE_DIRS})


作者：里高
链接：https://www.zhihu.com/question/35116055/answer/97523938
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

ORB里面bug也还是很多，而且过于面向对象了，使得代码反而凌乱。还有些理论上作者理解也有错误，一并在此指出：1. [bug] 初始化如果进入Homography checking，一共有八个数值解，其中两个具有物理意义，在没有先验假设的情况下，是无法区分这两个解对错的。作者假设parallax大的那个为最优解，这是错误的。parallax取决于观察平面的角度，垂直时大（正对着墙），平行时小（行走时平视马路），简单假设大的parallax赢是错误的。正规改法是取第三个frame，三个frame就只有一个物理解。取巧的改法是随机返回两个物理解中的一个，如果不巧是错的，自然tracking不上，重新开始。2. [bug] http://ORBmatcher.cc:478 行，统计方向有误， int bin = round(rot*factor) 改为: int bin = round(rot/(360*factor));3. [bug] Initializer::checkRT : 890, nGood++ 应该在{} 里面：if(cosParallax<0.99998){vbGood[vMatches12[i].first]=true;nGood++;}4. 。。。一些代码可以优化的地方，不算bug，不细说了。其它的就涉及到理论和算法流程，这里不详谈。ORB其实就是PTAM的加强版，最大的价值在于：1.证明了mono vision odometry 可行；2. 证明了orb很适合 mono vision odometry。理论上的突破不大，反而过于复杂了。

作者：庞阿困
链接：https://www.zhihu.com/question/35116055/answer/62001013
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

粘一个综述：ORB-SLAM 基本延续了 PTAM 的算法框架,但对框架中的大部分组件都做了改进, 归纳起来主要有 4 点: 1) ORB-SLAM 选用了 ORB 特征[27], 基于 ORB 描述量的特征匹配和重定位[28], 都比 PTAM具有更好的视角不变性. 此外, 新增三维点的特征匹配效率更高, 因此能更及时地扩展场景. 扩展场景及时与否决定了后续帧是否能稳定跟踪. 2) ORBSLAM 加入了循环回路的检测和闭合机制, 以消除误差累积. 系统采用与重定位相同的方法来检测回路(匹配回路两侧关键帧上的公共点), 通过方位图(Pose Graph)优化来闭合回路.  3) PTAM 需要用户指定 2 帧来初始化系统, 2 帧间既要有足够的公共点, 又要有足够的平移量. 平移运动为这些公共点提供视差(Parallax), 只有足够的视差才能三角化出精确的三维位置. ORB-SLAM 通过检测视差来自动选择初始化的 2 帧. 4) PTAM 扩展场景时也要求新加入的关键帧提供足够的视差, 导致场景往往难以扩展. ORB-SLAM 采用一种更鲁棒的关键帧和三维点的选择机制——先用宽松的判断条件尽可能及时地加入新的关键帧和三维点, 以保证后续帧的鲁棒跟踪; 再用严格的判断条件删除冗余的关键帧和不稳定的三维点, 以保证 BA 的效率和精度. 。

作者：半闲居士
链接：https://www.zhihu.com/question/35116055/answer/85416630
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

前一阵出了orbslam2，提供单目，双目和rgbd接口。加之代码也很整洁，确实是很好的工作。特点是以orb特征贯穿始终，从一开始的特征处理，匹配，以及用于回环的bag-of-words，词典，全用的是orb。下面说说我个人对它的一些看法。       作者从opencv2.4的orb改进了一版，比opencv里的orb多了一个网格处理，尽量保证每小块图像都能提到特征，避免了局部特征点不足的情形。据我个人的测试(Thinkpad T450 i7)，在640x480的图像中提取500orb约用时13ms左右，匹配精度可以接受，满足实时性要求。       相比于lsd-slam，orb-slam更像一个系统工程——采用当前各种主流的方式计算slam。它稳重大方，不像lsd那样追求标新立异。orb-slam基于研究了很久的特征点，使用dbow2库进行回环检测，具备重新定位能力，使用g2o作为global和local的优化，乃至pnp也用g2o来算。从效果而言比lsd优化，代码也比lsd整洁，更适合继续开发。虽说如楼上所言不像ptam那么惊艳（比如slam++名字好听效果好看但是不开源啊），我们做研究毕竟还是效果至上。       个人觉得，orb-slam的动机还是单目slam，用来做双目或rgbd有些不足。至少orb的建图部分只含有稀疏的map point，不管用于机器人还是AR/VR，这无论如何是不够的。如果给它加上一个较好的地图模块，相信会更加受欢迎。       附上我自己的orb-slam2在手持kinect2上的视频，仅供参考：http://pan.baidu.com/s/1eRcyW1s<img data-rawheight="471" data-rawwidth="834" src="https://pic2.zhimg.com/50/a59b329910d3551358055acf7dc0f96e_hd.jpg" class="origin_image zh-lightbox-thumb" width="834" data-original="https://pic2.zhimg.com/a59b329910d3551358055acf7dc0f96e_r.jpg"/>------------- 2016.2.25 -----------------优点：回环检测做的很好，基本上只要见过的场景都能找回来。接口丰富，代码清楚。缺点：* kinect2 qhd分辨率下（960x540），默认参数，thinkpad T450，帧率<=10Hz；* 运行前要读取一个几百兆的字典——调试程序的时候比较考验耐心；* 比较容易lost，虽然也容易找回来；* 尼玛为什么不支持地图保存和读取！<img data-rawheight="211" data-rawwidth="719" src="https://pic3.zhimg.com/50/4181f7f2953cec31fdeb79e015e992ce_hd.jpg" class="origin_image zh-lightbox-thumb" width="719" data-original="https://pic3.zhimg.com/4181f7f2953cec31fdeb79e015e992ce_r.jpg"/>这个TODO是让我去做吗！------------ 2016.3 ------------------在kinect部分加了个稠密地图，效果看上去还可以，给做rgbd的同学作个参考：加上地图显示就真的只有10Hz了……这个是自己撸了个点云地图模块上去的orbslam2：http://pan.baidu.com/s/1hrbW840还有一个是改了改速度但是精度比较糙的orbslam2：http://pan.baidu.com/s/1skdGeIT各有各用途吧，糙和精的应该都有人喜欢。


## RTAB

RTAB 建议源码安装. 

可以参考: https://www.ncnynl.com/archives/201709/1991.html

1、源码安装rtabmap

```bash
git clone https://github.com/introlab/rtabmap.git rtabmap
cd rtabmap/build
cmake -DCMAKE_INSTALL_PREFIX=~/catkin_ws/devel ..
make -j4
make install
```

2、源码安装 rtabmap_ros

$ cd ~/catkin_ws
$ git clone https://github.com/introlab/rtabmap_ros.git src/rtabmap_ros
$ catkin_make -j1 


3、修改catkin_ws/src/rtabmap_ros/launch中的rtabmap.launch

 <!-- RGB-D related topics -->
  <arg name="rgb_topic"               default="/camera/color/image_raw" />
  <arg name="depth_topic"             default="/camera/aligned_depth_to_color/image_raw" />
  <arg name="camera_info_topic"       default="/camera/color/camera_info" />
  <arg name="depth_camera_info_topic" default="$(arg camera_info_topic)" /> <!-- RGB-D related topics -->
  <arg name="rgb_topic"               default="/camera/color/image_raw" />
  <arg name="depth_topic"             default="/camera/aligned_depth_to_color/image_raw" />
  <arg name="camera_info_topic"       default="/camera/color/camera_info" />
  <arg name="depth_camera_info_topic" default="$(arg camera_info_topic)" />

4、运行

roslaunch realsense2_camera rs_rgbd.launch 
roslaunch rtabmap_ros rtabmap.launch rtabmap_args:="--delete_db_on_start"


在这里插入图片描述
实验效果如上图, 在局部进行建图效果还可以, 但是比如绕房间走一圈, 闭环容易出问题, 还需要进一步调试. 

## VINS-Mono

这个的坑比较大, 主要问题在于realsense  D435i 在ROS中发布的imu topic是分开来的, 同时这两个的时间戳也不太一样: 
/camera/gyro/sample 发布角速度
/camera/accel/sample 发布线加速度

目前网上对realsense  D435i 的IMU问题的相关资料很少, 到目前我还没有调试稳定. 
先发一张我暂时成功的图, 有关于我如何实现的我将单独写一个博客. 

后来发现其实realsense官方是做好了同步的！
直接修改launch文件（如rs_camera.launch）中的: 

<arg name="enable_sync"           default="true"/>
<arg name="unite_imu_method"      default="copy"/>


重新启动 roslaunch 就可以得到topic: “/camera/imu”
在这里插入图片描述

**VINS-Mono 环境配置**:  

比较大的坑在 OpenCV 这里: https://blog.csdn.net/bigdog_1027/article/details/79092263.   

解决方法:  

修改 /opt/ros/kinetic/share/cv_bridge/cmake/cv_bridgeConfig.cmake 文件:  

```bash
# 第 95 行  ------ Before
if(NOT "include;/opt/ros/kinetic/include/opencv-3.3.1-dev;/opt/ros/kinetic/include/opencv-3.3.1-dev/opencv " STREQUAL " ")
  set(cv_bridge_INCLUDE_DIRS "")
# 第 95 行  ------ After
if(NOT "include;/usr/include/opencv;/usr/include/opencv2 " STREQUAL " ")
  set(cv_bridge_INCLUDE_DIRS "")
  set( OpenCV_DIR /usr/local/opencv3.2/share/OpenCV )
  find_package(OpenCV REQUIRED)
  set(_include_dirs "include;${OpenCV_INCLUDE_DIRS}")
  ...  

# 原来的第 112 行  -----------Before
set(libraries "cv_bridge;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_core3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_imgproc3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_imgcodecs3.so.3.3.1")
# 原来的第 112 行  -----------After
set(libraries "cv_bridge;${OpenCV_LIBS}") 
```


将 /opt/ros/kinetic/share/cv_bridge/cmake/cv_bridge-extras.cmake 文件中的版本信息更改如下:  

```bash
set(OpenCV_VERSION 2.4.11)
set(OpenCV_VERSION_MAJOR 2)
set(OpenCV_VERSION_MINOR 4)
set(OpenCV_VERSION_PATCH 11)
set(OpenCV_SHARED ON)
set(OpenCV_CONFIG_PATH /usr/local/share/OpenCV)
set(OpenCV_INSTALL_PATH /usr/local)
set(OpenCV_LIB_COMPONENTS opencv_videostab;opencv_video;opencv_superres;opencv_stitching;opencv_photo;opencv_ocl;opencv_objdetect;opencv_nonfree;opencv_ml;opencv_legacy;opencv_imgproc;opencv_highgui;opencv_gpu;opencv_flann;opencv_features2d;opencv_core;opencv_contrib;opencv_calib3d;opencv_videostab;opencv_video;opencv_superres;opencv_stitching;opencv_photo;opencv_ocl;opencv_objdetect;opencv_nonfree;opencv_ml;opencv_legacy;opencv_imgproc;opencv_highgui;opencv_gpu;opencv_flann;opencv_features2d;opencv_core;opencv_contrib;opencv_calib3d)
set(OpenCV_USE_MANGLED_PATHS TRUE)
set(OpenCV_MODULES_SUFFIX )
```

另外一个文件 VINS-Mono/camera_model/CMakeLists.txt 需要修改:  

```bash
# 第 8 行 find_package 中添加 cv_bridge 包 
find_package(catkin REQUIRED COMPONENTS
    roscpp
    std_msgs
    cv_bridge
    )
```

两个问题:  

1) boost 版本冲突引起 pose-graph 段错误   

指定使用 boost1.58.0   

```bash
set(Boost_INCLUDE_DIR /usr/include)
set(Boost_LIBRARY_DIR_RELEASE /usr/lib/x86_64-linux-gnu)
set(Boost_LIBRARY_DIR_DEBUG /usr/lib/x86_64-linux-gnu)
include_directories(${Boost_INCLUDE_DIR})
# link_directories("/usr/lib/")
find_package(Boost REQUIRED COMPONENTS filesystem program_options system)
```

2) opencv 版本过低引起文件加载错误  

```bash
[ERROR] [1568110191.738181584]: Failed to load config_file
OpenCV Error: Null pointer (NULL or empty buffer) in cvOpenFileStorage, file /home/magic/opt/opencv-2.4.11/modules/core/src/persistence.cpp, line 2696
terminate called after throwing an instance of 'cv::Exception'
  what():  /home/magic/opt/opencv-2.4.11/modules/core/src/persistence.cpp:2696: error: (-27) NULL or empty buffer in function cvOpenFileStorage
```

将 /opt/ros/kinetic/share/cv_bridge/cmake/cv_bridgeConfig.cmake 中的 OpenCV 版本更改为 3.2 及以上即可.  

## Issues

1) Could NOT find ddynamic_reconfigure   

```bash
-- Could NOT find ddynamic_reconfigure (missing: ddynamic_reconfigure_DIR)
-- Could not find the required component 'ddynamic_reconfigure'. The following CMake error indicates that you either need to install the package with the same name or change your environment so that it can be found.
CMake Error at /opt/ros/melodic/share/catkin/cmake/catkinConfig.cmake:83 (find_package):
  Could not find a package configuration file provided by
  "ddynamic_reconfigure" with any of the following names:

    ddynamic_reconfigureConfig.cmake
    ddynamic_reconfigure-config.cmake
```

解决办法, 安装下面的软件包即可.  

```bash
sudo apt-get install ros-melodic-ddynamic-reconfigure
```

2) Resource not found: rgbd_launch  

```bash
roslaunch realsense2_camera rs_rgbd.launch 

... logging to /home/magic/.ros/log/d50b4962-0208-11ea-81ef-4074e0daee36/roslaunch-G7-25360.log
Checking log directory for disk usage. This may take awhile.
Press Ctrl-C to interrupt
Done checking log file disk usage. Usage is <1GB.

Resource not found: rgbd_launch
ROS path [0]=/opt/ros/melodic/share/ros
ROS path [1]=/home/magic/catkin_ws/src
ROS path [2]=/opt/ros/melodic/share
The traceback for the exception was written to the log file
```

安装 


## 参考  

- 在 ubuntu 上使用 Realsense  D435i   运行 ORB-SLAM2、RTAB 和 VINS-Mono: https://blog.csdn.net/qq_41839222/article/details/86503113  
- realsense 官网: https://dev.intelrealsense.com/docs/code-samples  
- realsense-ros: https://github.com/IntelRealSense/realsense-ros/wiki/SLAM-with- D435i   
- 如何用 Realsense  D435i  运行 VINS-Mono 等 VIO 算法: https://blog.csdn.net/qq_41839222/article/details/86552367  
- 从零开始使用 Realsense  D435i  运行 VINS-Mono: https://blog.csdn.net/weixin_44580210/article/details/89789416#3VINSMono_64  
