#!/usr/bin/env python3
#coding="utf-8"

'''
将 coco 数据集中的标注信息生成可供 YOLO 训练使用的 labels/ 数据
即将 bbox 部分抽离出来, 写入到对应图片名的 .txt 文件中 

.txt 文件中的内容格式: 

    [class] [x] [y] [w] [h]

使用方法:  

    将此脚本文件放在 COCO 数据集的根目录目录下, 数据集目录下包含数据文件压缩包和标注文件压缩包

    该脚本会自动解压数据集文件到 images/ 目录下, 解压标注数据文件到 annotations/ 目录下  

    用于 YOLO 训练的标注文件保存在 labels/ 目录下

'''

import os
import sys
sys.path.append(os.getenv("HOME")+ "/work/gitwork/dl_ai/coco/PythonAPI")
import subprocess
import shutil
from pycocotools import coco
import cv2
import numpy as np
import zipfile
# import skimage.io as io
# import matplotlib.pyplot as plt

classes = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']


classs_to_catids = {'0' : 'unlabeled', '1' : 'person', '2' : 'bicycle', '3' : 'car', '4' : 'motorcycle', '5' : 'airplane', '6' : 'bus', '7' : 'train', '8' : 'truck', '9' : 'boat', '10' : 'traffic light', '11' : 'fire hydrant', '12' : 'street sign', '13' : 'stop sign', '14' : 'parking meter', '15' : 'bench', '16' : 'bird', '17' : 'cat', '18' : 'dog', '19' : 'horse', '20' : 'sheep', '21' : 'cow', '22' : 'elephant', '23' : 'bear', '24' : 'zebra', '25' : 'giraffe', '26' : 'hat', '27' : 'backpack', '28' : 'umbrella', '29' : 'shoe', '30' : 'eye glasses', '31' : 'handbag', '32' : 'tie', '33' : 'suitcase', '34' : 'frisbee', '35' : 'skis', '36' : 'snowboard', '37' : 'sports ball', '38' : 'kite', '39' : 'baseball bat', '40' : 'baseball glove', '41' : 'skateboard', '42' : 'surfboard', '43' : 'tennis racket', '44' : 'bottle', '45' : 'plate', '46' : 'wine glass', '47' : 'cup', '48' : 'fork', '49' : 'knife', '50' : 'spoon', '51' : 'bowl', '52' : 'banana', '53' : 'apple', '54' : 'sandwich', '55' : 'orange', '56' : 'broccoli', '57' : 'carrot', '58' : 'hot dog', '59' : 'pizza', '60' : 'donut', '61' : 'cake', '62' : 'chair', '63' : 'couch', '64' : 'potted plant', '65' : 'bed', '66' : 'mirror', '67' : 'dining table', '68' : 'window', '69' : 'desk', '70' : 'toilet', '71' : 'door', '72' : 'tv', '73' : 'laptop', '74' : 'mouse', '75' : 'remote', '76' : 'keyboard', '77' : 'cell phone', '78' : 'microwave', '79' : 'oven', '80' : 'toaster', '81' : 'sink', '82' : 'refrigerator', '83' : 'blender', '84' : 'book', '85' : 'clock', '86' : 'vase', '87' : 'scissors', '88' : 'teddy bear', '89' : 'hair drier', '90' : 'toothbrush'}

def get_anns(ann_file):
    '''
    加载标注数据到内存, 并建立标注信息,图片和类别之间的关系

    :param: ann_file coco 数据集中的标注文件, 一般是 .json 文件
    :return 建立好标注信息,图片和类别之间的关系的数据
    '''

    if not os.path.exists(ann_file):
        print("No such file(s): {}\n".format(ann_file))
        sys.exit(1)

    anns_data = coco.COCO(ann_file)

    return anns_data
    

def get_classes(anns_data):
    '''
    获取 COCO 数据集中的所有类别名
    
    :param: anns_data 已经加载到内存中并建立好标注信息,图片和类别之间的关系的数据
    :return COCO 数据集中的所有类别名
    '''

    categories = anns_data.loadCats(anns_data.getCatIds())
    categorie_names=[cat['name'] for cat in categories]
    
    return categorie_names

def generate_labels(anns_data, 
                    data_dir='~/data/cocoDataset', 
                    data_type='train2014'):
    '''
    生成 labels/*.txt 文件

    获取两部分数据: 原图的宽高, bbox

    :param: anns_data 已经加载到内存中并建立好标注信息,图片和类别之间的关系的数据
    :param: data_dir 图片数据的保存路径, 默认为'~/data/cocoDataset'
    :param: data_type 数据集名称, 默认为'train2014'
    ''' 

    image_dir = "{}/images/{}".format(data_dir, data_type)
    if not os.path.exists(image_dir):
        print("No such file(s): {}\n".format(image_dir))
        sys.exit(1)
    
    labels_path = '{}/labels/{}'.format(data_dir, data_type)
    if not os.path.exists(labels_path):
        os.makedirs(labels_path)
    else:
        shutil.rmtree(labels_path)
        os.makedirs(labels_path)

    w = 0
    h = 0
    classes = get_classes(anns_data)
    img_ids = anns_data.getImgIds();
    train_file = open('{}/train.txt'.format(data_dir), "a")
    val_file = open('{}/val.txt'.format(data_dir), "a")
    for img_id in img_ids:

        # 获取原图的宽高 
        img = anns_data.loadImgs(img_id)[0]  # 只有一个图片信息
        w = int(img['width'])
        h = int(img['height'])

        img_name = img['file_name']
        img_path = "{}/{}".format(image_dir, img_name)

        # 保存 train.txt
        if "train" in data_type:
            train_file.write('{}\n'.format(img_path))
        elif ('val') in data_type:
            val_file.write('{}\n'.format(img_path))

        # 获取 bbox
        label_file = open('{}/{}.txt'.format(labels_path, 
            os.path.splitext(img_name)[0]), 'w')
        cls_and_bbox = []
        class_id = -1

        global classs_to_catids
        ann_id = anns_data.getAnnIds(imgIds=img_id)
        anns = anns_data.loadAnns(ann_id)  

        for ann in anns:
            if int(ann['image_id']) == int(img_id):
                x1 = int(ann['bbox'][0])
                y1 = int(ann['bbox'][1])
                x2 = x1 + int(ann['bbox'][2])
                y2 = x2 + int(ann['bbox'][3])
                bbox = (x1, x2, y1, y2)

                # 保存 labels/*.txt
                bb = convert((w,h), bbox)
                category_id = str(ann['category_id'])
                # 有些 id 是没有使用的, 因此实际标注的 category_id 可能大于 80
                cls_id = classes.index(classs_to_catids[category_id])


                if int(category_id) > 80:
                    print(ann['category_id'], cls_id, img_path, sep=", ")
                    continue;
                
                label_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
        label_file.close()        
    train_file.close()
    val_file.close()


def convert(size, box):
    '''
        将标准的 VOC xml 标注样式转换为 yolo 格式:
            <object-class> <x> <y> <width> <height>
        <x> <y> <width> <height> 表示的是标注框参数所占原图宽/高比例的浮点数, 范围是(0.0 to 1.0]. 
        注意: <x> <y> - 是标注框的中心, 而不是左上角点.  

        如: 
            1 0.716797 0.395833 0.216406 0.147222
        
        pram@size: 原图的宽和高  
        pram@box: (xmin,xmax), (ymin,ymax) 表示的边界框  
    '''
    dw = 1./(size[0])
    dh = 1./(size[1])

    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]

    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh

    return (x,y,w,h)

def run_main():   
    '''
    提取 'train2014', 'val2014', 'train2017', 'val2017' 数据集中的信息  

    :param: ann_file coco 数据集中的标注文件, 一般是 .json 文件
    :return
    '''
    # data_dir = os.getcwd()
    data_dir = "/home/klm/data_dl/common/cocoDataset"
    if not os.path.exists("images"):
        os.makedirs("images")
    else:
        shutil.rmtree("images")
        os.makedirs("images")

    data_types=['train2017', 'train2014', 'val2014',  'val2017']

    ## 解压标注信息
    subprocess.Popen("chmod +x ./*", shell=True, cwd=data_dir)
    ann_files = ['instances_train-val2014.zip', 'annotations_trainval2017.zip']
    
    for ann_file in ann_files:
        zip_file = zipfile.ZipFile("{}/{}".format(data_dir, ann_file))
        print("\nUnzip: {}...".format(ann_file))
        zip_file.extractall()
        zip_file.close()
    
    for data_type in data_types: 

        if not os.path.exists("images/"+data_type):
            os.makedirs("images/"+data_type)

        ## 解压数据集
        data_zipfile = "{}/{}.zip".format(data_dir, data_type)
        if os.path.exists(data_zipfile):
            zip_file = zipfile.ZipFile(data_zipfile)
            print("\nUnzip: {}...".format(data_zipfile))
            zip_file.extractall(path="images")
            zip_file.close()

        ann_file='{}/annotations/instances_{}.json'.format(data_dir, data_type)
        print("\n{}".format(ann_file))

        anns_data = get_anns(ann_file)
        generate_labels(anns_data, data_dir, data_type)


# 最后打印出所有的 train / val 样本个数
if __name__ == "__main__":
    run_main()