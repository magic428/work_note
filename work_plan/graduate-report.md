# 深度学习和图像处理应用概述  


## 深度学习  

整个深度神经网路可以比喻为一个非线性的函数映射关系, 将输入映射到输出.   

深度指的是神经网络的层数;   

深度学习框架: 可以用来训练一个深度学习模型的程序, 比如 YOLOv3, Caffe, tensorflow;  

深度学习属于监督学习;

深度学习为什么突然就火起来了?  

    GPU 图形处理单元的快速发展;  
    数据获取的途径更加便捷;  

适用于泛性的应用;  

## 图像处理  



## 展示部分  

1) OpenCV 课本的椒盐效果, 颜色数目减少效果, 前景检测自行车小人效果;  

$$
cd /home/klm/work/gitwork/work_note/image_process/code/tracker/build
./tracker
$$

2) 图像分割算法; 

$$
cd /home/klm/work/workSpace/cpp/saliency_cut/build
rm /home/klm/data_dl/common/saliency/light_test/saliency -rf
./saliency_cut /home/klm/data_dl/common/saliency/light_test
$$

3) 图像去雾算法; 

$$
cd /home/klm/work/gitwork/work_note/image_process/code/defrog/cpp/dehazing_korea/build
dehazing /home/klm/data_dl/video/video_frog/cross.avi output.avi
$$


4) 图像去噪-磨皮算法;

$$
cd /home/klm/work/gitwork/work_note/image_process/code/denoise/cpp/lee_filter_integer_image/build
./integer_image /home/klm/work/gitwork/work_note/image_process/images/aSa.jpg 3 7 
$$


5) 煤机摇臂和顶梁边缘线检测   

cd /home/magic/work/gitwork/work_note/tdmc/topline_armline_dehazing_fasa_v0.4



