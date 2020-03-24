# WIN10 + VS2015 + PCL1.8.1 环境安装

## 1、准备工作：下载下面两个文件   

下载地址：http://unanancyowen.com/en/pcl181/

百度云链接：

- 安装文件： 链接：https://pan.baidu.com/s/1i69LGZr  密码：5jnt  
- PDB文件： 链接：https://pan.baidu.com/s/1kWWcrrx  密码：zri4  

**安装选项配置如下**:  

- 1) Add PCL to the system Path for all users;  
- 2) 选择安装路径，建议修改，默认安装路径中的Program files和PCL 1.8.1这两个文件名中都有空格，在qt中无法识别;  
- 3) 安装的组件：全选;  
- 4) 安装过程中会弹出 OpenNI2 对话框，设置安装路径到 PCL 安装目录下的 /3rdParty/OpenNI2/ 下;   
等待安装完成后, 解压 pcl-1.8.1-pdb-msvc2015-win64.zip 到 PCL 安装目录的下的 bin 目录下.  

安装过程中修改了路径，此处我的路径是：D:\PCL 1.8.1 ，选择了自动生成系统变量。

（解压后放在安装目录的bin下面）

[个人建议（此建议更于2018.5.4）：配置环境变量有许多缺陷，大家可以尝试使用cmake进行编译，只需要将所用的包在CMakelists文档中提前声明，而且易于移植至其他环境或PC上运行。可以参见：https://blog.csdn.net/uniqueyyc/article/details/80181388，查看官方文档的示例（例子linux，window通用）]

## 2、配置环境变量

如果安装时选择自动生成就无需修改，当然也可以自己改。   

PCL_ROOT: D:\Programs\PCL181
%PCL_ROOT%\bin;
%PCL_ROOT%\3rdParty\FLANN\bin;
%PCL_ROOT%\3rdParty\VTK\bin;
%OPENNI2_REDIST64%;

并且手动添加下图所示变量：

## 3. 使用 cmake 

安装完毕后需要修改 PCLConfig.cmake 文件中 OPENNI2_INCLUDE_DIRS_HINT 变量的值:  

```
if(NOT OPENNI2_ROOT AND ("TRUE" STREQUAL "TRUE"))
  set(OPENNI2_INCLUDE_DIRS_HINT "D:/Programs/PCL181/3rdParty/OpenNI2/Include")
  get_filename_component(OPENNI2_LIBRARY_HINT "D:/Programs/PCL181/3rdParty/OpenNI2/Lib/OpenNI2.lib" PATH)
endif()
```

然后就可以创建 C++ 工程, 使用下面的 cmake 语句就可以添加 PCL 库.   

```
set( PCL_DIR "D:/Programs/PCL181/cmake")
find_package(PCL 1.8.1 REQUIRED)
include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})
if (PCL_FOUND)
    message("PCL_VERSION: ${PCL_VERSION}")
    message("PCL_INCLUDE_DIRS: ${PCL_INCLUDE_DIRS}")
endif()
list(APPEND LINKER_LIBS ${PCL_LIBRARIES})
```

至此配置完毕，用网上例子检测运行。

```cpp
#include <iostream>  
#include <pcl/io/pcd_io.h>  
#include <pcl/point_types.h>  
#include <pcl/ModelCoefficients.h>  
#include <pcl/filters/project_inliers.h>  
  
int main(int argc, char** argv)  
{  
    pcl::PointCloud<pcl::PointXYZ>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZ>);  
    pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_projected(new pcl::PointCloud<pcl::PointXYZ>);  
  
    // Fill in the cloud data  
    cloud->width = 5;  
    cloud->height = 1;  
    cloud->points.resize(cloud->width * cloud->height);  
  
    for (size_t i = 0; i < cloud->points.size(); ++i)  
    {  
        cloud->points[i].x = 1024 * rand() / (RAND_MAX + 1.0f);  
        cloud->points[i].y = 1024 * rand() / (RAND_MAX + 1.0f);  
        cloud->points[i].z = 1024 * rand() / (RAND_MAX + 1.0f);  
    }  
  
    std::cerr << "Cloud before projection: " << std::endl;  
    for (size_t i = 0; i < cloud->points.size(); ++i)  
        std::cerr << "    " << cloud->points[i].x << " "  
        << cloud->points[i].y << " "  
        << cloud->points[i].z << std::endl;  
  
    // Create a set of planar coefficients with X=Y=0,Z=1  
    pcl::ModelCoefficients::Ptr coefficients(new pcl::ModelCoefficients());  
    coefficients->values.resize(4);  
    coefficients->values[0] = coefficients->values[1] = 0;  
    coefficients->values[2] = 1.0;  
    coefficients->values[3] = 0;  
  
    // Create the filtering object  
    pcl::ProjectInliers<pcl::PointXYZ> proj;  
    proj.setModelType(pcl::SACMODEL_PLANE);  
    proj.setInputCloud(cloud);  
    proj.setModelCoefficients(coefficients);  
    proj.filter(*cloud_projected);  
  
    std::cerr << "Cloud after projection: " << std::endl;  
    for (size_t i = 0; i < cloud_projected->points.size(); ++i)  
        std::cerr << "    " << cloud_projected->points[i].x << " "  
        << cloud_projected->points[i].y << " "  
        << cloud_projected->points[i].z << std::endl;  
  
    system("pause");  
    return (0);  
}  
```

希望对大家有帮助！

## 参考文献  

- 官方教材: http://pointclouds.org/documentation/tutorials/using_pcl_pcl_config.php#using-pcl-pcl-config   

- http://blog.csdn.net/enigma_tong/article/details/58128983  
- http://blog.csdn.net/ldepn/article/details/75095283   
- http://blog.csdn.net/u014283958/article/details/52599457  
- http://blog.csdn.net/u011197534/article/details/52960394  
