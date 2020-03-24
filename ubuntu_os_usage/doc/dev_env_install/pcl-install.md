# 源码编译安装 PCL 包

PCL 编译需要使用 VTK 库, 因此先编译安装 VTK 库.  

## 1. 源码安装 VTK 库

> 源码安装很重要！！！ apt 安装的方式会出现 .so 文件缺失的情况！  

1.1 首先安装依赖项  

```bash
sudo apt-get install libx11-dev libxext-dev libxtst-dev libxrender-dev libxmu-dev libxmuu-dev build-essential libgl1-mesa-dev libglu1-mesa-dev cmake cmake-gui doxygen
```

1.2 安装并配置 QT 路径 

编译 VTK 首先要安装 QT, 这里安装的是 QT 5.10.0.  

命令行输入 gedit ~/.bashrc, 在文件结尾写入以下内容:  

```bash
export QTDIR=/home/magic/opt/Qt5.10.0/5.10.0/gcc_64/
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${QTDIR}/lib
export PATH=${QTDIR}/bin:${PATH}
```

运行 source ~/.bashrc 更新配置信息.  

1.3 下载 VTK 源码并配置 VTK  

官网下载: https://vtk.org/download/，我选择了 VTK-7.1.1.tar.gz，下载完成后解压缩到你的文件安装目录。  

```
cd /home/Username/Download/VTK
mkdir build
cd build 
ccmake ..
```

接下来会弹出配置窗口, 主要配置选项： 

```conf
# 按照 VTK tutorial 要求，每设置完一项均按 'c' 键进行一次 configuration 
BUILD_SHARED_LIBS = ON   
VTK_QT_VERSION=5
BUILD_TESTING = OFF  
CMAKE_BUILD_TYPE = Release    # 默认 Debug, 运行会较慢
CMAKE_INSTALL_PREFIX = /usr/local    # 这里用默认就行，或者改到想要安装的位置
VTK_GROUP_QT = ON
# 以下为高级设置，需先在命令行按't'才可见
VTK_FORBID_DOWNLOADS = ON   # 默认OFF，建议打开，否则编译会报错
```
 
# 此时应已经出现'g' generating 的按键选项，按 'g' 即完成配置.

1.4 安装 VTK  

```bash
cmake .
make -j12
sudo make install
```
## 2. 编译安装 

2.1 安装 PCL 的依赖包  

```bash
sudo apt-get install git build-essential linux-libc-dev cmake cmake-gui libusb-1.0-0-dev libusb-dev libudev-dev mpi-default-dev openmpi-bin openmpi-common libflann1.8 libflann-dev libeigen3-dev libpcap-dev libpng16-dev
```

其他可选的依赖库:  

```bash
sudo apt-get install libqhull* libgtest-dev freeglut3-dev pkg-config libxmu-dev libxi-dev  mono-complete  libopenni-dev  libopenni2-dev 
```

2.2. 下载 pcl 源码

去 pcl 官方 github 下载需要的 pcl 版本放到主目录下, 然后：

```bash
cd pcl 
mkdir build
cd build
ccmake ../
```

弹出下面的配置窗口:  

```
BUILD_common                     ON
BUILD_features                   ON
BUILD_filters                    ON
BUILD_global_tests               OFF
BUILD_io                         ON
BUILD_kdtree                     ON
BUILD_keypoints                  ON
BUILD_octree                     ON
BUILD_range_image                ON
BUILD_registration               ON
BUILD_sample_consensus           ON
BUILD_segmentation               ON
BUILD_surface                    ON
BUILD_visualization              ON
CMAKE_BUILD_TYPE
CMAKE_INSTALL_PREFIX             /usr/local
PCL_SHARED_LIBS                  ON
PCL_VERSION                      1.0.0
VTK_DIR                          /usr/local/lib/cmake/vtk-7.1
```

编译安装  

```bash
make -12
sudo make -j2 install
```

cmake 配置的输出信息如下:   

```bash
-- Using CPU native flags for SSE optimization: -march=native
-- Found OpenMP
-- Eigen found (include: /usr/include/eigen3, version: 3.2.92)
-- OpenNI found (include: /usr/include/ni, lib: /usr/lib/libOpenNI.so)
-- OpenNI2 found (include: /usr/include/openni2, lib: /usr/lib/libOpenNI2.so)
-- Checking for module 'metslib'
--   No package 'metslib' found
-- QHULL found (include: /usr/include, lib: optimized;/usr/lib/x86_64-linux-gnu/libqhull.so;debug;/usr/lib/x86_64-linux-gnu/libqhull.so)
-- Found CUDA Toolkit v10.0
-- CUDA NVCC target flags: -gencode;arch=compute_30,code=sm_30;-gencode;arch=compute_35,code=sm_35;-gencode;arch=compute_50,code=sm_50;-gencode;arch=compute_52,code=sm_52;-gencode;arch=compute_53,code=sm_53;-gencode;arch=compute_60,code=sm_60;-gencode;arch=compute_61,code=sm_61;-gencode;arch=compute_70,code=sm_70;-gencode;arch=compute_72,code=sm_72;-gencode;arch=compute_75,code=sm_75
-- VTK_MAJOR_VERSION 7, rendering backend: OpenGL2
-- VTK found (include: /usr/local/include/vtk-7.1, libs: vtkChartsCore;vtkCommonColor;vtkCommonCore;vtksys;vtkCommonDataModel;vtkCommonMath;vtkCommonMisc;vtkCommonSystem;vtkCommonTransforms;vtkCommonExecutionModel;vtkFiltersGeneral;vtkCommonComputationalGeometry;vtkFiltersCore;vtkInfovisCore;vtkFiltersExtraction;vtkFiltersStatistics;vtkImagingFourier;vtkImagingCore;vtkalglib;vtkRenderingContext2D;vtkRenderingCore;vtkFiltersGeometry;vtkFiltersSources;vtkRenderingFreeType;vtkfreetype;vtkzlib;vtkFiltersModeling;vtkImagingSources;vtkInteractionStyle;vtkInteractionWidgets;vtkFiltersHybrid;vtkImagingColor;vtkImagingGeneral;vtkImagingHybrid;vtkIOImage;vtkDICOMParser;vtkmetaio;vtkjpeg;vtkpng;vtktiff;vtkRenderingAnnotation;vtkRenderingVolume;vtkIOXML;vtkIOCore;vtkIOXMLParser;vtkexpat;vtkIOGeometry;vtkIOLegacy;vtkIOPLY;vtkRenderingLOD;vtkViewsContext2D;vtkViewsCore;vtkRenderingContextOpenGL2;vtkRenderingOpenGL2;vtkglew;vtkRenderingQt;vtkFiltersTexture;vtkGUISupportQt;vtkRenderingLabel
-- Boost version: 1.66.0
-- Found the following Boost libraries:
--   filesystem
--   date_time
--   iostreams
--   chrono
--   system
--   regex
-- Could NOT find GLEW (missing:  GLEW_INCLUDE_DIR GLEW_LIBRARY) 
-- DOXYGEN_FOUND 
-- HTML_HELP_COMPILER 
-- Found CPack generators: DEB
-- The following subsystems will be built:
--   common
--   geometry
--   octree
--   io
--   kdtree
--   search
--   sample_consensus
--   filters
--   2d
--   features
--   ml
--   segmentation
--   surface
--   registration
--   keypoints
--   tracking
--   recognition
--   stereo
--   tools
-- The following subsystems will not be built:
--   visualization: Disabled manually.
--   apps: Disabled: visualization missing.
--   outofcore: Requires visualization.
--   examples: Code examples are disabled by default.
--   people: Requires visualization.
--   global_tests: No reason
--   simulation: Disabled: visualization missing.
-- Configuring done
-- Generating done
-- Build files have been written to: /home/magic/opt/pcl/pcl/build
```

注意输出信息中的:  The following subsystems will not be built.  

```
BUILD_common: option to enable/disable building of common library
BUILD_features: option to enable/disable building of features library
BUILD_filters: option to enable/disable building of filters library
BUILD_global_tests: option to enable/disable building of global unit tests
BUILD_io: option to enable/disable building of io library
BUILD_kdtree: option to enable/disable building of kdtree library
BUILD_keypoints: option to enable/disable building of keypoints library
BUILD_octree: option to enable/disable building of octree library
BUILD_range_image: option to enable/disable building of range_image library
BUILD_registration: option to enable/disable building of registration library
BUILD_sample_consensus: option to enable/disable building of sample_consensus library
BUILD_segmentation: option to enable/disable building of segmentation library
BUILD_surface: option to enable/disable building of surface library
BUILD_visualization: option to enable/disable building of visualization library
CMAKE_BUILD_TYPE: here you specify the build type. In CMake, a CMAKE_BUILD_TYPE corresponds to a set of options and flags passed to the compiler to activate/deactivate a functionality and to constrain the building process.
CMAKE_INSTALL_PREFIX: where the headers and the built libraries will be installed
PCL_SHARED_LIBS: option to enable building of shared libraries. Default is yes.
PCL_VERSION: this is the PCL library version. It affects the built libraries names.
VTK_DIR: directory of VTK library if found
The above are called cmake cached variables. At this level we only looked at the basic ones.
```

## issues 

(1) boost 1.66.0 API 错误: 

```bash
[ 68%] Building CXX object surface/CMakeFiles/pcl_surface.dir/src/on_nurbs/fitting_cylinder_pdm.cpp.o
In file included from /usr/local/include/boost/asio/impl/write.hpp:25:0,
                 from /usr/local/include/boost/asio/write.hpp:927,
                 from /usr/local/include/boost/asio/buffered_write_stream.hpp:29,
                 from /usr/local/include/boost/asio/buffered_stream.hpp:22,
                 from /usr/local/include/boost/asio.hpp:41,
                 from /home/magic/opt/pcl/pcl/apps/src/openni_octree_compression.cpp:56:
/usr/local/include/boost/asio/detail/consuming_buffers.hpp: In member function ‘boost::asio::detail::consuming_buffers<Buffer, Buffers, Buffer_Iterator>::prepared_buffers_type boost::asio::detail::consuming_buffers<Buffer, Buffers, Buffer_Iterator>::prepare(std::size_t)’:
/usr/local/include/boost/asio/detail/consuming_buffers.hpp:105:50: error: parse error in template argument list
     while (next != end && max_size > 0 && result.count < result.max_buffers)
                                                  ^
...
apps/CMakeFiles/pcl_openni_octree_compression.dir/build.make:62: recipe for target 'apps/CMakeFiles/pcl_openni_octree_compression.dir/src/openni_octree_compression.cpp.o' failed
make[2]: *** [apps/CMakeFiles/pcl_openni_octree_compression.dir/src/openni_octree_compression.cpp.o] Error 1
CMakeFiles/Makefile2:2230: recipe for target 'apps/CMakeFiles/pcl_openni_octree_compression.dir/all' failed
make[1]: *** [apps/CMakeFiles/pcl_openni_octree_compression.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
Makefile:149: recipe for target 'all' failed
make: *** [all] Error 2
```

解决方案:  

The patch above is needed to update the boost API.

However, even with the patch applied, domoticz will not compile with g++5; it compiles fine with g++6. Apparently, the boost header file boost/asio/detail/consuming_buffers.hpp triggers a parsing error in g++5. I'm not a c++ programmer, so excuse me if this explanation is not accurate. I figured g++ thinks it's a template invocation and chokes. To circumvent this, you can just add parenthesis around result_count in the header file. I have suggested that workaround to the boost developers. Meanwhile, you can apply the following patch to boost and domoticz will compile.

```diff
--- a/boost/asio/detail/consuming_buffers.hpp
+++ b/boost/asio/detail/consuming_buffers.hpp
@@ -102,7 +102,7 @@ public:

     std::advance(next, next_elem_);
     std::size_t elem_offset = next_elem_offset_;
-    while (next != end && max_size > 0 && result.count < result.max_buffers)
+    while (next != end && max_size > 0 && (result.count) < result.max_buffers)
     {
       Buffer next_buf = Buffer(*next) + elem_offset;
       result.elems[result.count] = boost::asio::buffer(next_buf, max_size);
```

(32) 消除 Imported targets not available for Boost version 106300警告提示 原
 lieefu   lieefu 发布于 2016/12/31 09:04 字数 230 阅读 1779 收藏 0 点赞 0  评论 0
使用新版本的boost库，运行cmake编译程序时，遇到警告信息： Imported targets not available for Boost version 106600，

这是由于cmake版本旧，boost版本新，cmake带来的FindBoost.cmake，

编辑/usr/share/cmake-3.5/Modules/FindBoost.cmake文件，搜索Imported targets not available for Boost version ${Boost_VERSION}
在这个if语句最后加入，内容可以复制对上个版本的内容或者把版本好加大：

elseif(NOT Boost_VERSION VERSION_LESS 106600 AND Boost_VERSION VERSION_LESS 106800)
    set(_Boost_CHRONO_DEPENDENCIES system)
    set(_Boost_CONTEXT_DEPENDENCIES thread chrono system date_time)
    set(_Boost_COROUTINE_DEPENDENCIES context system)
    set(_Boost_FIBER_DEPENDENCIES context thread chrono system date_time)
    set(_Boost_FILESYSTEM_DEPENDENCIES system)
    set(_Boost_IOSTREAMS_DEPENDENCIES regex)
    set(_Boost_LOG_DEPENDENCIES date_time log_setup system filesystem thread regex chrono atomic)
    set(_Boost_MATH_DEPENDENCIES math_c99 math_c99f math_c99l math_tr1 math_tr1f math_tr1l atomic)
    set(_Boost_MPI_DEPENDENCIES serialization)
    set(_Boost_MPI_PYTHON_DEPENDENCIES python mpi serialization)
    set(_Boost_RANDOM_DEPENDENCIES system)
    set(_Boost_THREAD_DEPENDENCIES chrono system date_time atomic)
    set(_Boost_WAVE_DEPENDENCIES filesystem system serialization thread chrono date_time atomic)
    set(_Boost_WSERIALIZATION_DEPENDENCIES serialization)
  else()
    message(WARNING "Imported targets not available for Boost version ${Boost_VERSION}")
    set(_Boost_IMPORTED_TARGETS FALSE)
  endif()

(3) fatal error: pcl/visualization/pcl_visualizer.h: No such file or directory

默认情况下是不会安装 visualizer 模块的, 需要手动在 ccmake 的配置界面开启. 然后重新编译安装.    


## 参考  

- PCL 官网: http://pointclouds.org/documentation/tutorials/  