## Ubuntu 16.04 下源码编译安装 OpenCV 3.2.0

## 1. 安装依赖包

GCC 4.4.x or later
CMake 2.6 or higher
Git
GTK+2.x or higher, including headers (libgtk2.0-dev) # 控制opencv GUI
pkg-config
Python 2.6 or later and Numpy 1.5 or later with developer packages (python-dev, python-numpy)
ffmpeg or libav development packages: libavcodec-dev, libavformat-dev, libswscale-dev
[optional] libtbb2 libtbb-dev
[optional] libdc1394 2.x
[optional] libjpeg-dev, libpng-dev, libtiff-dev, libjasper-dev, libdc1394-22-dev

```bash
$ sudo apt-get install build-essential
$ sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
$ sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev # 处理图像所需的包
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev liblapacke-dev libopenblas-dev
$ sudo apt-get install libxvidcore-dev libx264-dev # 处理视频所需的包
$ sudo apt-get install libatlas-base-dev gfortran # 优化opencv功能
$ sudo apt-get install ffmpeg libgstreamer-plugins-base1.0-dev libavresample-dev libgphoto2-dev

sudo add-apt-repository "deb http://security.ubuntu.com/ubuntu xenial-security main"
sudo apt update
sudo apt install libjasper1 libjasper-dev

```

       set(OPENCV_ICV_URL "https://raw.githubusercontent.com/opencv/opencv_3rdparty/81a676001ca8075ada498583e4166079e5744668/ippicv/ippicv_linux_20151201.tgz")


https://github.com/google/protobuf/releases/download/v3.1.0/protobuf-cpp-3.1.0.tar.gz

vgg_download(vgg_generated_48.i VGG_48)
vgg_download(vgg_generated_64.i VGG_64)
vgg_download(vgg_generated_80.i VGG_80)
vgg_download(vgg_generated_120.i VGG_120)

set(FILE_HASH_VGG_48 "e8d0dcd54d1bcfdc29203d011a797179")
set(FILE_HASH_VGG_64 "7126a5d9a8884ebca5aea5d63d677225")
set(FILE_HASH_VGG_80 "7cd47228edec52b6d82f46511af325c5")
set(FILE_HASH_VGG_120 "151805e03568c9f490a5e3a872777b75")


mkdir e8d0dcd54d1bcfdc29203d011a797179 && cd e8d0dcd54d1bcfdc29203d011a797179/ && wget https://raw.githubusercontent.com/opencv/opencv_3rdparty/fccf7cd6a4b12079f73bbfb21745f9babcd4eb1d/vgg_generated_48.i


mkdir 7126a5d9a8884ebca5aea5d63d677225 && cd 7126a5d9a8884ebca5aea5d63d677225/ && wget https://raw.githubusercontent.com/opencv/opencv_3rdparty/fccf7cd6a4b12079f73bbfb21745f9babcd4eb1d/vgg_generated_64.i

mkdir 7cd47228edec52b6d82f46511af325c5 && cd 7cd47228edec52b6d82f46511af325c5/ && wget https://raw.githubusercontent.com/opencv/opencv_3rdparty/fccf7cd6a4b12079f73bbfb21745f9babcd4eb1d/vgg_generated_80.i

mkdir 151805e03568c9f490a5e3a872777b75 && cd 151805e03568c9f490a5e3a872777b75/ && wget https://raw.githubusercontent.com/opencv/opencv_3rdparty/fccf7cd6a4b12079f73bbfb21745f9babcd4eb1d/vgg_generated_120.i

分别解压到以下三个文件夹内.  

/home/magic/opt/opencv-3.2.0/3rdparty/ippicv/downloads/linux-808b791a6eac9ed78d32a7666804320e/

/home/magic/opt/opencv-3.2.0/opencv_contrib-3.2.0/modules/dnn/.download/bd5e3eed635a8d32e2b99658633815ef/v3.1.0/

/home/magic/opt/opencv-3.2.0/opencv_contrib-3.2.0/modules/xfeatures2d/cmake/.download/

## 2. 下载 opencv 3.2.0

需要下载 opencv 和 opencv_contrib, 因为 opencv3 以后 SIFT 和 SURF 之类的属性被移到了 contrib 中.  

```bash
$ wget https://github.com/opencv/opencv/archive/3.2.0.zip 
$ wget https://github.com/opencv/opencv_contrib/archive/3.2.0.zip
```

然后分别解压两个压缩包, 将其中一个 opencv_contrib_3.2 移动到 opencv_3.2.0/ 目录下.  

## 3. 配置编译 opencv

(1) 无 NVIDIA CUDA 版本(推荐)   

将上述 opencv 包和 opencv_contrib 包解压, 然后使用下面的命令进行 cmake 属性配置.  

```bash
$ cd opencv-3.2.0
$ mkdir build
$ cd build
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local/opencv3.2 \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib-3.2.0/modules \
    -D PYTHON_EXCUTABLE=/usr/bin/python3 \
    -D WITH_TBB=ON \
    -D WITH_LIBV4L=ON \
    -D WITH_V4L=OFF \
    -D WITH_QT=ON \  # 如果qt未安装可以删去此行;
    -D WITH_GTK=ON \
    -D WITH_OPENGL=ON \
    -D WITH_CUDA=OFF \
    -D BUILD_EXAMPLES=ON .. 
$ make -j4
$ sudo make install
$ sudo ldconfig
```

cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local/opencv3.2 -D INSTALL_PYTHON_EXAMPLES=ON -D INSTALL_C_EXAMPLES=OFF -D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib-3.2.0/modules -D PYTHON_EXCUTABLE=/usr/bin/python3 -D WITH_TBB=ON -D WITH_LIBV4L=ON -D WITH_V4L=OFF -D WITH_QT=ON -D WITH_GTK=ON -D WITH_OPENGL=ON -D WITH_CUDA=OFF -D BUILD_EXAMPLES=ON .. 

其中,  

- CMAKE_INSTALL_PREFIX: 安装的 python 目录前缀, 其实就是指定了 python 模块的安装路径: CMAKE_INSTALL_PREFIX/lib/python2.7/dist-packages. 获取该路径的方式可以用python -c "import sys; print sys.prefix"  
- PYTHON_EXCUTABLE: 指定 python 路径
- OPENCV_EXTRA_MODULES_PATH: 指定 opencv_contrib 所在路径  

(2) NVIDIA CUDA 版本  

opencv 最麻烦的地方就是编译是属性的配置, 对于不同的需求要配置不同的属性. 当使用 NVIDIA GPU GeForce 720m 的时候:   

```bash
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D OPENCV_EXTRA_MODULES_PATH= ../opencv_contrib-3.2.0/modules \ 
    -D PYTHON_EXCUTABLE=/usr/bin/python \
    -D WITH_CUDA=ON \    # 使用CUDA
    -D WITH_CUBLAS=ON \
    -D DCUDA_NVCC_FLAGS="-D_FORCE_INLINES" \
    -D CUDA_ARCH_BIN="2.1" \    # 这个需要去官网确认使用的GPU所对应的版本[查看这里](https://developer.nvidia.com/cuda-gpus)
    -D CUDA_ARCH_PTX="" \
    -D CUDA_FAST_MATH=ON \    # 计算速度更快但是相对不精确
    -D WITH_TBB=ON \
    -D WITH_LIBV4L=ON \
    -D WITH_V4L=OFF \
    -D WITH_QT=ON \    # 如果 qt 未安装可以删去此行;
    -D WITH_GTK=ON \
    -D WITH_OPENGL=ON \
    -D BUILD_EXAMPLES=ON ..

$ make -j4
$ sudo make install
$ sudo ldconfig
```

(3) NVIDIA Jetson TX2 开发板   

目前官方提供的 opencv4tegra 是 2.4 版本的, 尚不支持 3.2 版本, 所以需要自己编译.  

```bash
$ cmake -D WITH_CUDA=ON \
    -D CUDA_ARCH_BIN="6.2" \  # 安装了6.2版本
    -D CUDA_ARCH_PTX=""  \
    -D WITH_OPENGL=ON  \
    -D WITH_LIBV4L=ON \
    -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local ..
```

PS: 不需要安装 contrib 包, 否则之后调用摄像头调整分辨率的时候会失败.  

编译成功时显示下面这些信息:   

```bash
CUDA8.0
--   Other third-party libraries:
--     Use Cuda:                    YES (ver 8.0)
--   NVIDIA CUDA
--     Use CUFFT:                   YES
--     Use CUBLAS:                  NO
--     USE NVCUVID:                 NO
--     NVIDIA GPU arch:             53
--     NVIDIA PTX archs:
--     Use fast math:               NO
OpenGL
--   GUI: 
--     GTK+ 2.x:                    YES (ver 2.24.30)
--     OpenGL support:              YES (/usr/lib/aarch64-linux-gnu/libGLU.so /usr/lib/aarch64-linux-gnu/libGL.so)
VideoIO
--   Video I/O:
--     DC1394 2.x:                  YES (ver 2.2.0)
--     FFMPEG:                      YES
--       codec:                     YES (ver 54.92.100)
--       format:                    YES (ver 54.63.104)
--       util:                      YES (ver 52.18.100)
--       swscale:                   YES (ver 2.2.100)
--       gentoo-style:              YES
--     GStreamer:
--       base:                      NO
--       video:                     NO
--       app:                       NO
--       riff:                      NO
--       pbutils:                   NO
--     V4L/V4L2:                    Using libv4l (ver 1.0.0)
```

注: GPU 版本安装的时候很容易出错, 这里说的出错并不是编译报错, 而是在 python 中调用的时候报错, 比如 cv2.VideoCapture(0) 返回 false, cv2.imshow() 的时候报unspecified error.   

在调用 cv2 的时候报错一般都是在 cmake 配置编译的时候由于配置错误导致的, 所以需要确认配置的参数是否能够覆盖到你所需的范围.   

安装完成之后的输出信息:   

```bash
Install the project...
-- Install configuration: "RELEASE"
-- Installing: /usr/local/opencv3.2/include/opencv2/cvconfig.h
-- Installing: /usr/local/opencv3.2/include/opencv2/opencv_modules.hpp
-- Installing: /usr/local/opencv3.2/lib/pkgconfig/opencv.pc
-- Installing: /usr/local/opencv3.2/share/OpenCV/OpenCVModules.cmake
-- Installing: /usr/local/opencv3.2/share/OpenCV/OpenCVModules-release.cmake
-- Installing: /usr/local/opencv3.2/share/OpenCV/OpenCVConfig-version.cmake
-- Installing: /usr/local/opencv3.2/share/OpenCV/OpenCVConfig.cmake
-- Installing: /usr/local/opencv3.2/include/opencv/cxcore.hpp
-- Installing: /usr/local/opencv3.2/include/opencv/cxeigen.hpp
-- Installing: /usr/local/opencv3.2/include/opencv/cv.h
-- Installing: /usr/local/opencv3.2/include/opencv/ml.h
-- Installing: /usr/local/opencv3.2/include/opencv/cvwimage.h
-- Installing: /usr/local/opencv3.2/include/opencv/cvaux.hpp
-- Installing: /usr/local/opencv3.2/include/opencv/cxcore.h
-- Installing: /usr/local/opencv3.2/include/opencv/cxmisc.h
-- Installing: /usr/local/opencv3.2/include/opencv/highgui.h
-- Installing: /usr/local/opencv3.2/include/opencv/cvaux.h
-- Installing: /usr/local/opencv3.2/include/opencv/cv.hpp
-- Installing: /usr/local/opencv3.2/include/opencv2/opencv.hpp

-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/calibrate.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/tst_scene_render.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/houghcircles.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/video.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/opt_flow.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/browse.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/letter_recog.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/squares.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/video_v4l2.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/demo.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/lk_homography.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/turing.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/stereo_match.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/grabcut.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/color_histogram.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/mser.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/deconvolution.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/digits_adjust.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/hist.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/facedetect.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/inpaint.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/gabor_threads.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/mouse_and_match.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/kmeans.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/digits_video.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/_doc.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/plane_ar.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/find_obj.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/lappyr.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/plane_tracker.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/lk_track.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/feature_homography.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/peopledetect.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/_coverage.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/fitline.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/digits.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/morphology.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/texture_flow.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/camshift.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/video_threaded.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/coherence.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/opencv_version.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/dft.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/common.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/logpolar.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/gaussian_mix.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/watershed.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/kalman.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/mosse.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/houghlines.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/floodfill.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/contours.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/distrans.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/edge.py
-- Installing: /usr/local/opencv3.2/share/OpenCV/samples/python/asift.py
```


## 4. 完成安装并测试

安装完成以后, 重启下机器. 编译之后应该会在 `CMAKE_INSTALL_PREFIX/lib/python2.7/dist-packages/` 目录下找到 cv2.so. 打开 python console, 检测 opencv 版本 `python -c "import cv2; print cv2.__version__"`. 如果正确安装的话则会输出3.2.0.   

PS: 如果 import 的时候报类似于 error while loading shared libraries: libopencv_core.so.3.0: cannot open shared object file: No such file or directory. 的错误, 可能是 library 环境变量的错误, 可以尝试将 export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib 加入到 ~/.bashrc 中然后运行 `source ~/.bashrc` 命令即可.   

## 参考

https://www.learnopencv.com/install-opencv3-on-ubuntu/  
http://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/  
http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html  
http://stackoverflow.com/questions/31040746/cant-open-video-using-opencv  
http://dev.t7.ai/jetson/opencv/  
https://developer.nvidia.com/cuda-gpus  
http://stackoverflow.com/questions/41818870/python-opencv-imshow-error  
http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_fedora/py_setup_in_fedora.html  
http://answers.opencv.org/question/27114/error-while-loading-shared-libraries-libopencv_coreso30/  

## 可能遇到的问题 

1. Could NOT find Doxygen (missing:  DOXYGEN_EXECUTABLE)   

```bash
-- Could NOT find JNI (missing:  JAVA_INCLUDE_PATH JAVA_INCLUDE_PATH2 JAVA_AWT_INCLUDE_PATH) 
-- Could NOT find Matlab (missing:  MATLAB_MEX_SCRIPT MATLAB_INCLUDE_DIRS MATLAB_ROOT_DIR MATLAB_LIBRARIES MATLAB_LIBRARY_DIRS MATLAB_MEXEXT MATLAB_ARCH MATLAB_BIN) 
-- The imported target "vtkRenderingPythonTkWidgets" references the file
   "/usr/lib/x86_64-linux-gnu/libvtkRenderingPythonTkWidgets.so"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/cmake/vtk-6.2/VTKTargets.cmake"
but not all the files it references.

-- The imported target "vtk" references the file
   "/usr/bin/vtk"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/cmake/vtk-6.2/VTKTargets.cmake"
but not all the files it references.

-- Found VTK ver. 6.2.0 (usefile: /usr/lib/cmake/vtk-6.2/UseVTK.cmake)
CMake Error at cmake/OpenCVModule.cmake:268 (message):
  The directory /home/magic/opt/opencv-3.2.0/modules is observed for OpenCV
  modules second time.
Call Stack (most recent call first):
  modules/CMakeLists.txt:7 (ocv_glob_modules)
```

solved:  

```
sudo ln -s /usr/lib/python2.7/dist-packages/vtk/libvtkRenderingPythonTkWidgets.x86_64-linux-gnu.so /usr/lib/x86_64-linux-gnu/libvtkRenderingPythonTkWidgets.so
sudo apt-get install python-vtk
```

2. CMake Error: The following variables are used in this project, but they are set to NOTFOUND.  

Please set them or make sure they are set and tested correctly in the CMake files:  

CUDA_nppi_LIBRARY (ADVANCED) 

solved:   

https://blog.csdn.net/u014613745/article/details/78310916  
