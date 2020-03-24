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
