#coding=utf-8
#!/usr/bin/env python3

'''
Generate the images in JPEGImages for Annotations and labels

Usage:
    python3 custom_data_labels.py --path DATA_PATH --type DATA_TYPE

Help:
    python3 custom_data_labels.py -h

Note:
    There is no train data and validate date division.

'''

import os
import random
import shutil
import argparse
from xml.etree import ElementTree as ET

# COCO dataSet classed name, total 80 classes.
coco_classes = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush', 'bigcoal']

# VOC dataSet classed name, total 20 classes.
voc_classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor", 'bigcoal', 'roller', 'workBoard', 'fullFoldBoard', 'uneven']

# custom_classes = ["Coal_miner", "Lump_coal", "Shearer_drum", "Face_sprag"]
custom_classes = ["Lump_coal", "Shearer_drum", "Coal_miner", "FS_open", "FS_close", "FS_semi_close"]

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


def convert_annotation(data_path, data_type):
    '''
        生成 train.txt 文件和 labels/ 文件

        labels 文件内容是通过将 xml 文件中的标注信息转换后得到

        param@data_path: 要处理的数据集目录
        param@data_type: 要处理的数据集类型. 例如 VOC, COCO
    '''

    # get data set classes label name
    classes = ''
    if data_type == "voc":
        classes = voc_classes;
    elif data_type == "coco":
        classes = coco_classes;
    elif data_type == "custom":
        classes = custom_classes;

    cwd = os.getcwd()

    xml_path = '{}/Annotations/'.format(data_path)
    xml_files = os.listdir(xml_path)

    labels_path = '{}/labels/'.format(data_path)
    if not os.path.exists(labels_path):
        os.makedirs(labels_path)
    else:
        shutil.rmtree(labels_path)
        os.makedirs(labels_path)

    image_list = []
    for xml_file in xml_files:

        # jpg, png, jpeg
        img_name = '___'
        jpg_image_name = '{}/JPEGImages/{}.jpg'.format(data_path, os.path.splitext(xml_file)[0])
        jpeg_image_name = '{}/JPEGImages/{}.jpeg'.format(data_path, os.path.splitext(xml_file)[0])
        png_image_name = '{}/JPEGImages/{}.png'.format(data_path, os.path.splitext(xml_file)[0])
        if os.path.exists(jpg_image_name):
            img_name = jpg_image_name
        elif os.path.exists(jpeg_image_name):
            img_name = jpeg_image_name
        elif os.path.exists(png_image_name):
            img_name = png_image_name
        if not img_name == '___':
            image_list.append(img_name)

        in_file = open(xml_path+xml_file)
        out_file = open('{}{}.txt'.format(labels_path, os.path.splitext(xml_file)[0]), 'w')
        print('{}{}.txt'.format(labels_path, os.path.splitext(xml_file)[0]))

        tree=ET.parse(in_file)
        root = tree.getroot()
        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text)

        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls not in classes:
                print('**error** class: <{}> not in classes, check it.'.format(cls))
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = convert((w,h), b)
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

        in_file.close()
        out_file.close()

    return image_list

# generate test.txt and train.txt
def split_train_test_samples(image_list):
    '''
        train: 0.9
        test: 0.1
    '''

    train_file = open('{}/train.txt'.format(data_path), "w")
    test_file = open('{}/test.txt'.format(data_path), "w")

    random.shuffle(image_list)

    ratio = 0.1
    n_test = int(len(image_list)*ratio)
    test_list = image_list[:n_test]
    train_list = image_list[n_test:]

    for line in test_list:
        test_file.write(line+'\n')

    for line in train_list:
        train_file.write(line+'\n')

    test_file.close()
    train_file.close()


if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument('--path', '-p', help="Sepcify the path to dataset", required=True)
    ap.add_argument('--type', '-t', help="Sepcify the type of dataset, eg: VOC, COCO, custom", required=True)
    args = vars(ap.parse_args())

    data_path = args["path"]
    data_type = args["type"]
    data_type = data_type.lower()
    data_path = os.path.abspath(data_path)
    print(data_path, data_type, sep=", ")
    if '/' == data_path[-1]:
        data_path = data_path[:-1]

    img_list = convert_annotation(data_path, data_type)
    split_train_test_samples(img_list)
