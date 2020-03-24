#coding=utf8

'''
    1. Clear the samples with no object, which will remove the image files 
       without no object. 

    2. Move the files to fixed DIRECTORIES: JPEGImages, Annotations

    3. Move the files without objects to "noObjs/"
'''


import os
import argparse 
import shutil
from enum import Enum

class dirStruct(Enum):
    DirNone = 1     # 直接拷贝到指定的目录
    DirExt = 2      # 按后缀名新建文件夹，将相同的文件拷贝到指定的目录
    DirOrigin = 3   # 按照原来目录来新建目录并且拷贝文件
 
def remove_no_obj_files(path):
    txtFile = []

    files = os.listdir(path)
    for i in range(len(files)):
        if files[i].lower().endswith("txt"):
            txtFile.append(files[i])

    for i in range(len(txtFile)):
        fileName = path + '/' + txtFile[i]
        input = open(fileName, 'r')
        num = input.read(1)
        input.close()
        if num == '0':
            os.remove(fileName)

            name = txtFile[i].split('.',1)[0]
            #print name
            jpgName = path + '/' + "".join(name) + ".jpg"
            if os.path.exists(jpgName):
                os.remove(jpgName)

            xmlName = path + '/' + "".join(name) + ".xml"
            if os.path.exists(xmlName):
                os.remove(xmlName)

def move_no_obj_files(path):
    txtFile = []

    files = os.listdir(path)
    for i in range(len(files)):
        if files[i].lower().endswith("txt"):
            txtFile.append(files[i])
    
    dst_dir = path+'/noObjs/'
    check_dir_exists(dst_dir)
    for i in range(len(txtFile)):
        fileName = path + '/' + txtFile[i]
        input = open(fileName, 'r')
        num = input.read(1)
        input.close()
        if num == '0':
            os.remove(fileName)

            name = txtFile[i].split('.',1)[0]
            xmlName = path + '/' + "".join(name) + ".xml"
            if os.path.exists(xmlName):
                os.remove(xmlName)

            jpgName = path + '/' + "".join(name) + ".jpg"
            dst_fpath = dst_dir + "".join(name) + ".jpg"
            print('move',jpgName, dst_fpath)
            if os.path.exists(jpgName):
                shutil.move(jpgName, dst_fpath)


def check_dir_exists(dir_path):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    else:
        shutil.rmtree(dir_path)
        os.makedirs(dir_path)


def copy_files_to_standard_dir(data_path):
    '''
        copy the files with fixed extension which specified by "ext".

        param@data_path: path to dataset, data has been labeled 
    '''

    # JPEGImages/, Annotations/, Txts/
    JPEGImages_dir = data_path + '/JPEGImages/'
    Annotations_dir = data_path + '/Annotations/'
    Txts_dir = data_path + '/Txts/'
    check_dir_exists(JPEGImages_dir)
    check_dir_exists(Annotations_dir)
    check_dir_exists(Txts_dir)
    
    all_files = os.listdir(data_path)
    for filename in all_files:

        filepath = data_path+'/'+filename
        
        if os.path.isfile(filepath):
            extname = os.path.splitext(filename)[1]
            basename = os.path.basename(filename)
            dst_dir = ''

            dst_fname = filename 
            if extname == ".jpg" or extname == ".jpeg" or extname == ".png":
                dst_dir = JPEGImages_dir + dst_fname
            elif extname == ".xml":
                dst_dir = Annotations_dir + dst_fname
            elif extname == ".txt":
                dst_dir = Txts_dir + dst_fname

            # print('{}   ===>  {}'.format(filepath, dst_dir))
            shutil.move(filepath, dst_dir)

def rm_files(data_path):
    '''
        rm the files with fixed extension which specified by "ext".

        param@data_path: path to dataset, data has been labeled 
    '''
    all_files = os.listdir(data_path)
    jpg_files = set()
    txt_files = set()
    for filename in all_files:
        if filename.endswith('.jpg') :
            jpg_files.add(os.path.splitext(filename)[0])
        elif filename.endswith('.txt'):
            txt_files.add(os.path.splitext(filename)[0])

    need_rm_files = txt_files-jpg_files
    print("len", len(need_rm_files))

    for need_rm_file in need_rm_files:
    
        txt_filepath = data_path+'/'+need_rm_file+".txt"
        xml_filepath = data_path+'/'+need_rm_file+".xml"
        print(txt_filepath, xml_filepath)
   
        os.remove(txt_filepath)
        os.remove(xml_filepath)

if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("--path", "-p", help="sepcify the path to dataset", required=True)
    args = vars(ap.parse_args())
    path = args["path"]
    
    # deal with the last character '/' in path
    if path[-1] == '/':
        path = path[:-1]

    # remove_no_obj_files(path)

    move_no_obj_files(path)
    copy_files_to_standard_dir(path)

    # rm_files(path)
