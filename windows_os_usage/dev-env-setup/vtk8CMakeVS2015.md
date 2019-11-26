# VS2015 CMake 编译 VTK-8.0.0 得到 qvtkWidget 控件  

**注意: VTK 版本过低会导致后期编译好的 QT exe 程序运行崩溃.**  

> 首先说明一下 VTK-8.0.0 版本的选择原因, VTK-7.1.1 对应的 QT 控件程序会运行失败; 如果使用过高的版本 (如 VTK-8.2.0), 也会出现文末最后提到的问题.   

## 1 VTK 下载

下载 VTK 源码后切换到 v8.0.0 分支.  

```bash
git clone https://gitlab.kitware.com/vtk/vtk
git checkout v8.0.0
```

## 2. CMake 配置 VTK for Qt 编译环境  

2.1) 启动 CMake-GUI，指定源码目录和编译目录，点击 Configure。  

```bash
D:/thirdparty20170624/VTK-8.2.0  
D:/thirdparty20170624/VTK-8.2.0/build  
```

2.2) 指定 VS 版本  

64 位选 Visual Studio 14 2015 Win64，32 位选 Visual Studio 14 2015。点击 finish，等待配置完成, 这可能需要几分钟的时间。  


2.3) 配置编译选项（1）  

a) BUILD 选项: 选择 BUILD_EXAMPLES，BUILD_SHADRED_LIBS，BUILD_TESTING。  

**注意：**  

- 不建议选择 DOCUMENTATION，这需要先安装 doxygen。  
- 不建议去掉 TESTING，这会导致在后期 VS 编译阶段报错，需要修改头文件。  

b) 设置 VTK 安装目录 - CMAKE_INSTALL_PREFIX : C:/PCL_181/3rdParty/VTK8_0_0, 用于安装 include，lib，dll(bin) 等编译结果的目录。  

c) VTK_Group_Qt: 这里设置编译的目标环境为 Qt。  
 
完成上述三个设置后，点击 Configure。  

2.4) 配置编译选项（2）  

第 1 次配置完成后，会提示用户输入 QT_QMAKE_EXECUTABLE 和 VKT_QT_VERSION. 将 QT_QMAKE_EXECUTABLE 选项设置为 C:/QT5_10_0/5.10.0/msvc2015_64/bin/qmake.exe; 将 VKT_QT_VERSION 选项设置为 5, 再次点击 Configure 继续.  

2.5) 配置编译选项（3）
 
第 2 次配置完成后，会提示用户输入 Qt5_DIR. 将 Qt5_DIR 选项设置为 C:/QT5_10_0/5.10.0/msvc2015_64/lib/cmake/Qt5, 再次点击 Configure 继续。

下面的这些变量会被自动填充:  

- Qt5Core_DIR 选项设置为  C:/QT5_10_0/5.10.0/msvc2015_64/lib/cmake/Qt5Core;  
- Qt5Gui_DIR 选项设置为  C:/QT5_10_0/5.10.0/msvc2015_64/lib/cmake/Qt5Gui;  
- Qt5Sql_DIR 选项设置为  C:/QT5_10_0/5.10.0/msvc2015_64/lib/cmake/Qt5Sql;  
- Qt5UiPlugin_DIR 选项设置为  C:/QT5_10_0/5.10.0/msvc2015_64/lib/cmake/Qt5UiPlugin;  
- Qt5Widgets_DIR 选项设置为  C:/QT5_10_0/5.10.0/msvc2015_64/lib/cmake/Qt5Widgets.  

2.6) Generate工程

配置成功后，会出现 Configure done 提示。然后点击 Generate 生成 .sln 工程。  

2.7) 启动 VS 2015 开始编译

在编译目录 D:/thirdparty20170624/VTK-8.2.0/build 下打开 VTK.sln 工程。  

## 3. 在 VS 2015 中编译 VTK 工程  

3.1) 编译  

a) 打开工程后，默认启动项为 ALL_BUILD，直接选择生成即可。  
b) Debug 和 Release 版本都需要生成，所以要执行两次编译。  

请耐心等待......直至编译成功。  

3.2) 安装  

选择 INSTALL 项目, 右键点击 "生成"。 其实这一步可以省略, 直接使用 build 目录中的 dll 文件和 lib 文件. 因为安装后的 dll 文件没有区分 Release 和 Debug 版本。  

3.3) 编译结果  

VS 2015 的编译结果主要包括 4 个部分：  

- include: 不区分 Release 和 Debug 版本;  
- lib: 不区分版本;  
- dll: 根据输入配置选择 Debug 和 Release 版本;  
- plugin dll: 只有 Release 版本可用.  

## 4、Qt Designer下安装 QVTKWidget 插件  

4.1) 安装  

将 "C:\VTK\VTK-8.0.01\build\bin\Release\QVTKWidgetPlugin.dll" 复制到 "C:\QT5_10_0\5.10.0\msvc2015_64\plugins\designer" 目录。 

注意：一定要复制 Release 版本的 QVTKWidgetPlugin.dll。  

**验证**  

启动 Qt Designer, 在左侧 widget box 的最下方可以看到 QVTKWidget，说明安装成功。  

Qt Creator 环境下的 designer 是看不见 QVTKWidget 插件的，所以不能直接拖放。需先拖放 QWidget，然后再选择 QWidget 提升为 QVTKWidget。  

## ISSUES  

1) PCL-1.8.1 + VTK-8.2.0: `error: ‘class vtkDataSetMapper’ has no member named ‘ImmediateModeRenderingOff‘`  

c:\program files\pcl 1.9.1\3rdparty\vtk\include\vtk-8.1\vtkmapper.h(218): note: 参见“vtkMapper::ImmediateModeRenderingOff”的声明

在 PCL-1.8.1 环境下编译 Qt VTK-8.2.0 程序时出现:  

```bash
xxx:87:11: error: ‘class vtkDataSetMapper’ has no member named ‘ImmediateModeRenderingOff’
   mapper->ImmediateModeRenderingOff ();
```
 
经过一番搜索之后，发现是因为 VTK-8.1.0 之后的版本中将 vtkMapper 的 ImmediateModeRenderingOff() 方法移除了.  

解决办法: 将错误提示中对应的那一行代码注释掉即可，或者更换为更低版本的 VTK-8.0.0 也行。最简单的方法是注释掉上述出错的两行代码，因为ImmediateModeRenderingOff() 方法实现的功能并不是必须的操作。  

