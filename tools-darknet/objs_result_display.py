#coding=utf-8
import skimage.io as io
import matplotlib.pyplot as plt
import numpy as np
import os
import cv2

from PIL import Image
from matplotlib import pyplot as plt
from pylab import *
# axis()返回坐标轴的默认值(0.0, 1.0, 0.0, 1.0),(xmin, xmax, ymin, ymax)
# plt.axis()
# 设置x轴和y轴的值
# plt.autoscale(),该方法会计算坐标轴的最佳大小以适应数据的显示# plt.axes(),该方法向图形中添加新的坐标轴# rect属性,归一化单位(0, 1)下的left、bottom、width、height四个属性# axisbg参数,指定坐标轴的背景颜色# sharex/sharey参数,接收其他坐标轴的值并让当前坐标轴(x/y)共享相同的值# polar参数,指定是否使用极坐标轴# plt.axhline()/plt.axvline()根据给定的x和y值相应地绘制出相对于坐标轴的水平线/垂直线plt.axhline()plt.axvline()plt.axhline(4)# plt.axhspan()/plt.axvspan()添加一个跨坐标轴的水平带(矩形)# plt.axhspan()/plt.axvspan()必需ymin/xmin和ymax/xmax参数指定水平/垂直带的宽度plt.axhspan(-7, -4)plt.axvspan(0.2, 0.7)# plt.grid()打开网格# which:指定绘制的网格刻度类型(major、minor或者both)# axis:指定绘制哪组网格线(both、x或者y)plt.grid()# 单独一个坐标轴由matplotlib.axis.Axis类表示,matplotlib.axis.XAxis表示x轴# matplotlib.axis.YAxis表示y轴plt.show()

# print(help(PIL))
image_path = '/home/magic/Desktop/multiData_label_sparse/'

# label_names = ["bigcoal", "FT", "GC", "HC", "MSS", "GU", "ARC", "GMR", "GroundTruth"]
# labels = ["FT", "GC", "HC", "MSS", "GU", "RC", "Ours"]

file_pre = set()
row_idx = 0
rows = 10

labels = os.listdir(image_path)
cols = len(labels)

label_paths = []
for label in labels:
    label = image_path + label + '/'
    label_paths.append(label)

size = 30
fig, axs = plt.subplots(rows, cols, figsize=(40, 30))
plt.tight_layout(pad=0.2, w_pad=0.1, h_pad=0.1) # 调整布局

for col_idx, label_path in enumerate(label_paths):

    img_names = os.listdir(label_path)
    rows = len(img_names)

    if(rows == 10):

        for row_idx, img_name in enumerate(img_names):
            ## begin plots
            plt.subplots_adjust(wspace =0.1, hspace =0.1)#调整子图间距

            img_path = label_path + img_name
            print(img_path)
            print(rows, cols, col_idx+1+cols*(row_idx), sep=',')

            plt.subplot(rows, cols, col_idx+1+cols*(row_idx))
            plt.axis('off')
            img_data = Image.open(img_path)
            img_data = img_data.resize((800, 350), Image.ANTIALIAS)
            width, height = img_data.size 
            x_size = max(width, height)
            ratio = height/width
            # xlim(0, x_size)
            # ylim(x_size*ratio, 0)
            img_data = img_data.resize((x_size, int(x_size*ratio)), Image.ANTIALIAS)
            ax_values = [0, x_size, x_size*ratio, 0]
            plt.axis(ax_values)
            plt.imshow(img_data)

fig.suptitle('position',fontsize=16,x=0.53,y=1.05,)
fig.suptitle('汉子',fontsize=16,x=0.13,y=1.05,)
plt.axis('off')
plt.show()