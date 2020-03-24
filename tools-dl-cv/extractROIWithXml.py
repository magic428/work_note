#coding=utf-8
'''
功能： 
      使用标注文件 *.xml 中的 BBOX 坐标信息提取其对应的 ROI 区域
      然后按照其对应的类别保存 ROI 区域为图片
      
注意： 
      ROI 区域的切片规则是：[row_s:row_e，column_s:column_e]
'''

import os
import cv2
import time
import argparse
from xml.etree import ElementTree as ET  

class_cnt = {}

def loadROI(path):
    print(path)

    per=ET.parse(path) 

    roi = []
    rois = []
    colStart = 0
    colEnd = 0
    rowStart = 0
    rowEnd = 0 
    class_name = []

    name_node = per.getiterator("name") 
    for name in name_node:
        class_name.append(name.text)
        # print ("node.text:%s" % name.text)

    lst_node = per.getiterator("bndbox")  
    for oneper in lst_node:  #找出person节点  
        for child in oneper.getchildren(): #找出person节点的子节点  
            
            if child.tag == 'xmin':
                colStart = int(child.text)
            elif child.tag == 'ymin':
                colEnd = int(child.text)
            elif child.tag == 'xmax':
                rowStart = int(child.text)
            elif child.tag == 'ymax':
                rowEnd = int(child.text)

            roi=[[colStart, colEnd],[rowStart,rowEnd]] # 此时只考虑了一个框
        
        rois.append(roi)
        # print roi[0][0],roi[0][1],roi[1][0],roi[1][1], type(roi)
    if len(rois) == len(class_name):
        return rois, class_name

# 保存为ROI图片        
def saveROI(name, class_name, rois, img):

    if(not os.path.exists('roi')):
        os.makedirs('roi')

    for index, roi in enumerate(rois):
        class_path = 'roi/'+ class_name[index]
        if class_name[index] not in class_cnt:
            class_cnt[class_name[index]] = 0
        else:
            class_cnt[class_name[index]] += 1
        
        if(not os.path.exists(class_path)):
            os.makedirs(class_path)
        roi_prefix = os.path.splitext(name)[0]
        full_name = 'roi/{}/{}_{:<02d}.jpg'.format(class_name[index], roi_prefix, index) 

        d = roi[0]
        e = roi[1]
        pmin = (min(d[0], e[0]), min(d[1], e[1]))
        pmax = (max(d[0], e[0]), max(d[1], e[1]))

        colStart = pmin[0]
        colEnd = pmax[0]
        rowStart = pmin[1]
        rowEnd = pmax[1]

        # roiImg = np.zeros((height,width,3), np.uint8)
        # roiImg = (colStart, rowStart), (colEnd, rowEnd)
        # roiImg = ( rowStart:rowEnd, colStart:colEnd)
        cv2.imwrite(full_name, img[rowStart:rowEnd, colStart:colEnd], [int(cv2.IMWRITE_JPEG_QUALITY), 100])   # 100 is the highest quality.
        # cv2.imwrite(full_name, img[colStart:colEnd, rowStart:rowEnd], [int(cv2.IMWRITE_JPEG_QUALITY), 100])   # 100 is the highest quality.

# 在图片上将ROI区域框选出来  
def saveRect(name, class_name, rois, img):
    index = 0
    class_path = 'roi/'+ class_name[index]

    if(not os.path.exists('roi')):
        os.makedirs('roi')
    if(not os.path.exists(class_path)):
        os.makedirs(class_path)

    if len(rois):
        for roi in rois:
            full_name = 'roi/{}/{}'.format(class_name[index], name) 


            d = roi[0]
            e = roi[1]
            pmin = (min(d[0], e[0]), min(d[1], e[1]))
            pmax = (max(d[0], e[0]), max(d[1], e[1]))

            colStart = pmin[0]
            colEnd = pmax[0]
            rowStart = pmin[1]
            rowEnd = pmax[1]

            # roiImg = np.zeros((height,width,3), np.uint8)
            # roiImg = (colStart, rowStart), (colEnd, rowEnd)
            # roiImg = ( rowStart:rowEnd, colStart:colEnd)
            cv2.rectangle(img, (colStart, rowStart), (colEnd, rowEnd), (255,0,0), 2)
            cv2.imwrite(full_name, img,[int(cv2.IMWRITE_JPEG_QUALITY), 100])   # 100 is the highest quality.

            index = index + 1


if __name__ == "__main__":

    # Standard data directory
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", "-p", help="sepcify the path to dataset", required=True)
    args = vars(ap.parse_args())
    path = args["path"]
    if path[-1] == os.sep:
        path = path[:-1]

    jpgPath = os.sep.join([path, "JPEGImages"])
    xmlPath = os.sep.join([path, "Annotations"]) 

    # get imglist and xmllist; their length must be equal
    imgs = os.listdir(jpgPath)
    imgs = [(imgs[i], jpgPath + "/" + imgs[i]) for i in range(len(imgs))]
    for i in range(len(imgs)-1, -1, -1):
        if not imgs[i][1].lower().endswith("jpg") and not imgs[i][1].lower().endswith("png") and not imgs[i][1].lower().endswith("jpeg"):
            del imgs[i]

    xmls = os.listdir(xmlPath)
    xmls = [(xmls[i], xmlPath + "/" + xmls[i]) for i in range(len(xmls))]
    for i in range(len(xmls)-1, -1, -1):
        if not xmls[i][1].lower().endswith("xml"):
            del xmls[i]

    if(len(imgs) != len(xmls)):
        print ("error: imgs is not equals to xmls counts.")
        exit(1)

    while i < len(imgs):

        show = cv2.imread(imgs[i][1])
        pos = imgs[i][0].rfind(".")   # 文件扩展名的前缀
        rois, class_name = loadROI("%s/%s.xml" %(xmlPath, imgs[i][0][:pos]))
        # currentClass, objs = loadObjs("%s/%s.xml.txt" %(path, imgs[i][0][:pos]))
        # print rois
        saveROI("%s.jpg" %(imgs[i][0][:pos]), class_name, rois, show)
        #saveRect("%s.jpg" %(imgs[i][0][:pos]), class_name, rois, show)
        i = i+1
    print(class_cnt)