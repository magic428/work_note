# SLAM 开发环境配置  

**目录**  

- PCL 安装 
- Pangolin   
- g2o   
- ceres   
- Sophus   
- DBow3   

## PCL 点云库安装  

[PCL 点云库安装可以参考这里](https://github.com/magic428/work_note/blob/master/ubuntu_os_usage/doc/dev_env_install/pcl-install.md)   

## 1. Pangolin 

1. 下载源码  

```bash
git clone https://github.com/stevenlovegrove/Pangolin
```

2.  安装依赖包  

```bash
sudo apt-get install libglew-dev
```
3. 编译安装   

```bash
cd /path/to/pangolin
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release  ..
make 
sudo make install 
```

安装输出信息如下:   

```bash
$ sudo make install

Install the project...
-- Install configuration: "Release"
-- Installing: /usr/local/include/pangolin/config.h
-- Installing: /usr/local/include/pangolin/factory/factory_registry.h
-- Installing: /usr/local/lib/libpangolin.so
-- Installing: /usr/local/lib/cmake/Pangolin/PangolinConfig.cmake
-- Installing: /usr/local/lib/cmake/Pangolin/PangolinConfigVersion.cmake
-- Installing: /usr/local/lib/cmake/Pangolin/PangolinTargets.cmake
-- Installing: /usr/local/lib/cmake/Pangolin/PangolinTargets-release.cmake
-- Installing: /usr/local/bin/VideoViewer
-- Set runtime path of "/usr/local/bin/VideoViewer" to ""
-- Installing: /usr/local/bin/VideoConvert
-- Set runtime path of "/usr/local/bin/VideoConvert" to ""
-- Installing: /usr/local/bin/VideoJsonPrint
-- Set runtime path of "/usr/local/bin/VideoJsonPrint" to ""
-- Installing: /usr/local/bin/VideoJsonTransform
-- Set runtime path of "/usr/local/bin/VideoJsonTransform" to ""
-- Installing: /usr/local/bin/Plotter
-- Set runtime path of "/usr/local/bin/Plotter" to ""
```

4. issues   

1)  /usr/bin/ld: cannot find -lEGL

首先安装 OpenGL.   

```bash
sudo apt-get install build-essential libgl1-mesa-dev
sudo apt-get install freeglut3-dev
sudo apt-get install libglew-dev libsdl2-dev libsdl2-image-dev libglm-dev libfreetype6-dev
```

然后使用 `sudo find /usr -name "libEGL*"` 来查找 libEGL 库, 发现其位于: /usr/lib/x86_64-linux-gnu/mesa-egl 目录下.  

查看 /usr/lib/x86_64-linux-gnu/mesa-egl 目录后发现, 

```bash
lrwxrwxrwx   1 root root     15 8月  29 15:04 libEGL.so.1 -> libEGL.so.1.0.0
-rw-r--r--   1 root root 239104 8月  29 15:04 libEGL.so.1.0.0
lrwxrwxrwx   1 root root     18 8月  29 15:04 libGLESv2.so.2 -> libGLESv2.so.2.0.0
-rw-r--r--   1 root root  34592 8月  29 15:04 libGLESv2.so.2.0.0
```

只有 libEGL.so.1 文件, 而没有 libEGL.so. 只需要创建软链接 libEGL.so 指向 libEGL.so.1.0.0 即可.   

```bash
sudo ln -s libEGL.so.1.0.0 libEGL.so
```

## 3. 安装 g2o  

1. 安装依赖项  

```bash
sudo apt-get install cmake libeigen3-dev libsuitesparse-dev qtdeclarative5-dev qt5-qmake libqglviewer-dev
```

2. 下载源码

```bash
git clone https://github.com/RainerKuemmerle/g2o.git
```

3. 编译安装g2o库。

```bash
cd /path/to/g2o  # 进入到安装包文件夹内
mkdir build 
cd build 
cmake ..
make -j8
sudo make install
```

安装信息输出如下:   

```bash
Install the project...
-- Install configuration: "Release"
-- Installing: /usr/local/include/g2o/config.h
-- Installing: /usr/local/lib/cmake/g2o/g2oConfig.cmake
-- Installing: /usr/local/lib/cmake/g2o/g2oConfigVersion.cmake
-- Installing: /usr/local/lib/cmake/g2o/g2oTargets.cmake
-- Installing: /usr/local/lib/cmake/g2o/g2oTargets-release.cmake
-- Installing: /usr/local/lib/libg2o_ext_freeglut_minimal.so
```

## 4. 安装 ceres  

1. 安装依赖项  

```bash
sudo apt-get install cmake libgoogle-glog-dev libatlas-base-dev libeigen3-dev libsuitesparse-dev
```

2. 下载源码  

```bash
git clone https://github.com/ceres-solver/ceres-solver
```

3. 编译安装 ceres 库   

```bash
cd /path/to/ceres  # 进入到安装包文件夹内
mkdir build 
cd build 
cmake ..
make -j8
sudo make install
```

安装信息输出如下:   

```bash
Install the project...
-- Install configuration: "Release"
-- Installing: /usr/local/include/ceres/normal_prior.h
-- Installing: /usr/local/lib/cmake/Ceres/CeresTargets.cmake
-- Installing: /usr/local/lib/cmake/Ceres/CeresTargets-release.cmake
-- Installing: /usr/local/lib/cmake/Ceres/CeresConfig.cmake
-- Installing: /usr/local/lib/cmake/Ceres/CeresConfigVersion.cmake
-- Installing: /usr/local/lib/cmake/Ceres/FindEigen.cmake
-- Installing: /usr/local/lib/cmake/Ceres/FindGlog.cmake
-- Installing: /usr/local/lib/cmake/Ceres/FindGflags.cmake
-- Installing: /usr/local/lib/libceres.a
```

## 5. 安装 Sophus  

1. 下载源码  

```bash
git clone http://github.com/strasdat/Sophus.git
```

2. 编译安装 Sophus 库   

```bash
cd /path/to/Sophus  # 进入到安装包文件夹内
git checkout a621ff  # 使用 Sophus 的非模板版本

mkdir build
cd build
cmake ..
make -j8
sudo make install
```

安装信息输出如下:   

```bash
Install the project...
/usr/bin/cmake -P cmake_install.cmake
-- Install configuration: "Release"
-- Installing: /usr/local/include/sophus
-- Installing: /usr/local/include/sophus/sim3.h
-- Installing: /usr/local/include/sophus/so2.h
-- Installing: /usr/local/include/sophus/se3.h
-- Installing: /usr/local/include/sophus/so3.h
-- Installing: /usr/local/include/sophus/scso3.h
-- Installing: /usr/local/include/sophus/se2.h
-- Installing: /usr/local/lib/libSophus.so
```

## 6. 安装 DBow3

1. 下载源码 

```bash
git clone https://github.com/rmsalinas/DBow3.git
```

2. 编译安装 DBow3  

```bash
cd /path/to/DBow3  # 进入到安装包文件夹内
mkdir build
cd build
cmake ..
make -j8
sudo make install
```

安装信息输出如下:   

```bash
Install the project...
-- Install configuration: "Release"
-- Installing: /usr/local/lib/cmake/FindDBoW3.cmake
-- Installing: /usr/local/lib/cmake/DBoW3/DBoW3Config.cmake
-- Installing: /usr/local/lib/libDBoW3.so.0.0.1
-- Installing: /usr/local/lib/libDBoW3.so.0.0
-- Installing: /usr/local/lib/libDBoW3.so
-- Set runtime path of "/usr/local/lib/libDBoW3.so.0.0.1" to ""
-- Installing: /usr/local/include/DBoW3/FeatureVector.h
-- Installing: /usr/local/include/DBoW3/DescManip.h
-- Installing: /usr/local/include/DBoW3/timers.h
-- Installing: /usr/local/include/DBoW3/Vocabulary.h
-- Installing: /usr/local/include/DBoW3/QueryResults.h
-- Installing: /usr/local/include/DBoW3/ScoringObject.h
-- Installing: /usr/local/include/DBoW3/BowVector.h
-- Installing: /usr/local/include/DBoW3/quicklz.h
-- Installing: /usr/local/include/DBoW3/Database.h
-- Installing: /usr/local/include/DBoW3/exports.h
-- Installing: /usr/local/include/DBoW3/DBoW3.h
```

## 7. 安装 OctoMap  


1. OctoMap 的下载   

```bash
git clone https：//github.com/OctoMap/octomap
```

2. 依赖库安装

```bash
sudo apt-get install build-essential cmake doxygen libqt4-dev libqt4-opengl-dev libqglviewer-qt4-dev
```

3. 编译安装 DBow3  

```bash
cd /path/to/octomap  # 进入到安装包文件夹内
mkdir build
cd build
cmake ..
make -j8
sudo make install
```

安装时的输出信息:  

```bash
Install the project...
-- Install configuration: ""
-- Installing: /usr/local/include/octomap/OcTreeNode.h
-- Installing: /usr/local/share/octomap/package.xml
-- Installing: /usr/local/share/octomap/octomap-config.cmake
-- Installing: /usr/local/share/octomap/octomap-config-version.cmake
-- Installing: /usr/local/lib/pkgconfig/octomap.pc
-- Installing: /usr/local/lib/liboctomath.so.1.9.0
-- Installing: /usr/local/lib/liboctomath.so.1.9
-- Installing: /usr/local/lib/liboctomath.so
-- Installing: /usr/local/share/octovis/octovis-targets.cmake
-- Installing: /usr/local/include/octovis/ColorOcTreeDrawer.h
-- Installing: /usr/local/include/octovis/SelectionBox.h
-- Installing: /usr/local/include/octovis/SceneObject.h
-- Installing: /usr/local/include/octovis/TrajectoryDrawer.h
-- Installing: /usr/local/include/octovis/OcTreeRecord.h
-- Installing: /usr/local/include/octovis/PointcloudDrawer.h
-- Installing: /usr/local/include/octovis/OcTreeDrawer.h
-- Installing: /usr/local/share/octovis/octovis-config.cmake
-- Installing: /usr/local/share/octovis/octovis-config-version.cmake
-- Installing: /usr/local/share/octovis/package.xml
-- Installing: /usr/local/include/dynamicEDT3D/point.h
-- Installing: /usr/local/include/dynamicEDT3D/bucketedqueue.h
-- Installing: /usr/local/include/dynamicEDT3D/dynamicEDT3D.h
-- Installing: /usr/local/include/dynamicEDT3D/dynamicEDTOctomap.h
-- Installing: /usr/local/include/dynamicEDT3D/bucketedqueue.hxx
-- Installing: /usr/local/include/dynamicEDT3D/dynamicEDTOctomap.hxx
-- Installing: /usr/local/share/dynamic_edt_3d/package.xml
-- Installing: /usr/local/share/dynamicEDT3D/dynamicEDT3DConfig.cmake
-- Installing: /usr/local/share/dynamicEDT3D/dynamicEDT3DConfig-version.cmake
-- Installing: /usr/local/lib/pkgconfig/dynamicEDT3D.pc
-- Installing: /usr/local/lib/libdynamicedt3d.so.1.9.0
-- Installing: /usr/local/lib/libdynamicedt3d.so.1.9
-- Installing: /usr/local/lib/libdynamicedt3d.so
-- Set runtime path of "/usr/local/lib/libdynamicedt3d.so.1.9.0" to "/usr/local/lib"
-- Installing: /usr/local/lib/libdynamicedt3d.a
-- Installing: /usr/local/share/dynamicEDT3D/dynamicEDT3DTargets.cmake
```

# 8. 安装 apriltag  

```bash
Install the project...
-- Install configuration: "Release"
-- Installing: /usr/local/lib/libapriltag.so.3.1.0
-- Installing: /usr/local/lib/libapriltag.so.3
-- Installing: /usr/local/lib/libapriltag.so
-- Installing: /usr/local/include/apriltag/tag25h9.h
-- Installing: /usr/local/share/apriltag/cmake/apriltagConfig.cmake
-- Installing: /usr/local/share/apriltag/cmake/apriltagConfig-release.cmake
-- Installing: /usr/local/lib/pkgconfig/apriltag.pc
-- Installing: /usr/local/bin/opencv_demo
```