# Ubuntu 18.04 源码编译安装 OpenCV2.4.10

> 声明：如果安装中出现问题，可以去本文最后的问题 Issues 模块中寻找解决方案。  

## 1. 下载 OpenCV 源码  

下载地址: http://opencv.org/downloads.html  

## 2. 解压     

```bash
unzip opencv-2.4.10.zip
# 进入源码目录   
cd opencv-2.4.10
```

## 3. 安装依赖库    

```
sudo apt install build-essential cmake libgtk2.0-dev pkg-config python-dev python-numpy libavcodec-dev libavformat-dev libswscale-dev libopenexr-dev
```

## 4. 编译配置   

```bash
mkdir build
cd build/
# ubuntu 1604 使用如下命令
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D CUDA_GENERATION=Kepler -D WITH_CUDA=OFF ../  
# ubuntu 1804 使用如下命令
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D CUDA_GENERATION=Kepler -D WITH_CUDA=OFF -D WITH_FFMPEG=OFF -DENABLE_PRECOMPILED_HEADERS=OFF ../
```

安装所有的 `lib` 文件都会被安装到 `/usr/local` 目录。   

**注意命令行的设置参数都是有原因的**:   

1) 加上 `-D CUDA_GENERATION=Kepler` 或者 `-D CUDA_GENERATION=auto` 是因为我的显卡计算能力较弱，会报如下错误： 

```
nvcc fatal   : Unsupported gpu architecture 'compute_11'
CMake Error at cuda_compile_generated_matrix_operations.cu.o.cmake:208 (message):
  Error generating
```

2) 加上 `-DENABLE_PRECOMPILED_HEADERS=OFF` 是为了防止编译的时候找不到 stdlib.h   

```bash
Error compiling OpenCV, fatal error: stdlib.h: No such file or directory
```

Try by disabling pre-compiled headers, either from cmake-gui or using the command line parameter:  

```bash
-DENABLE_PRECOMPILED_HEADERS=OFF
```

3) 加上 `-D WITH_FFMPEG=OFF` 是为了防止编译的时候 ffmpeg error   

```bash
ffmpeg_codecs.hpp:104:7: error: ‘CODEC_ID_H264’ was not declared in this scope
```

## 5. 编译并安装  

如果计算机中安装过`cuda8`，那么在此之前需要修改`opencv-2.4.10/modules/gpu/src/graphcuts.cpp`：  

```
#if !defined (HAVE_CUDA) || defined (CUDA_DISABLER)   
# 改为  
#if !defined (HAVE_CUDA) || defined (CUDA_DISABLER) || (CUDART_VERSION >= 8000) 
```

然后再开始编译，如果未安装过`cuda`，则可以忽略。    

开始编译.

```bash
make -j8
sudo make install   # 编译完成后安装.   
```

## 6. 收尾工作  

以下是非必要操作(可忽略)：    

- 1) 配置相关信息，使`OpenCV`动态库被共享，具体方法如下：   

在`sudo gedit /etc/ld.so.conf.d/opencv.conf`文件，文件内容如下：   

```bash
# opencv.conf
/usr/local/lib
```

然后使用动态库管理命令`ldconfig`，使`opencv`的相关链接库文件被系统共享，具体命令如下：   

```bash
sudo ldconfig -v | grep "opencv"
```

- 2) 添加`OpenCV`的头文件位置，首先在 `/ect/profile` 文件中添加如下信息：    

```bash
export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig
```

`pkg-config` 维护 `opencv` 的相关配置文件，可以在 `/usr/local/lib/pkgconfig` 目录下看到`opencv.pc` 文件，此文件主要记录 opencv` 的动态库信息和头文件信息。  

使用 `pkg-config` 命令，可以列出 `opencv的配置信息` ，具体命令如下： 

```bash
# 切换路径：
cd /urs/local/lib/pkgconfig
# 执行如下命令：
pkg-config --libs opencv  #查看opencv相关配置信息
```

**注意**：在更改相关文件时，可能文件的权限首先，故需先更改相关的权限。   

## 7. 测试  

在某个目录下建立一个 `test.cpp` 文件.   

```cpp
#include <cv.h>
#include <highgui.h>

using namespace cv;

int main(int argc, char* argv[]) {
    Mat image;
    image = imread(”test.jpg“, 1);

    namedWindow("Display Image", CV_WINDOW_AUTOSIZE);
    imshow("Display Image", image);
    waitKey(0);
    return 0;
}
```

在 `test.cpp` 文件所在目录下新建一个 `CMakeLists.txt` 文件 , 写入如下内容：  

```c
project(test)  
find_package(OpenCV REQUIRED)  
add_executable(test test)  
target_link_libraries(test ${OpenCV_LIBS})  
cmake_minimum_required(VERSION 2.8)
```

然后编译测试文件.  

```bash
cmake .
make
```

找一张`jpg`图片做个测试，注意要和上面那个可执行文件放在同一目录下面,图片名是 `test.jpg`。  

```bash
./test
```

如果能看到照片，那就表示成功了。     

## 问题总结- issues   

1) -Werror=address error.  

```
~/opt/opencv-2.4.11/modules/contrib/src/chamfermatching.cpp:969:30: 
error: the compiler can assume that the address of ‘annotate_img’ will never be NULL [-Werror=address]
                 if (&annotate_img!=NULL) {
                                  ^
```

需要把 `-Werror=address` 编译选项去掉. opencv 是使用 cmake 编译的，将文件 cmake/OpenCVCompilerOptions.cmake 的 74 行注释掉即可.   

```
endif()
#add_extra_compiler_option(-Werror=address)
add_extra_compiler_option(-Werror=sequence-point)
```

2) dumpversion error  

```bash
CMake Error at cmake/OpenCVDetectCXXCompiler.cmake:85 (list):
  list GET given empty list
Call Stack (most recent call first):
  CMakeLists.txt:109 (include)
```

修改 opencv2.4.11/cmake/OpenCVDetectCXXCompiler.cmake 文件, 将其中的 "dumpversion" 改为 "dumpfullversion".  
