# 训练 YOLO 之前的检查工作  

## 0. 数据集是否预留有测试集?  

按照 1:9 将数据集分为训练集和测试集.  

## 1. 数据集主体是 VOC 还是 COCO?

确认使用 class 的 id 是否正确. 比如 person 类在 COCO 数据集的 id 为 1, 但在 VOC 的 id 为 14.  

如果之前为 COCO 生成的数据集, 则不能直接用在 VOC 中.  

## 2. 检查 yolov3_xxx.cfg 文件的 TRAIN 和 TEST 阶段

训练阶段和测试阶段的 batch 和 subdivision 是不同的.   

## 3. 调用 GPU 设备时一定要使用 root 权限

即运行命令前添加 sudo.   

## 4. 检查生成的 train.txt 中是否存在空行

如果在 train.txt 文件中存在空行, 那么在 load_image() 的时候无法加载图片文件, 则程序会段错误崩溃.   

## 5. VOC 数据集的训练次数

对于 VOC 数据集而言, max_batches 一般达到 10W 次就可以了, 没必要向像 COCO 数据集一样使用 50W 的训练次数.   