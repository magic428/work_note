#coding=utf-8
#!/usr/bin/env python3

'''
label tool, label files' format similar to VOC: .xml, .txt;  

Usage: 

    python3 label_tool.py --path PATH

Help: 
    python3 label_tool.py -h  

'''

import os
import argparse
import cv2
import copy 


def check_dir_exists(dir_path):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    else:
        shutil.rmtree(dir_path)
        os.makedirs(dir_path)


def check_file_exists(file_path):
    if not os.path.exists(file_path):
        print("error: No Such file:{}".format(file_path))
        return False

if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("--path", "-p", help="sepcify the path to dataset", required=True)
    args = vars(ap.parse_args())
    path = args["path"]
    if path[-1] != os.sep:
        path += os.sep

    cnt = 0
    img_names = os.listdir(path)
    for img_name in img_names:
        if img_name.endswith('.png'):

            png_img_path = path + img_name 
            check_file_exists(png_img_path)
            img_data = cv2.imread(png_img_path)
            os.remove(png_img_path)
            jpg_img_path = png_img_path.replace('png', 'jpg') 
            print("{}  ====>  \n{}".format(png_img_path, jpg_img_path))
            cv2.imwrite(jpg_img_path, img_data, [int(cv2.IMWRITE_JPEG_QUALITY), 100]) 
            cnt += 1

    print('{} files converted.'.format(cnt))

