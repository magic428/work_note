# Ubuntu 16.04 安装 boost 库  

> 不建议使用 apt install 之后的包, 其中的很多功能都是是无法正常使用的.  
> boost 版本确定: 先安装 ros, 然后查看 ros 使用的 boost 版本, 最后自己下载编译对应的 boost 版本安装, 这样就不会造成系统内部的 boost 版本冲突.   

接下来开始安装.  

到 boost 官网安装一个boost库的压缩包，我下的是 1.67.0 版本. 执行下面的命令解压:  

```bash
tar -xzvf boost_1_67_0.tar.gz
```
解压出来以后，进入解压出来的文件夹，执行下面的命令安装依赖库,   

```bash
sudo apt-get install libbz2-dev
```

否则会在编译 `libboost_iostreams.so` 的时候出错.  然后执行下面的命令进行配置:  

```bash
sudo ./bootstrap.sh
```

在执行下面的命令，这样头文件就被默认安装在 /usr/local/include 头文件下，库文件就被默认安装在 /usr/local/lib 下:  

```bash
b2 toolset=gcc cxxflags="-std=c++11"
sudo ./b2 install
```

这个时候就已经安装好了，不过在编译的时候可能还会有一点小问题，比如有下面的代码:  

```cpp
#include <iostream>
#include <boost/regex.hpp>
#include <boost/algorithm/string.hpp>
using namespace std;

int main(){
    string str = "data-num=\"1056\"";
    boost::regex reg("\\d{1,6}");//{1,6}表示\d重复1-6次，\d表示匹配整数
    boost::smatch what;
    string::const_iterator begin = str.begin();
    string::const_iterator end = str.end();

    boost::regex_search(begin,end,what,reg);
    string result(what[0].first,what[0].second);
    cout << result << endl;
    return 0;
}
```

这里用到了一个regex.hpp的库，那么我们在编译的时候会还需要加上相应库的链接，如下（-I选项是添加头文件的路径，-L选项是添加库文件的路径，-l是具体哪个库文件）

```bash
g++ -o test test.cc -std=c++11  -I /usr/local/include -L /usr/local/lib  -lboost_regex
```

如果执行起来碰到下面的问题  

./test: error while loading shared libraries: libboost_regex.so.1.67.0: cannot open shared object file: No such file or directory  

这是因为系统不知道 ***.so 文件在哪个位置，找不到该文件。这个时候就要在 /etc/ld.so.conf 中加入 xxx.so 所在的目录: /usr/local/lib，所以要在该文件中末尾加入这样路径。添加完以后执行下面的命令:  

```bash
sudo ldconfig
```

这样就可以编译通过了.    


## issues  

1. Imported targets not available for Boost version 106600

```
CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106600
Call Stack (most recent call first):
```

这是由于 FindBoost.cmake 发布文件相对较早, 当时尚未发布对应的 boost 版本. 只需添加进入我们的版本就可以了.    

打开 /usr/share/cmake-3.5/Modules/FindBoost.cmake 文件, 在 725 行处添加如下内容:  

```
elseif(NOT Boost_VERSION VERSION_LESS 106200 AND Boost_VERSION VERSION_LESS 106800)
    set(_Boost_CHRONO_DEPENDENCIES system)
    set(_Boost_COROUTINE_DEPENDENCIES context system)
    set(_Boost_FILESYSTEM_DEPENDENCIES system)
    set(_Boost_IOSTREAMS_DEPENDENCIES regex)
    set(_Boost_LOG_DEPENDENCIES date_time log_setup system filesystem thread regex chrono atomic)
    set(_Boost_MATH_DEPENDENCIES math_c99 math_c99f math_c99l math_tr1 math_tr1f math_tr1l atomic)
    set(_Boost_MPI_DEPENDENCIES serialization)
    set(_Boost_MPI_PYTHON_DEPENDENCIES python mpi serialization)
    set(_Boost_RANDOM_DEPENDENCIES system)
    set(_Boost_THREAD_DEPENDENCIES chrono system date_time atomic)
    set(_Boost_TIMER_DEPENDENCIES chrono system)
    set(_Boost_WAVE_DEPENDENCIES filesystem system serialization thread chrono date_time atomic)
    set(_Boost_WSERIALIZATION_DEPENDENCIES serialization)
```

2. 更换系统中的 boost 版本  

cmake 检测的是 `include/boost/version.hpp` 文件中的宏定义 `BOOST_LIB_VERSION`, 必须要删除 /usr/local/include/boost 和 /usr/local/lib/libboost_* 文件.  

然后再运行 `sudo ./b2 install` 重新安装 boost 头文件和库文件即可.  

切记: 一定要先删除原来的目录.  

```bash
sudo rm -rf /usr/local/include/boost 
sudo rm -rf /usr/local/lib/libboost_* 
```


