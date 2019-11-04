# Realsense-D435i 深度相机环境搭建 

 sudo apt-get install ros-kinetic-cv-bridge ros-kinetic-tf ros-kinetic-message-filters ros-kinetic-image-transport


Realsense D435i 在ubuntu上安装SDK与ROS Wrapper 运行ORB-SLAM2、RTAB和VINS-Mono
2019年01月18日 21:14:12 Manii 阅读数 4776
版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。
本文链接：https://blog.csdn.net/qq_41839222/article/details/86503113
前言
等了一个月的realsense d435i终于发货了！
这款D435i（见下图）在D435的基础上，另外搭载了博世的惯性测量单元（IMU），可以作为研究VIO及其他SLAM算法的良好传感器组。本文将介绍自己一步步搭建d435i环境，并成功跑通ORB-SLAM2、RTAB和VINS-Mono的过程，供大家参考。
在这里插入图片描述

安装环境
系统：ubuntu 16.04 内核 4.15.0-43-generic
ROS： Kinetic
传感器：intel realsense d435i
环境上已经成功搭建并使用dateset跑过ORB-SLAM2、VINS-Mono与RTAB。

## 1. 安装 Realsense SDK

github：https://github.com/IntelRealSense/librealsense  

安装可以参考文档：https://github.com/IntelRealSense/librealsense/blob/master/doc/installation.md  

1、下载 source

```bash
git clone https://github.com/IntelRealSense/librealsense
cd librealsense
```

2、安装依赖项

```bash
sudo apt-get install libudev-dev pkg-config libgtk-3-dev libusb-1.0-0-dev pkg-config libglfw3-dev libssl-dev
```

3、Install Intel Realsense permission scripts located in librealsense source directory:

```bash
sudo cp config/99-realsense-libusb.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && udevadm trigger 
```

4、这边需要注意把 realsense 相机拔下来  

Build and apply patched kernel modules for:  


根据不同的 ubuntu 版本安装：对于 Ubuntu 14/16/18 LTS   

```bash
./scripts/patch-realsense-ubuntu-lts.sh
sudo dmesg | tail -n 50
```

这里可以看一下UVC是否安装成功了:  

```bash
[ 7853.426645] input: Intel(R) RealSense(TM) Depth Ca as /devices/pci0000:00/0000:00:14.0/usb2/2-7/2-7:1.0/input/input23
[ 7853.427347] uvcvideo: Found UVC 1.50 device Intel(R) RealSense(TM) Depth Camera 435i (8086:0b3a)
[ 7853.428343] uvcvideo: Unable to create debugfs 2-5 directory.
[ 7853.428463] uvcvideo 2-7:1.3: Entity type for entity Processing 7 was not initialized!
[ 7853.428467] uvcvideo 2-7:1.3: Entity type for entity Extension 8 was not initialized!
[ 7853.428470] uvcvideo 2-7:1.3: Entity type for entity Camera 6 was not initialized!
[ 7853.589704] hid-sensor-hub 0003:8086:0B3A.0008: No report with id 0xffffffff found
[ 7853.832928] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7853.908547] hid-sensor-hub 0003:8086:0B3A.0008: No report with id 0xffffffff found
[ 7854.203436] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7854.253585] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7854.303816] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7854.407915] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7854.558642] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7859.513162] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7859.563308] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7860.613766] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7860.663909] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7861.714432] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7861.764581] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7862.815022] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7862.865124] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7867.916980] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7867.967141] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7874.019476] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7875.069866] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7876.120392] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7876.170546] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7877.221005] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7877.271162] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7880.322474] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7880.372637] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7882.423437] uvcvideo: Failed to query (GET_CUR) UVC control 1 on unit 3: -32 (exp. 1024).
[ 7889.845463] hid-sensor-hub 0003:8086:0B3A.0008: No report with id 0xffffffff found
[ 7889.845580] hid-sensor-hub 0003:8086:0B3A.0008: No report with id 0xffffffff found
[ 8050.312036] hid-sensor-hub 0003:8086:0B3A.0008: No report with id 0xffffffff found
[ 8052.368689] hid-sensor-hub 0003:8086:0B3A.0008: No report with id 0xffffffff found
[ 8085.635786] hid-sensor-hub 0003:8086:0B3A.0008: No report with id 0xffffffff found
[ 8086.345037] hid-sensor-hub 0003:8086:0B3A.0008: No report with id 0xffffffff found
[ 8107.911562] hid-sensor-hub 0003:8086:0B3A.0008: No report with id 0xffffffff found
[ 8107.916391] hid-sensor-hub 0003:8086:0B3A.0008: No report with id 0xffffffff found
[ 8149.891255] hid-sensor-hub 0003:8086:0B3A.0008: No report with id 0xffffffff found
[ 8150.691295] hid-sensor-hub 0003:8086:0B3A.0008: No report with id 0xffffffff found
[14841.010329] perf: interrupt took too long (2508 > 2500), lowering kernel.perf_event_max_sample_rate to 79500
[19849.670339] perf: interrupt took too long (3138 > 3135), lowering kernel.perf_event_max_sample_rate to 63500
[30003.311179] perf: interrupt took too long (3941 > 3922), lowering kernel.perf_event_max_sample_rate to 50750
[50465.237420] perf: interrupt took too long (4932 > 4926), lowering kernel.perf_event_max_sample_rate to 40500
[61092.424634] usb 2-7: USB disconnect, device number 5
[61092.425122] hid-sensor-hub 0003:8086:0B3A.0008: No report with id 0xffffffff found
[61093.450534] hid-sensor-hub 0003:8086:0B3A.0008: No report with id 0xffffffff found
```

5、基于 cmake 的编译

```bash
mkdir build
cd build
cmake ../ -DBUILD_EXAMPLES=true
make
sudo make install
```

-DBUILD_EXAMPLES=true 这个选项表示带演示和教程的.  

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
```


6、进入 /librealsense/build/examples/capture，试一下效果

```
./rs-capture 
```d

在这里插入图片描述
在这里插入图片描述
大功告成！

## 安装 ROS Wrapper  

https://github.com/intel-ros/realsense  
 
直接按照 github 上的教程即可：

1、建立 workspace，已经有的可以跳过

```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src/
catkin_init_workspace 
cd ..
catkin_make
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

2、在catkin_ws/src/下载源程序

cd src
git clone https://github.com/intel-ros/realsense.git

3、catkin_make

cd ..
catkin_make

4、如果没有错误说明，已经装好了，启动相机节点

roslaunch realsense2_camera rs_rgbd.launch

5、看一下发布的topic

rostopic list

在这里插入图片描述

6、打开RVIZ看看效果

在这里插入图片描述

内参获取

若不进行标定，可以先从Realsense ROS Wrapper发布的topic中获得相机的内参。

rostopic echo /camera/color/camera_info 
rostopic echo /camera/aligned_depth_to_color/camera_info

解释一下topic中所有 aligned_depth_to_color 是指已经将深度信息通过相机到 RGBD 的外参映射到彩色图像上了

在这里插入图片描述

## ORB-SLAM

1、在ORB-SLAM2/Examples/ROS/ORB-SLAM2/src中修改ros_rgbd.cc的topic订阅：

message_filters::Subscriber<sensor_msgs::Image> rgb_sub(nh, "/camera/color/image_raw", 1);
message_filters::Subscriber<sensor_msgs::Image> depth_sub(nh, "/camera/aligned_depth_to_color/image_raw", 1);

2、重新编译ORB-SLAM2

chmod +x build_ros.sh
./build_ros.sh

3、连接 realsense d435i，启动 ROS realsense2_camera：

roslaunch realsense2_camera rs_rgbd.launch

4、先用TUM1.yaml的参数运行一下试试看：

rosrun ORB_SLAM2 RGBD Vocabulary/ORBvoc.txt Examples/RGB-D/TUM1.yaml 

在这里插入图片描述程序正常运行！

5、修改yaml文件中的部分参数再试试看！

rosrun ORB_SLAM2 RGBD Vocabulary/ORBvoc.txt Examples/RGB-D/realsense_d435i.yaml 

在这里插入图片描述

## RTAB

RTAB建议源码安装。

可以参考：https://www.ncnynl.com/archives/201709/1991.html

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
实验效果如上图，在局部进行建图效果还可以，但是比如绕房间走一圈，闭环容易出问题，还需要进一步调试。

## VINS-Mono

这个的坑比较大，主要问题在于realsense d435i在ROS中发布的imu topic是分开来的，同时这两个的时间戳也不太一样：
/camera/gyro/sample 发布角速度
/camera/accel/sample 发布线加速度

目前网上对realsense d435i的IMU问题的相关资料很少，到目前我还没有调试稳定。
先发一张我暂时成功的图，有关于我如何实现的我将单独写一个博客。

后来发现其实realsense官方是做好了同步的！
直接修改launch文件（如rs_camera.launch）中的：

<arg name="enable_sync"           default="true"/>
<arg name="unite_imu_method"      default="copy"/>


重新启动 roslaunch 就可以得到topic：“/camera/imu”
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



## 参考  

- realsense 官网: https://dev.intelrealsense.com/docs/code-samples  
- realsense-ros: https://github.com/IntelRealSense/realsense-ros/wiki/SLAM-with-D435i  
- 在 ubuntu 上使用 Realsense D435i  运行 ORB-SLAM2、RTAB 和 VINS-Mono: https://blog.csdn.net/qq_41839222/article/details/86503113  
- 如何用 Realsense D435i 运行 VINS-Mono 等 VIO 算法: https://blog.csdn.net/qq_41839222/article/details/86552367  
- 从零开始使用 Realsense D435i 运行 VINS-Mono: https://blog.csdn.net/weixin_44580210/article/details/89789416#3VINSMono_64  