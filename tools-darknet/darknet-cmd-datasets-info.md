## 常用的 darknet 命令行  

sudo ./darknet detector train cfg/sw-5.data cfg/yolov3-sw-5ma.cfg darknet53.conv.74 -gpus 1 -map

sudo ./darknet detector demo cfg/sw-5.data cfg/yolov3-sw-5ma-test.cfg ~/data/darknet/backup/sw-5ma/yolov3-sw-5ma_best.weights ~/data/video/sw-test.mp4 -i 2

sudo ./darknet detector map cfg/sw-5.data cfg/yolov3-sw-5ma.cfg ~/data/darknet/backup/sw-5ma/yolov3-sw-5ma_best.weights  -i 2

sudo ./darknet detector calc_anchors cfg/sw-4.data -num_of_clusters 9 -width 416 -height 416


## yjl

 Tensor Cores are used. Last accuracy mAP@0.5 = 98.13 %, best = 98.49 % 
 200000: 0.220557, 0.229053 avg loss, 0.000010 rate, 1.459967 seconds, 12800000 images
Resizing to initial size: 608 x 608 
 try to allocate additional workspace_size = 59.71 MB 
 CUDA allocate done! 

 calculation mAP (mean average precision)...
1708
 detections_count = 2858, unique_truth_count = 2315  
class_id = 0, name = Coal_miner, ap = 98.56%   	 (TP = 1246, FP = 49) 
class_id = 1, name = Lump_coal, ap = 99.74%   	 (TP = 94, FP = 3) 
class_id = 2, name = Shearer_drum, ap = 97.57%   	 (TP = 86, FP = 2) 
class_id = 3, name = Abnormal_alignment, ap = 96.56%   	 (TP = 789, FP = 92) 

 for conf_thresh = 0.25, precision = 0.94, recall = 0.96, F1-score = 0.95 
 for conf_thresh = 0.25, TP = 2215, FP = 146, FN = 100, average IoU = 79.47 % 

 IoU threshold = 50 %, used Area-Under-Curve for each unique Recall 
 mean average precision (mAP@0.50) = 0.981073, or 98.11 % 
Total Detection Time: 19.000000 Seconds

Set -points flag:
 `-points 101` for MS COCO 
 `-points 11` for PascalVOC 2007 (uncomment `difficult` in voc.data) 
 `-points 0` (AUC) for ImageNet, PascalVOC 2010-2012, your custom dataset

 mean_average_precision (mAP@0.5) = 0.981073 

 
## sw

 calculation mAP (mean average precision)...
1520
 detections_count = 17139, unique_truth_count = 16038  
class_id = 0, name = Coal_miner, ap = 97.39%   	 (TP = 1876, FP = 107) 
class_id = 1, name = Lump_coal, ap = 98.10%   	 (TP = 2470, FP = 112) 
class_id = 2, name = Shearer_drum, ap = 97.40%   	 (TP = 863, FP = 4) 
class_id = 3, name = Face_sprag, ap = 99.69%   	 (TP = 10593, FP = 61) 

 for conf_thresh = 0.25, precision = 0.98, recall = 0.99, F1-score = 0.98 
 for conf_thresh = 0.25, TP = 15802, FP = 284, FN = 236, average IoU = 88.06 % 

 IoU threshold = 50 %, used Area-Under-Curve for each unique Recall 
 mean average precision (mAP@0.50) = 0.981469, or 98.15 % 
Total Detection Time: 17.000000 Seconds

## sw802-1

伸展护帮板:  16964;  
护帮板半收:  25384;  
折叠护帮板:  5761;  
大块煤:     14165;  
采煤机滚筒:  5518;
矿工:       1213;

 detections_count = 7796, unique_truth_count = 6924  
class_id = 0, name = Lump_coal, ap = 92.09%   	 (TP = 1278, FP = 150) 
class_id = 1, name = Shearer_drum, ap = 99.56%   	 (TP = 559, FP = 6) 
class_id = 2, name = Coal_miner, ap = 96.80%   	 (TP = 118, FP = 3) 
class_id = 3, name = FS_open, ap = 98.89%   	 (TP = 1673, FP = 42) 
class_id = 4, name = FS_close, ap = 99.56%   	 (TP = 507, FP = 5) 
class_id = 5, name = FS_semi_close, ap = 97.75%   	 (TP = 2505, FP = 50) 

for conf_thresh = 0.25, precision = 0.96, recall = 0.96, F1-score = 0.96 
for conf_thresh = 0.25, TP = 6640, FP = 256, FN = 284, average IoU = 85.25 % 

IoU threshold = 50 %, used Area-Under-Curve for each unique Recall 
mean average precision (mAP@0.50) = 0.974419, or 97.44 % 

## SW802-tiny-1ma

sudo ./darknet detector demo cfg/sw802-1.data cfg/yolov3-tiny_3l-sw802-1ma-test.cfg ~/data/darknet/backup/sw802-1ma/yolov3-tiny_3l-sw802-1ma_best.weights ~/data/video/sw802-test1.mp4 -i 2

class_id = 0, name = Lump_coal, ap = 91.35%   	 (TP = 1201, FP = 158) 
class_id = 1, name = Shearer_drum, ap = 99.53%   	 (TP = 551, FP = 9) 
class_id = 2, name = Coal_miner, ap = 96.72%   	 (TP = 116, FP = 5) 
class_id = 3, name = FS_open, ap = 97.77%   	 (TP = 1642, FP = 82) 
class_id = 4, name = FS_close, ap = 98.13%   	 (TP = 470, FP = 23) 
class_id = 5, name = FS_semi_close, ap = 97.37%   	 (TP = 2456, FP = 84) 

 for conf_thresh = 0.25, precision = 0.95, recall = 0.93, F1-score = 0.94 
 for conf_thresh = 0.25, TP = 6436, FP = 361, FN = 488, average IoU = 79.33 % 

 IoU threshold = 50 %, used Area-Under-Curve for each unique Recall 
 mean average precision (mAP@0.50) = 0.968126, or 96.81 % 



 compute_capability = 700, cudnn_half = 1 
   layer   filters  size/strd(dil)      input                output
   0 conv     16       3 x 3/ 1    608 x 608 x   3 ->  608 x 608 x  16 0.319 BF
   1 max               2 x 2/ 2    608 x 608 x  16 ->  304 x 304 x  16 0.006 BF
   2 conv     32       3 x 3/ 1    304 x 304 x  16 ->  304 x 304 x  32 0.852 BF
   3 max               2 x 2/ 2    304 x 304 x  32 ->  152 x 152 x  32 0.003 BF
   4 conv     64       3 x 3/ 1    152 x 152 x  32 ->  152 x 152 x  64 0.852 BF
   5 max               2 x 2/ 2    152 x 152 x  64 ->   76 x  76 x  64 0.001 BF
   6 conv    128       3 x 3/ 1     76 x  76 x  64 ->   76 x  76 x 128 0.852 BF
   7 max               2 x 2/ 2     76 x  76 x 128 ->   38 x  38 x 128 0.001 BF
   8 conv    256       3 x 3/ 1     38 x  38 x 128 ->   38 x  38 x 256 0.852 BF
   9 max               2 x 2/ 2     38 x  38 x 256 ->   19 x  19 x 256 0.000 BF
  10 conv    512       3 x 3/ 1     19 x  19 x 256 ->   19 x  19 x 512 0.852 BF
  11 max               2 x 2/ 1     19 x  19 x 512 ->   19 x  19 x 512 0.001 BF
  12 conv   1024       3 x 3/ 1     19 x  19 x 512 ->   19 x  19 x1024 3.407 BF
  13 conv    256       1 x 1/ 1     19 x  19 x1024 ->   19 x  19 x 256 0.189 BF
  14 conv    512       3 x 3/ 1     19 x  19 x 256 ->   19 x  19 x 512 0.852 BF
  15 conv     44       1 x 1/ 1     19 x  19 x 512 ->   19 x  19 x  44 0.016 BF
  16 yolo
[yolo] params: iou loss: mse, iou_norm: 0.75, cls_norm: 1.00, scale_x_y: 1.00
  17 route  13
  18 conv    128       1 x 1/ 1     19 x  19 x 256 ->   19 x  19 x 128 0.024 BF
  19 upsample                 2x    19 x  19 x 128 ->   38 x  38 x 128
  20 route  19 8
  21 conv    256       3 x 3/ 1     38 x  38 x 384 ->   38 x  38 x 256 2.555 BF
  22 conv     44       1 x 1/ 1     38 x  38 x 256 ->   38 x  38 x  44 0.033 BF
  23 yolo
[yolo] params: iou loss: mse, iou_norm: 0.75, cls_norm: 1.00, scale_x_y: 1.00
  24 route  21
  25 conv    128       1 x 1/ 1     38 x  38 x 256 ->   38 x  38 x 128 0.095 BF
  26 upsample                 2x    38 x  38 x 128 ->   76 x  76 x 128
  27 route  26 6
  28 conv    128       3 x 3/ 1     76 x  76 x 256 ->   76 x  76 x 128 3.407 BF
  29 conv     11       1 x 1/ 1     76 x  76 x 128 ->   76 x  76 x  11 0.016 BF


   compute_capability = 700, cudnn_half = 1 
   layer   filters  size/strd(dil)      input                output
   0 conv     32       3 x 3/ 1    416 x 416 x   3 ->  416 x 416 x  32 0.299 BF
   1 conv     64       3 x 3/ 2    416 x 416 x  32 ->  208 x 208 x  64 1.595 BF
   2 conv     32       1 x 1/ 1    208 x 208 x  64 ->  208 x 208 x  32 0.177 BF
   3 conv     64       3 x 3/ 1    208 x 208 x  32 ->  208 x 208 x  64 1.595 BF
   4 Shortcut Layer: 1
   5 conv    128       3 x 3/ 2    208 x 208 x  64 ->  104 x 104 x 128 1.595 BF
   6 conv     64       1 x 1/ 1    104 x 104 x 128 ->  104 x 104 x  64 0.177 BF
   7 conv    128       3 x 3/ 1    104 x 104 x  64 ->  104 x 104 x 128 1.595 BF
   8 Shortcut Layer: 5
   9 conv     64       1 x 1/ 1    104 x 104 x 128 ->  104 x 104 x  64 0.177 BF
  10 conv    128       3 x 3/ 1    104 x 104 x  64 ->  104 x 104 x 128 1.595 BF
  11 Shortcut Layer: 8
  12 conv    256       3 x 3/ 2    104 x 104 x 128 ->   52 x  52 x 256 1.595 BF
  13 conv    128       1 x 1/ 1     52 x  52 x 256 ->   52 x  52 x 128 0.177 BF
  14 conv    256       3 x 3/ 1     52 x  52 x 128 ->   52 x  52 x 256 1.595 BF
  15 Shortcut Layer: 12
  16 conv    128       1 x 1/ 1     52 x  52 x 256 ->   52 x  52 x 128 0.177 BF
  17 conv    256       3 x 3/ 1     52 x  52 x 128 ->   52 x  52 x 256 1.595 BF
  18 Shortcut Layer: 15
  19 conv    128       1 x 1/ 1     52 x  52 x 256 ->   52 x  52 x 128 0.177 BF
  20 conv    256       3 x 3/ 1     52 x  52 x 128 ->   52 x  52 x 256 1.595 BF
  21 Shortcut Layer: 18
  22 conv    128       1 x 1/ 1     52 x  52 x 256 ->   52 x  52 x 128 0.177 BF
  23 conv    256       3 x 3/ 1     52 x  52 x 128 ->   52 x  52 x 256 1.595 BF
  24 Shortcut Layer: 21
  25 conv    128       1 x 1/ 1     52 x  52 x 256 ->   52 x  52 x 128 0.177 BF
  26 conv    256       3 x 3/ 1     52 x  52 x 128 ->   52 x  52 x 256 1.595 BF
  27 Shortcut Layer: 24
  28 conv    128       1 x 1/ 1     52 x  52 x 256 ->   52 x  52 x 128 0.177 BF
  29 conv    256       3 x 3/ 1     52 x  52 x 128 ->   52 x  52 x 256 1.595 BF
  30 Shortcut Layer: 27
  31 conv    128       1 x 1/ 1     52 x  52 x 256 ->   52 x  52 x 128 0.177 BF
  32 conv    256       3 x 3/ 1     52 x  52 x 128 ->   52 x  52 x 256 1.595 BF
  33 Shortcut Layer: 30
  34 conv    128       1 x 1/ 1     52 x  52 x 256 ->   52 x  52 x 128 0.177 BF
  35 conv    256       3 x 3/ 1     52 x  52 x 128 ->   52 x  52 x 256 1.595 BF
  36 Shortcut Layer: 33
  37 conv    512       3 x 3/ 2     52 x  52 x 256 ->   26 x  26 x 512 1.595 BF
  38 conv    256       1 x 1/ 1     26 x  26 x 512 ->   26 x  26 x 256 0.177 BF
  39 conv    512       3 x 3/ 1     26 x  26 x 256 ->   26 x  26 x 512 1.595 BF
  40 Shortcut Layer: 37
  41 conv    256       1 x 1/ 1     26 x  26 x 512 ->   26 x  26 x 256 0.177 BF
  42 conv    512       3 x 3/ 1     26 x  26 x 256 ->   26 x  26 x 512 1.595 BF
  43 Shortcut Layer: 40
  44 conv    256       1 x 1/ 1     26 x  26 x 512 ->   26 x  26 x 256 0.177 BF
  45 conv    512       3 x 3/ 1     26 x  26 x 256 ->   26 x  26 x 512 1.595 BF
  46 Shortcut Layer: 43
  47 conv    256       1 x 1/ 1     26 x  26 x 512 ->   26 x  26 x 256 0.177 BF
  48 conv    512       3 x 3/ 1     26 x  26 x 256 ->   26 x  26 x 512 1.595 BF
  49 Shortcut Layer: 46
  50 conv    256       1 x 1/ 1     26 x  26 x 512 ->   26 x  26 x 256 0.177 BF
  51 conv    512       3 x 3/ 1     26 x  26 x 256 ->   26 x  26 x 512 1.595 BF
  52 Shortcut Layer: 49
  53 conv    256       1 x 1/ 1     26 x  26 x 512 ->   26 x  26 x 256 0.177 BF
  54 conv    512       3 x 3/ 1     26 x  26 x 256 ->   26 x  26 x 512 1.595 BF
  55 Shortcut Layer: 52
  56 conv    256       1 x 1/ 1     26 x  26 x 512 ->   26 x  26 x 256 0.177 BF
  57 conv    512       3 x 3/ 1     26 x  26 x 256 ->   26 x  26 x 512 1.595 BF
  58 Shortcut Layer: 55
  59 conv    256       1 x 1/ 1     26 x  26 x 512 ->   26 x  26 x 256 0.177 BF
  60 conv    512       3 x 3/ 1     26 x  26 x 256 ->   26 x  26 x 512 1.595 BF
  61 Shortcut Layer: 58
  62 conv   1024       3 x 3/ 2     26 x  26 x 512 ->   13 x  13 x1024 1.595 BF
  63 conv    512       1 x 1/ 1     13 x  13 x1024 ->   13 x  13 x 512 0.177 BF
  64 conv   1024       3 x 3/ 1     13 x  13 x 512 ->   13 x  13 x1024 1.595 BF
  65 Shortcut Layer: 62
  66 conv    512       1 x 1/ 1     13 x  13 x1024 ->   13 x  13 x 512 0.177 BF
  67 conv   1024       3 x 3/ 1     13 x  13 x 512 ->   13 x  13 x1024 1.595 BF
  68 Shortcut Layer: 65
  69 conv    512       1 x 1/ 1     13 x  13 x1024 ->   13 x  13 x 512 0.177 BF
  70 conv   1024       3 x 3/ 1     13 x  13 x 512 ->   13 x  13 x1024 1.595 BF
  71 Shortcut Layer: 68
  72 conv    512       1 x 1/ 1     13 x  13 x1024 ->   13 x  13 x 512 0.177 BF
  73 conv   1024       3 x 3/ 1     13 x  13 x 512 ->   13 x  13 x1024 1.595 BF
  74 Shortcut Layer: 71
  75 conv    512       1 x 1/ 1     13 x  13 x1024 ->   13 x  13 x 512 0.177 BF
  76 conv   1024       3 x 3/ 1     13 x  13 x 512 ->   13 x  13 x1024 1.595 BF
  77 conv    512       1 x 1/ 1     13 x  13 x1024 ->   13 x  13 x 512 0.177 BF
  78 conv   1024       3 x 3/ 1     13 x  13 x 512 ->   13 x  13 x1024 1.595 BF
  79 conv    512       1 x 1/ 1     13 x  13 x1024 ->   13 x  13 x 512 0.177 BF
  80 conv   1024       3 x 3/ 1     13 x  13 x 512 ->   13 x  13 x1024 1.595 BF
  81 conv     44       1 x 1/ 1     13 x  13 x1024 ->   13 x  13 x  44 0.015 BF
  82 yolo
[yolo] params: iou loss: mse, iou_norm: 0.75, cls_norm: 1.00, scale_x_y: 1.00
  83 route  79
  84 conv    256       1 x 1/ 1     13 x  13 x 512 ->   13 x  13 x 256 0.044 BF
  85 upsample                 2x    13 x  13 x 256 ->   26 x  26 x 256
  86 route  85 61
  87 conv    256       1 x 1/ 1     26 x  26 x 768 ->   26 x  26 x 256 0.266 BF
  88 conv    512       3 x 3/ 1     26 x  26 x 256 ->   26 x  26 x 512 1.595 BF
  89 conv    256       1 x 1/ 1     26 x  26 x 512 ->   26 x  26 x 256 0.177 BF
  90 conv    512       3 x 3/ 1     26 x  26 x 256 ->   26 x  26 x 512 1.595 BF
  91 conv    256       1 x 1/ 1     26 x  26 x 512 ->   26 x  26 x 256 0.177 BF
  92 conv    512       3 x 3/ 1     26 x  26 x 256 ->   26 x  26 x 512 1.595 BF
  93 conv     44       1 x 1/ 1     26 x  26 x 512 ->   26 x  26 x  44 0.030 BF
  94 yolo
[yolo] params: iou loss: mse, iou_norm: 0.75, cls_norm: 1.00, scale_x_y: 1.00
  95 route  91
  96 conv    128       1 x 1/ 1     26 x  26 x 256 ->   26 x  26 x 128 0.044 BF
  97 upsample                 2x    26 x  26 x 128 ->   52 x  52 x 128
  98 route  97 36
  99 conv    128       1 x 1/ 1     52 x  52 x 384 ->   52 x  52 x 128 0.266 BF
 100 conv    256       3 x 3/ 1     52 x  52 x 128 ->   52 x  52 x 256 1.595 BF
 101 conv    128       1 x 1/ 1     52 x  52 x 256 ->   52 x  52 x 128 0.177 BF
 102 conv    256       3 x 3/ 1     52 x  52 x 128 ->   52 x  52 x 256 1.595 BF
 103 conv    128       1 x 1/ 1     52 x  52 x 256 ->   52 x  52 x 128 0.177 BF
 104 conv    256       3 x 3/ 1     52 x  52 x 128 ->   52 x  52 x 256 1.595 BF
 105 conv     11       1 x 1/ 1     52 x  52 x 256 ->   52 x  52 x  11 0.015 BF
 106 yolo
