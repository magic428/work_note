# VS2015-Cmake-Windows SDK 中出现的问题  

## issues

(1) The CXX compiler identification is unknown   

CMake 选择了 VS2015 进行编译配置，在执行 cmake 的时候，出现如下错误：  

```bash
$ cmake -G "Visual Studio 14 2015 Win64" ../

-- Selecting Windows SDK version 10.0.18362.0 to target Windows 10.0.17763.
-- The C compiler identification is unknown
-- The CXX compiler identification is unknown
CMake Error at CMakeLists.txt:2 (PROJECT):
  No CMAKE_C_COMPILER could be found.
```

上面的错误提示中包含了两个问题.  

**1) Selecting Windows SDK version 10.0.18362.0 to target Windows 10.0.17763**:  

说明 SDK 版本和windows 版本不匹配, 需要重新下载对应版本的 SDK: https://developer.microsoft.com/zh-cn/windows/downloads/sdk-archive.   

**2) The CXX compiler identification is unknown**:   

引起这个错误的原因是 CMake 找不到 C++ 的编译器，检查 VS 的安装目录 (C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin (此编译器与VS2015对应)) 中是否有 cl.exe 以及 rc.exe 和 rcdll.dll。

- 如果没有 cl.exe，那么可能是只安装了 VS，没有安装 VC 编译器，打开VS，选择 VC 安装即可;   
- 如果没有 rc.exe 和 rcdll.dll，这是编译资源用的，可能安装在 Windows SDK 中，直接复制这两个文件到 VC/bin 目录下即可。   

解决方案： 

(1) 把 C:\Program Files (x86)\Windows Kits\8.1\bin\x86 加入系统变量 PATH 中; 将 C:\Program Files (x86)\Windows Kits\8.1\bin\x64 (64 位编译器) 加入系统变量 PATH 中; 将 C:\Program Files (x86)\Windows Kits\8.1\bin\arm (arm 编译器) 加入系统变量 PATH 中;  
(2) 后把 C:\Program Files (x86)\Windows Kits\8.1\bin\x86 (x64 或 arm) 里的 rc.exe 和 rcdll.dll 复制粘贴到C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin (此编译器与 VS2015 对应) 文件夹中.
