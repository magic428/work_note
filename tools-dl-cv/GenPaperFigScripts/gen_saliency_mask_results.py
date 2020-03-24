#coding=utf-8
import skimage.io as io
import matplotlib.pyplot as plt
import numpy as np
import os
import cv2

from PIL import Image
from matplotlib import pyplot as plt
from pylab import *

'''
显著性检测论文中生成显著性图表和分割图表的脚本文件

1. 文件命名规范: 
    [".png", "_RSRC.png", "_MASk.png"]

2. subplot 下标游走:
    idx = groups*27 + class_idx*cols + (col_idx% 9) + 1
    
    一个 group 表示三行, 第一行显示 9 张原图, 接下来两行为显著性图和分割图;
    class_idx 表示文件名对应的显著图和分割图;

3. 原图为彩色图, 显著图和分割图为灰度图.  
'''

image_dirs = ['D:/Downloads/seafile/tdmarco-docs/achievements/papers/saliency/采矿与安全工程学报 - 显著性检测分割算法_v4/miners-saliency/']

# 获取图片名
cols = 9
rows = 0
file_pre = set()
for image_dir in image_dirs:
    img_names = os.listdir(image_dir)
    print(rows)
    for img_name in img_names:
        img_pre = ''
        if -1 != img_name.find('_MASK'):
            print(img_name)
            img_pre = img_name.rsplit('_', 1)[0]

            if img_pre in file_pre:
                print(img_pre)
                continue
            else:
                file_pre.add(img_pre)

print(len(file_pre))
rows = len(file_pre)//cols*3

post_names = [".png", "_RSRC.png", "_MASk.png"]

f, axs = plt.subplots(rows, cols, figsize=(20,20))
groups = 0   # 9张图像为1组
for col_idx, image_name in enumerate(file_pre):

    ## begin plots
    plt.subplots_adjust(wspace =0.1, hspace =0.05)#调整子图间距

    for class_idx, post_name in enumerate(post_names):
        img_path = image_dir + image_name + post_name

        idx = groups*27 + class_idx*cols + (col_idx% 9) + 1
        print(rows, cols, idx, sep=',')

        plt.subplot(rows, cols, idx)
        plt.axis('off')
        img_data = Image.open(img_path)
        width, height = img_data.size 
        x_size = max(width, height)
        ratio = 0.75  #(300/400)
        img_data = img_data.resize((x_size, int(x_size*ratio)), Image.ANTIALIAS)
        ax_values = [0, x_size, x_size*ratio, 0]
        plt.axis(ax_values)
    
        if class_idx % 3 == 0:
            plt.imshow(img_data)
        else:
            plt.imshow(img_data, cmap='gray')
    
    if (col_idx+1) % 9 == 0:
        groups += 1

plt.axis('off')
plt.show()