# Windows 10 - VS2015 编译 G2O  

> https://blog.csdn.net/aptx704610875/article/details/51245143 


## Requirements

* cmake             http://www.cmake.org/  
* Eigen3            http://eigen.tuxfamily.org  

### Optional requirements

* suitesparse       http://faculty.cse.tamu.edu/davis/suitesparse.html  
* Qt5               http://qt-project.org  
* libQGLViewer      http://www.libqglviewer.com/  

## Compilation

Our primary development platform is Linux. Experimental support for
Mac OS X, Android and Windows (MinGW or MSVC).   

We recommend a so-called out of source build which can be achieved
by the following command sequence.

On Windows with `vcpkg` the following two commands will generate build scripts for Visual Studio 2015 MSVC 14 tool set:

- `mkdir build`
- `cd build`
- `cmake -G "Visual Studio 14 2015 Win64" -DG2O_BUILD_APPS=ON -DG2O_BUILD_EXAMPLES=ON -DVCPKG_TARGET_TRIPLET="%VCPKG_DEFAULT_TRIPLET%" -DCMAKE_TOOLCHAIN_FILE="%VCPKG_ROOT_DIR%\scripts\buildsystems\vcpkg.cmake" ..`

If you are compiling on Windows and you are for some reasons **not** using `vcpkg` please download Eigen3 and extract it.   

Within cmake-gui set the variable `EIGEN3_INCLUDE_DIR` to that directory.   

在 CmakeLists.txt 中添加下面两行, 其中 QT5_DIR 那一行是可选的 (需要安装 QT5).  

```
set(EIGEN3_INCLUDE_DIR D:/workSpace/thirdparty20170624/eigen3) 
set(Qt5_DIR D:/Qt/Qt5.10.0/5.10.0/winrt_x64_msvc2015/lib/cmake/Qt5)
```

然后执行下面的 cmake 命令:   

- `cmake -G "Visual Studio 14 2015 Win64" ..`  

cmake 成功后会生成 g2o.sln, 用 VS2015 打开后生成解决方案即可, 成功编译后会打印一下信息:    

```bash
1>------ 已启动生成: 项目: stuff, 配置: Release x64 ------
2>------ 已启动生成: 项目: opengl_helper, 配置: Release x64 ------
3>------ 已启动生成: 项目: csparse, 配置: Release x64 ------
4>------ 已启动生成: 项目: freeglut_minimal, 配置: Release x64 ------
5>------ 已启动生成: 项目: parser_library, 配置: Release x64 ------
    2>  opengl_primitives.cpp
    1>  os_specific.c
    1>    正在创建库 D:/workSpace/thirdparty20170624/g2o/bin/Release/g2o_stuff.lib 和对象 D:/workSpace/thirdparty20170624/g2o/bin/Release/g2o_stuff.exp
...
...
...
49>  sclam_pure_calibration.cpp
46>  Building Custom Rule D:/workSpace/thirdparty20170624/g2o/g2o/apps/g2o_simulator/CMakeLists.txt
46>  CMake does not need to re-run because D:/workSpace/thirdparty20170624/g2o/build/g2o/apps/g2o_simulator/CMakeFiles/generate.stamp is up-to-date.
46>  test_simulator2d.cpp
48>  sclam_odom_laser.vcxproj -> D:\workSpace\thirdparty20170624\g2o\bin\Release\sclam_odom_laser.exe
47>  sclam_laser_calib.vcxproj -> D:\workSpace\thirdparty20170624\g2o\bin\Release\sclam_laser_calib.exe
40>  tutorial_slam2d.vcxproj -> D:\workSpace\thirdparty20170624\g2o\bin\Release\tutorial_slam2d.exe
49>  sclam_pure_calibration.vcxproj -> D:\workSpace\thirdparty20170624\g2o\bin\Release\sclam_pure_calibration.exe
44>  g2o_simulator3d_application.vcxproj -> D:\workSpace\thirdparty20170624\g2o\bin\Release\g2o_simulator3d.exe
45>  convertSegmentLine_application.vcxproj -> D:\workSpace\thirdparty20170624\g2o\bin\Release\convertSegmentLine.exe
42>  gicp_sba_demo.vcxproj -> D:\workSpace\thirdparty20170624\g2o\bin\Release\gicp_sba_demo.exe
43>  sba_demo.vcxproj -> D:\workSpace\thirdparty20170624\g2o\bin\Release\sba_demo.exe
41>  gicp_demo.vcxproj -> D:\workSpace\thirdparty20170624\g2o\bin\Release\gicp_demo.exe
46>  g2o_simulator2d_application.vcxproj -> D:\workSpace\thirdparty20170624\g2o\bin\Release\g2o_simulator2d.exe
50>------ 已启动生成: 项目: ALL_BUILD, 配置: Release x64 ------
50>  Building Custom Rule D:/workSpace/thirdparty20170624/g2o/CMakeLists.txt
50>  CMake does not need to re-run because D:/workSpace/thirdparty20170624/g2o/build/CMakeFiles/generate.stamp is up-to-date.
========== 生成: 成功 50 个，失败 0 个，最新 1 个，跳过 0 个 ==========
```

生成的 dll 和 lib 文件位于 ../bin/Release 目录中, 将其添加到系统环境变量中即可.   

## Open-MVO

(1) 在项目中设置使用 g2o.   

1) 顶层 CMakeLists.txt 中添加一行:  

```
SET(G2O_ROOT D:/workSpace/thirdparty20170624/g2o)
```

(2) 修改 Findg2o.cmake:  

1) 在 FIND_LIBRARY("${MYLIBRARY}_DEBUG" 函数中添加:  

```cmake
    ${G2O_ROOT}/bin/Debug
```

2) 在 FIND_PATH(G2O_INCLUDE_DIR g2o/core/base_vertex.h 函数中添加:   

```
  ${G2O_ROOT}
```

3) 在 FIND_LIBRARY(${MYLIBRARY} 中添加:   

```
    ${G2O_ROOT}/bin/Release
```

### 2. 

```cpp
#define M_PI 3.14159265358979323846
```

### 3. 尝试引用已删除的函数

```
Eigen::Block<Eigen::Block<Eigen::Map<Eigen::Matrix<double,-1,-1,0,-1,-1>,0,Eigen::Stride<0,0>>,-1,-1,false>,-1,-1,false> &Eigen::Block<Eigen::Block<Eigen::Map<Eigen::Matrix<double,-1,-1,0,-1,-1>,0,Eigen::Stride<0,0>>,-1,-1,false>,-1,-1,false>::operator =(const Eigen::Block<Eigen::Block<Eigen::Map<Eigen::Matrix<double,-1,-1,0,-1,-1>,0,Eigen::Stride<0,0>>,-1,-1,false>,-1,-1,false> &): 尝试引用已删除的函数
...

```


But that definition is not enabled if EIGEN_COMP_MSVC_STRICT is true.
Could you change line 595 in src/Core/util/Macros.h to:

```cpp
#if EIGEN_COMP_MSVC_STRICT && EIGEN_COMP_MSVC < 1900
```

and report what happens?
Comment 2 Michael Hofmann 2014-12-16 17:42:15 UTC
My version of src/Core/util/Macros.h (from tip of default) doesn't even have that many lines (it has 468), but I have changed line 340 like this:

$ hg diff
diff -r 3cc5093598e5 src/Eigen/Eigen/src/Core/util/Macros.h
--- a/src/Eigen/Eigen/src/Core/util/Macros.h    Tue Dec 16 15:49:46 2014 +0100
+++ b/src/Eigen/Eigen/src/Core/util/Macros.h    Tue Dec 16 17:15:00 2014 +0100
@@ -337,7 +337,7 @@

```cpp
 // just an empty macro !
 #define EIGEN_EMPTY

-#if defined(_MSC_VER) && (!defined(__INTEL_COMPILER))
+#if defined(_MSC_VER) && (_MSC_VER < 1900) && (!defined(__INTEL_COMPILER))
 #define EIGEN_INHERIT_ASSIGNMENT_EQUAL_OPERATOR(Derived) \
   using Base::operator =;
 #elif defined(__clang__) // workaround clang bug (see http://forum.kde.org/viewtopic.php?f=74&t=102653)
```

This fixes the above compiler error but triggers another error further up the chain, in MapBase<>:

使用新版本的 Eigen, 更改 OpenMVO-master\cmake\script_eigen.cmake 文件中:  

```cmake
SET(EIGEN_EMBEDDED_INCLUDE_DIR "D:/workSpace/thirdparty20170624/eigen3.3.7/" CACHE PATH "Eigen path for embedded use")
```

为新版本的 Eigen 路径即可.  


##  无法解析的外部符号 

```
openmvo_mvo.lib(depth_filter.obj) : error LNK2019: 无法解析的外部符号  
"public: bool __cdecl mvo::Matcher::findEpipolarMatchDirect(class mvo::Frame const &,class mvo::Frame const &,struct mvo::Feature const &,double,double,double,double &)" (?findEpipolarMatchDirect@Matcher@mvo@@QEAA_NAEBVFrame@2@0AEBUFeature@2@NNNAEAN@Z)，该符号在函数  
"protected: void __cdecl mvo::DepthFilter::updateSeeds(class std::shared_ptr)" (?updateSeeds@DepthFilter@mvo@@IEAAXV?$shared_ptr@VFrame@mvo@@@std@@@z) 中被引用   
```

仔细观察后可以发现, 两个函数中均有 Frame 参数, 但是在 C++ 库的符号表中, 二者并不相同.  

mvo::Matcher::findEpipolarMatchDirect() 中生成的 Frame 符号表为:  

```cpp
QEAA_NAEBVFrame
```

mvo::DepthFilter::updateSeeds() 函数中生成的 Frame 符号表为:  

```cpp
VFrame
```

初步判断 Error 的原因是: 未正确包含定义 Frame 类的头文件.  

1) 方法是在 matcher.cpp 中把 `#include  matcher.h` 放到包含的头文件的最后;  
2) 由于 UTF-8 文件编码错误( 这个问题普遍存在于整个工程中 );   

**参考**:  

> https://blog.csdn.net/enotswn/article/details/5934938  
> C++头文件的包含顺序研究: https://blog.csdn.net/clever101/article/details/7269058  
