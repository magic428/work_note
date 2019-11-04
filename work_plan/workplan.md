# 工作计划 TODO List

## 2017-11-16  

### personal   

1. caffe的源码 每天2个.cpp  
2. 传统图像处理, 基于opencv  
3. 论文阅读  


### official  

1. 去除分类检测到的噪点, 拆分检测到的动作, 判断最终的进入点和出去点  
2. 如何对检测到的数据做线性拟合？  


## 2018-07-30

### 1.yolo 训练和行人数据


- 熟悉 yolo 训练自定义数据的流程  

- 准备行人数据(从行人数据集合中挑选, 自己再从网上爬取一部分矿工数据)  

- 熟悉 yolo 需要的 Annotations 数据格式  

- 熟悉 VOC xml 标注数据到 yolo 标注数据的格式转换   

### 2.显著性检测算法优化思路  

整理 fasa 算法的核心思想, 学习了其中的亮点思路. 主要有以下几个切入点:  

(1) 引进边缘像素作为背景像素的先验;  
(2) 考虑像素在空间分布的信息, 作为显著值计算的权值;  
(3) 用 fast cluster 算法取代 RC 算法中的区域分割部分;  

## 2019-01-19  

### 1. 个人学习方面   

目的:  提高自己的核心竞争力.    

短板:  图像处理； 深度学习理论和前沿方法.   

策略:   

(1) 从理论层面完整学习 OpenCV 中涉及到的图像处理方法;   

(2) 根据 <统计学习方法> 学习机器学习理论知识;  

(3) 定时研究前沿方法(哪怕只是跑跑demo);   

(4) 了解主流的深度学习检测方法: faster-rcnn, mask-rcnn, mt-cnn;   

(5) 学习搭建浅层神经网络, 处理简单问题.  


(1), (2) 为知识储备, 是为长期计划.   

(3), (4), (5) 为目前工作阶段的紧迫计划.  


### 2.工作方面   

目的: 提高自己的工作积极性和考虑问题的深度.   

How: 以 "创新研究" 为导向开展工作. 想办法提高自己研究内容的核心竞争力(可复制性和应用意义).   

策略:  
 
(1) 一定要重视理论的夯实;   

(2) 计划没有做到细化为每一天的连贯性工作量;   

(3) 前期准备工作一定要多方面考量(比如测试数据, 样本数据的质量是否满足场景要求?);  

## 榆家梁出差期间的工作汇总   

1. 将去雾算法打包成 setup.exe 安装包  

遇到的问题:   
（1）打包 32 位程序时, 使用对应的 32 位库文件包. 如果使用 cmake,  记得不要加“Win64”；  
（2）32位平台上关于临时字符串变量的 c_str() 返回值错误问题；  
（3）安装程序会在公用用户目录中生成快捷方式, 需设置 General Information | ALLUSERS=“”；  
（4）打包方法:  https://www.cnblogs.com/xinaixia/p/5473815.html；  
（5）设置安装路径拷贝配置文件 .ini；
（6）TODO:  如何保证快捷方式的运行路径和原文件的运行路径一致？  
VS2015C#使用Install Shield创建快捷方式为何属性中“目标”和“目标位置”为灰色: https://blog.csdn.net/qq_39985392/article/details/78198271

序列号： 3F4A2QW-D2D-C16CCDD1CN

依然存在的花屏问题. . . 
雾气流动造成的 block 闪烁问题. . . . 
记录实验结果. . . 

2. yolov3 windows 版本

（1）调试 windows_rtsp 版本时遇到的 darknet 中的 det.data 未赋值引起的指针异常问题；  
（2）编译 yolo_cpp_dll 模块时遇到的 x86 和 x64 不匹配导致加载库失败；
（3）C# 中导入 .dll 时, 如果是复制的, 不要忘记修改函数符号；
（4）char* 和 byte[] 之间的跨语言类型转换；
（5）byte[] a = null; 表示空字符指针；
（6）将 dll 中的打印信息显示出来:  属性 | 调试 | 启动本机代码调试；
（7）使用 C# 调用 C++ dll 库:  https://www.cnblogs.com/94cool/p/5772376.html；
 https://www.cnblogs.com/cyf-besti/p/5325186.html


OpenCV 的 C API 接口的使用；  
自动车牌识别系统,  EasyPR；  
图像处理基础技术；  

[h264 @ 04422b60] left block unavailable for requested intra mode at 0 39
[h264 @ 04422b60] error while decoding MB 0 39, bytestream (6557)
[h264 @ 04422b60] error while decoding MB 75 43, bytestream (-8)
[h264 @ 043c0060] left block unavailable for requested intra4x4 mode -1 at 0 38
[h264 @ 043c0060] error while decoding MB 0 38, bytestream (10226)
[h264 @ 043c0060] error while decoding MB 54 14, bytestream (-6)
[h264 @ 04422b60] error while decoding MB 51 42, bytestream (-6)
[h264 @ 043c0060] error while decoding MB 63 12, bytestream (-6)
[h264 @ 043c0060] left block unavailable for requested intra4x4 mode -1 at 0 42
[h264 @ 043c0060] error while decoding MB 0 42, bytestream (4169)
[h264 @ 04422b60] error while decoding MB 43 44, bytestream (-14)
[h264 @ 043c0060] left block unavailable for requested intra4x4 mode -1 at 0 40
[h264 @ 043c0060] error while decoding MB 0 40, bytestream (8922)
[h264 @ 040adb60] left block unavailable for requested intra4x4 mode -1 at 0 36
[h264 @ 040adb60] error while decoding MB 0 36, bytestream (16462)
[h264 @ 040adb60] error while decoding MB 63 40, bytestream (-6)
[h264 @ 040adb60] left block unavailable for requested intra4x4 mode -1 at 0 43
[h264 @ 040adb60] error while decoding MB 0 43, bytestream (2322)
[h264 @ 043c0060] error while decoding MB 45 44, bytestream (-10)
[h264 @ 040adb60] left block unavailable for requested intra4x4 mode -1 at 0 23
[h264 @ 040adb60] error while decoding MB 0 23, bytestream (27435)


## 2019-06-19

deadline: 材料提交时间: 7 月 12 日下班前

天玛公司 2019 年度青年科技论文演讲比赛 

> 论文要求: 参赛论文应反映当前国内外相关学科领域的前沿进展或重要研究成果, 具有较高理论水平、学术价值或较强技术创新性. 

> 请选手规范标注专业类别, 比赛设置采矿组、煤机装备组、地质安全组、清洁利用及新兴专业组、工程建设与管理科学组 5 个专业组. 

> 演讲要求: 主题鲜明, 层次清晰, 内容富创新性. 

> 参赛者仪表端正、语言标准、表达流畅、具感染力. 

> 演讲时间为12分钟. 题目自拟. 

> 论文演讲比赛通过现场PPT展示的方式进行, PPT模板不作统一规定. 评分细则另行通知. 

> 初赛演讲时间: 2019年7月19日(周五)

比赛将从参赛选手的"论文写作"和"现场演讲"两方面进行综合评选. 比赛设置一等奖 1 名, 二等奖 2 名, 三等奖 3 名, 最佳新人奖 1 名,最佳 ppt 制作奖1名,最佳台风奖 1 名,优秀奖若干. 

参赛论文应是尚未公开发表的或 2018 年及以后（含 2018 年）发表的科技论文, 且参赛选手应为第一作者.  未发表论文请按统一格式要求撰写（附件2）. 

选手每人限投1篇文章、1个专业组, 不得一稿多投或多次参赛. 

1.报名时间: 2019年5月24日（周五）下班前, 各部门完成初选并报送最终参赛人选;  

2.材料提交时间: 7月12日下班前, 将论文材料及ppt文件报至马楠处（分机: 8050, 邮箱: manan@tdmarco.com）. 参赛选手于7月18日（周四）抽签确认比赛顺序.   

3.比赛时间: 2019年7月19日（周五）全天及7月26日（周五）.   

4.比赛地点: 天地大厦123会议室.   


## 2019-06-24

1、 确定煤岩分界检测的初步方案, 开始基于语义分割网络模型的训练. 
2、 完成井下人员、大块煤、错茬异常检测模型的测试分析. 
3、 查阅相关文献资料, 初步探索基于KITTI数据集的激光点云数据与可见光图像的融合方法. 
4、 继续优化实时去雾算法. 

## 2019-07-04

基于图像处理的井下工作面视频去雾和雾浓度检测   
正则化的意义  
MRF 的应用场景和解决的问题  
最大似然估计在图像处理中的应用   
HSV-YUV-RGB 空间的转换及其适用场景  


Haze Detection and Removal in High Resolution Satellite Image with Wavelet Analysis 

## 2019-08-03  

上湾电脑的 IP 配置：  ![](sw-ipconfig.png)

上湾煤矿出差基本信息记录:  

1) 上湾矿 camera Ip：   

```json
破碎机处

10.210.142.181   # 常用位置
10.210.142.225
10.210.142.232
10.210.142.169

登录名：admin
密码：admin12345

rtsp://admin:admin12345@10.210.142.181:554/h264/ch1/main/av_stream
```

2) 榆家梁 camera IP   

```json
rtsp://admin:admin1234@10.224.41.48:554/h264/ch1/main/av_stream
//rtsp://admin:admin1234@10.224.41.48:554/cam/realmonitor?channel=1&subtype=0
```

3) 视频流录屏软件  

https://www.liveqing.com/docs/download/LiveNVR.html  

4） TeamViewer14试用版到期怎么解决-TeamViewer14无限试用版  

https://blog.csdn.net/weixin_38293850/article/details/87969560    

## 2019-08-07  

- 将采集到的视频裁剪为图片;  
- 挑选出含有感兴趣目标的图片;  
- 确定标注原则;  
- 开始标注;  

点云数据的转换和 C++ 实现.  

- 点云数据投影到图像平面;  
- 剔除无效的投影点;  
- 使用距离作为颜色绘制点;  
- 将 RGB 颜色值反投影到点云中;  
- 使用 PCL 库可视化最终结果;  


## 南京北路相机 rtsp 

rtsp://admin:root1234@192.168.1.64:554/h264/ch1/main/av_stream  

## 出差北京准备煤展会   

> 2019.10.08 - 2019.10.30  

### 1. extern "C" {} 的作用   

被 extern "C" 修饰的变量和函数是按照 C 语言方式进行编译和链接的：这点很重要！！！ 其主要作用是为了能够正确实现 C++ 代码调用其他 C 语言代码. 由于 C++ 支持函数重载, 因此编译器编译函数的过程中会将函数的参数类型也加到编译后的代码中, 而不仅仅是函数名；而 C 语言并不支持函数重载, 因此编译 C 语言代码的函数时不会带上函数的参数类型, 一般只包括函数名.   

extern "C" 可以包含头文件, 相当于头文件中的声明都加了 extern "C"：  

```cpp
extern "C"
{
    #include <cmath>
}
```

### 5. vs 编译 live555 为静态链接库和动态链接库

1. 静态编译 (可实现)

1) 我们从http://live555.com/liveMedia/public下载最新版的live555工程。将工程解压于C:\live（该路径可自己设定）下。
2) 配置编辑环境：打开VS开发环境的选项，点击工具-选项-项目与解决方案-VC++目录，下拉对列表框中选定：inlcue files，添加：C:\live\BasicUsageEnvironment\include；C:\LIVE\GROUPSOCK\INCLUDE；C:\LIVE\USAGEENVIRONMENT\INCLUDE；C:\LIVE\LIVEMEDIA\INCLUDE。
3) 新建Win32 Static Library工程，工程名为BasicUsageEnvironment 位置 C:\live\BasicUsageEnvironment 点击下一步-完成。将live555工程中BasicUsageEnvironment文件夹下.cpp文件添加至工程源文件中，将include文件夹下文件添加至工程头文件夹中。在工程属性-连接器-输出中输入 ..\lib\BasicUsageEnvironment.lib，然后编译即可在live目录下lib文件夹中生成BasicUsageEnvironment.lib。同样建立GROUPSOCK、UsageEnvironment、liveMedia工程，最后得到另外三个lib。
4) 将BasicUsageEnvironment、GROUPSOCK、UsageEnvironment、liveMedia四个工程的头文件和lib加到其他工程中，这是就可以使用live555了。

2. 动态编译

1，2步同上。
3、新建DLL工程，工程名为live555，将live555源代码中BasicUsageEnvironment、GROUPSOCK、UsageEnvironment、liveMedia下所有c、cpp文件均添加到工程，然后在链接器里依赖项添加ws2_32.lib。
      但是dll没有导出函数，这个怎么弄？



## td_lwai.exe error:  

1. concealing 3342 DC 3342 AC 3342MV errors in P frame   

由 FFMPEG 的解码函数导致.  

**solution1**: 此问题由相机生成, 因此通过GANZ技术支持升级相机最新固件. 此h.264视频压缩不支持相机.   

如果你正在使用 UDP, 你可以期望丢弃帧 - 这是UDP设计的一部分, 它有利于速度而不是可靠性. 丢失数据包对于H264格式来说是一个严重问题, 因为给定数据包可能依赖于它前面或后面的数据包（使用差异图像而不是发送全新图像）. 因此, 使用UDP会产生很多错误, 包括“RTP：错过XXX数据包”. 

通过传递 rtsp_transport="tcp" 选项切换到更可靠但速度更慢的 TCP av_open_input. 例：

```cpp
AVDictionary * opts = NULL;
av_dict_set(&opts, "rtsp_transport", "tcp", 0);
int error = avformat_open_input(&rtsp_format_context, "rtsp://your url here", NULL, &opts);
if (error < 0)
    ; // Connection error. Add your error handling here.
```

这将阻止丢弃数据包, 消除视频损坏.  


## 参考资料  

opencv 读取 rtsp 视频流并保存为图片后花屏卡顿的问题: https://bbs.csdn.net/topics/392441165  
FFmpeg源代码简单分析：avformat_alloc_output_context2() https://blog.csdn.net/leixiaohua1020/article/details/41198929  
EasyDarwin服务器搭建及客户端推流完整示例 https://www.cnblogs.com/tiancun/p/7327444.html  

Windows使用Nginx搭建RTMP服务器 https://www.jianshu.com/p/f4d4c4156a15  

【EasyDarwin】RTSP视频转发服务器搭建  https://blog.csdn.net/qq_26920077/article/details/50459152  

EasyDarwin: https://github.com/EasyDarwin/EasyDarwin  

ffmpeg 推流:   

```bash
ffmpeg.exe -re -i .\yjl_test.mp4 -rtsp_transport tcp -vcodec h264 -f rtsp rtsp://localhost/test
```

rtsp://admin:root1234@192.168.1.64:554/h264/ch1/main/av_stream  
rtsp://admin:admin123@192.168.1.156:554/h264/ch1/main/av_stream  


ffmpeg解码数据转为Mat通过opencv函数显示: https://blog.csdn.net/tkp2014/article/details/46651615?_t_t_t=0.0488573508318535  
代码: https://github.com/how0723/opencvideo  

VS2019 CMake 环境配置 FFMPEG: https://blog.csdn.net/shulianghan/article/details/99540829#Visual_Studio_Cmake__FFMPEG_137   

利用ffmpeg从RTSP服务器拉流并保存各种格式文件: https://www.jianshu.com/p/c8488537501b   

ffmpeg处理rtmp/文件/rtsp的推流和拉流: https://www.cnblogs.com/lidabo/p/6932134.html   

Win10+VS2015+cuda10.1安装: https://blog.csdn.net/yangjf91/article/details/90753293  

ffmpeg 播放 RTSP 的一点优化: https://www.cnblogs.com/betterwgo/p/7642331.html  


分享一下海康威视古老的播放器源码 https://blog.csdn.net/houwenbin1986/article/details/78593566  

海康 网络摄像头 多摄像头数据传输及流解码: http://www.voidcn.com/article/p-penkffql-ve.html

**Live555 编译**   
live555在windows下通過VS2008編譯: https://www.twblogs.net/a/5b87a58e2b71775d1cd84f05  

使用 dll 生成 lib: http://suddymail.org/show-160-1.html   

live555 编译：增加CMake支持: https://www.cnblogs.com/JeroZeng/p/4783547.html  

live555在windows下通過VS2008編譯 https://www.twblogs.net/a/5b87a58e2b71775d1cd84f05  

windows下生成dll lib 与linux生成共享文件: https://blog.csdn.net/liuxiangxxl/article/details/84861952  

Linux静态库.a与动态库.so的生成与区别、以及.so库文件的封装与使用: https://blog.csdn.net/psy6653/article/details/78529054  

Windows和Linux上生成动态库（dll，.so）: https://blog.csdn.net/gx1589969/article/details/93861483  

导出函数__declspec(dllexport): https://blog.csdn.net/GVFDBDF/article/details/52204240  

VS2017动态链接库（.dll）的生成与使用 https://blog.csdn.net/m0_37170593/article/details/76445972  

VS2010中dumpbin工具的使用: https://blog.csdn.net/fengbingchun/article/details/43956673  

导出函数__declspec(dllexport): https://blog.csdn.net/gaoyi221119/article/details/84102920  

**Linux**  
Live555实战之交叉编译live555共享库: https://blog.csdn.net/liukun321/article/details/38012497  


### windows git 服务器  

java7: https://www.cnblogs.com/heqiyoujing/p/9502726.html  

gitblit: https://blog.csdn.net/pansaky/article/details/80885277    

git clone ssh://admin@114.114.114.113:29418/td_lwai.git  


VS2015 Professional： HMGNV-WCYXV-X7G9W-YCX63-B98R2

