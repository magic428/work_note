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

def delete_file(file_path):  
    if os.path.exists(file_path):
        os.remove(file_path)
        print("remove file: ", file_path)

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
    txtPath = os.sep.join([path, "Txts"]) 

    # get imglist and xmllist; their length must be equal
    imgs = os.listdir(jpgPath)
    for i in range(len(imgs)-1, -1, -1):
        if not imgs[i].lower().endswith("jpg") and not imgs[i].lower().endswith("png") and not imgs[i][1].lower().endswith("jpeg"):
            del imgs[i]

    img_names = set(os.path.splitext(imgs[i])[0] for i in range(len(imgs)))

    xmls = os.listdir(xmlPath)
    for i in range(len(xmls)-1, -1, -1):
        if not xmls[i].lower().endswith("xml"):
            del xmls[i]
    xml_names = set(os.path.splitext(xmls[i])[0] for i in range(len(xmls)))

    txts = os.listdir(txtPath)
    for i in range(len(txts)-1, -1, -1):
        if not txts[i].lower().endswith("txt"):
            del txts[i]
    txt_names = set(os.path.splitext(txts[i])[0] for i in range(len(txts)))

    # if(len(img_names) > len(xml_names)):
    #     print ("imgs > xmls.")
    #     extra_files = img_names - xml_names
    #     for extra_file in extra_files:
    #         extra_path = os.sep.join([jpgPath, extra_file]) + '.jpg'
    #         os.remove(extra_path)
    #         print(extra_path)

    extra_files = (txt_names | img_names) - (txt_names & img_names)
    print ("extra_files: ", extra_files)
    for extra_file in extra_files:
        extra_img_path = os.sep.join([jpgPath, extra_file]) + '.jpg'
        extra_xml_path = os.sep.join([xmlPath, extra_file]) + '.xml'
        extra_txt_path = os.sep.join([txtPath, extra_file]) + '.txt'

        delete_file(extra_img_path)
        delete_file(extra_xml_path)
        delete_file(extra_txt_path)

    img_cnt = len(os.listdir(jpgPath))
    xml_cnt = len(os.listdir(xmlPath))
    txt_cnt = len(os.listdir(txtPath))
    print("cnts: %d, %d, %d", img_cnt, xml_cnt, txt_cnt)


    
