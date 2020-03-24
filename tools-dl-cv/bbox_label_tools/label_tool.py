#coding=utf-8
#!/usr/bin/env python3

'''
label tool, label files' format similar to VOC: .xml, .txt  

Usage: 

    python3 label_tool.py --path PATH

Help: 
    python3 label_tool.py -h  

'''

import os
import argparse
import cv2
import copy 


# 标注多个样本时想分开标注请修改这个参数为当前标注类别
current_labeled_cls = 0

current_jpg_name = ''
pre_labeled_file_name = ''

# parameters
# labels_path = "labels/"
# if not os.path.exists(labels_path):
#     os.makedirs(labels_path)

wndName = "ESC close, s save, c clean, p back"
# # className = ["Lump_coal", "Shearer_drum", "Coal_miner", "FS_open", "Abnormal_alignment"]
# className = ["Lump_coal", "Shearer_drum", "Coal_miner", "FS_open", "FS_close", "FS_semi_close"]
# colors = [(255, 0, 0), (0, 155, 0), (250, 230, 10), (255, 180, 0), (50, 40, 255), (40, 255, 30)]
className = ["Shearer_drum", "Coal_miner"]
colors = [(0, 155, 255), (250, 230, 10)]

show = []
convas = []
convas_mouse = []
dpoint = []
epoint = []
objs = []
waitSecDown = False
currentClass = 0

def refreshCurrentShow(labeled_num_rest):

    cv2.resize(show, (convas.shape[1], convas.shape[0]), convas)
    text = ""
    for t in className:
        text += t
        text += ","

    # cv2.putText(convas, text + "-" + str(labeled_num_rest), (10, 20), 1, 1.4, colors[current_labeled_cls], 2)
    cv2.putText(convas, className[current_labeled_cls] + "-" + str(labeled_num_rest), (10, 20), 1, 1.4, colors[current_labeled_cls], 2)
    # cv2.putText(convas, "", (30, 30), 1, 2, colors[currentClass], 2)
    drawObjs(objs, convas)

    if waitSecDown:
        cv2.circle(convas, dpoint, 5, colors[currentClass], 2)
    cv2.imshow(wndName, convas)

def onMouse(event, x, y, flag, points):
    global dpoint, waitSecDown, wndName, epoint

    if event == cv2.EVENT_LBUTTONDOWN:
        if waitSecDown:
            epoint = (x, y)
            waitSecDown = False
            objs.append((dpoint, epoint, currentClass))
        else:
            dpoint = (x, y)
            waitSecDown = True

        refreshCurrentShow(labeled_num_rest)
    elif event == cv2.EVENT_MOUSEMOVE:

        cv2.resize(convas, (convas.shape[1], convas.shape[0]), convas_mouse)
        cv2.line(convas_mouse, (0, y), (convas.shape[1], y), (0, 255, 0), 1)
        cv2.line(convas_mouse, (x, 0), (x, convas.shape[0]), (0, 255, 0), 1)
        cv2.imshow(wndName, convas_mouse)
    elif event == cv2.EVENT_RBUTTONDOWN:
       
        obj_cnt = len(objs)
        if obj_cnt == 0:
            # 复制 Bbox
            copyPreObjsRect(pre_labeled_file_name, x, y)
        else:
            for i in range(len(objs)-1, -1, -1):
                # xmin xmax
                xmin = min(objs[i][0][0], objs[i][1][0])
                xmax = max(objs[i][0][0], objs[i][1][0])
                ymin = min(objs[i][0][1], objs[i][1][1])
                ymax = max(objs[i][0][1], objs[i][1][1])
                # 删除错误框
                if x > xmin and x < xmax and y > ymin and y < ymax:
                    del objs[i]
                    break
                else:
                    copyPreObjsRect(pre_labeled_file_name, x, y)

        refreshCurrentShow(labeled_num_rest)


def drawObjs(objs, canvas):
    for item in objs:
        d = item[0]
        e = item[1]
        c = colors[item[2]]
        cv2.rectangle(canvas, d, e, c, 2)

def loadObjs(name):
    if not os.path.exists(name):
        return 0, []

    obs = []
    cls = 0
    with open(name, "r") as txt:
        info = txt.readline().split(",")
        num = int(info[0])
        cls = int(info[1])
        for i in range(num):
            info = txt.readline().split(",")
            d = (int(info[0]), int(info[1]))
            e = (int(info[2]), int(info[3]))
            c = int(info[4])
            obs.append((d, e, c))
    return cls, obs


def copyPreObjs(pre_labeled):
    if not os.path.exists(pre_labeled):
        print('File not exist: ', pre_labeled)
        return 0, []

    with open(pre_labeled, "r") as txt:
        info = txt.readline().split(",")
        num = int(info[0])
        for i in range(num):
            info = txt.readline().split(",")
            c = int(info[4])
            if current_labeled_cls == c:
                d = (int(info[0]), int(info[1]))
                e = (int(info[2]), int(info[3]))
                if (d, e, c) not in objs:
                    print((d, e, c))
                    print(objs)
                    objs.append((d, e, c))
                else:
                    print('already in txt') 
    return current_labeled_cls, objs


def copyPreObjsRect(pre_labeled, x, y):
    if not os.path.exists(pre_labeled):
        print('File not exist: ', pre_labeled)
        return 0, []

    with open(pre_labeled, "r") as txt:
        info = txt.readline().split(",")
        num = int(info[0])
        for i in range(num):
            info = txt.readline().split(",")
            c = int(info[4])
            if current_labeled_cls == c:
                d = (int(info[0]), int(info[1]))
                e = (int(info[2]), int(info[3]))
                if x > d[0] and x < e[0] and y > d[1] and y < e[1]:
                    if (d, e, c) not in objs:
                        print((d, e, c))
                        print(objs)
                        objs.append((d, e, c))
                    else:
                        print('already in txt')
    return current_labeled_cls, objs

def saveBreakpoint(bkp):
    with open("breakpoint.txt", "w") as p:
        p.write("%d" % bkp)

def loadBreakpoint():
    p = 0

    if os.path.exists("breakpoint.txt"):
        with open("breakpoint.txt", "r") as p:
            p = int(p.read())
    return p

def saveXML(name, objs, cls, w, h):
    global pre_labeled_file_name
    with open(name, "w") as xml:
        xml.write("<annotation><size><width>%d</width><height>%d</height></size>" % (w, h))
        for item in objs:
            fmt = """
            <object>
                <name>%s</name>
                <bndbox>
                    <xmin>%d</xmin>
                    <ymin>%d</ymin>
                    <xmax>%d</xmax>
                    <ymax>%d</ymax>
                </bndbox>
            </object>
            """

            d = item[0]
            e = item[1]
            pmin = (min(d[0], e[0]), min(d[1], e[1]))
            pmax = (max(d[0], e[0]), max(d[1], e[1]))

            cls = item[2]
            xml.write(fmt % (className[cls], pmin[0], pmin[1], pmax[0], pmax[1]))

        xml.write("</annotation>")

    pre_labeled_file_name = os.path.splitext(name)[0] + ".txt"
    print(os.path.splitext(name)[0]+'.jpg')
    with open(os.path.splitext(name)[0] + ".txt", "w") as txt:
        txt.write("%d,%d\n" % (len(objs), cls))
        for item in objs:
            d = item[0]
            e = item[1]
            pmin = (min(d[0], e[0]), min(d[1], e[1]))
            pmax = (max(d[0], e[0]), max(d[1], e[1]))

            cls = item[2]
            txt.write("%d,%d,%d,%d,%d,%s\n" % (pmin[0], pmin[1], pmax[0], pmax[1], cls, className[cls]))

def sort_as_filename(imgs):
    # 使用数字排序

    file_name_pre = ''
    file_name_post = ''
    dig_bits = 0
    i = 0
    sort_imgs_pre = list()
    sort_imgs = list()
    for i in range(len(imgs)):
        pos_s = imgs[i].rfind("_")
        pos_e = imgs[i].rfind(".")
        if len(file_name_pre) == 0:
            file_name_pre = imgs[i][:pos_s+1]
            file_name_post = imgs[i][pos_e:]
            dig_bits = len(imgs[i][pos_s+1:pos_e])
        sort_imgs_pre.append(int(imgs[i][pos_s+1:pos_e])) 
        # print(file_name_pre)
        # print(file_name_post)
        # print(dig_bits)
        # print(imgs[i])
    sort_imgs_pre.sort()
    sort_imgs_pre = set(sort_imgs_pre)
    sort_imgs_pre = list(sort_imgs_pre)

    ## 排序后再将文件名恢复 
    for i in range(len(sort_imgs_pre)):
        # imgs[i] = "bx002_0_{:>06d}.jpg".format(imgs[i])
        sort_imgs.append("{}{:>06d}{}".format(file_name_pre,sort_imgs_pre[i],file_name_post))
        # print(imgs[i])
    return list(sort_imgs)

def do_label(imgs):
    '''
        标注工具的执行部分

        :param imgs: 所有待标注图片的路径集合
    '''
    global currentClass, current_labeled_cls, show, convas, convas_mouse, objs, labeled_num_rest

    endOf = False
    i = loadBreakpoint()  # 标注的图片编号断点

    while True:
        if i < 0:
            i = len(imgs) + i
        elif i > len(imgs) - 1:
            i = 0
        print("Breakpoint: ", i)
        saveBreakpoint(i)
        labeled_num_rest = len(imgs) - i
        current_jpg_name = os.path.basename(imgs[i][1])
        print("Breakpoint2: ", i)
        show = cv2.imread(imgs[i][1])
        convas = copy.deepcopy(show)
        convas_mouse = copy.deepcopy(show)

        pos = imgs[i][0].rfind(".")
        currentClass, objs = loadObjs("%s/%s.txt" %(path, imgs[i][0][:pos]))
        waitSecDown = False
        currentClass = current_labeled_cls
        while True:
            cv2.resize(show, (convas.shape[1], convas.shape[0]), convas)

            refreshCurrentShow(labeled_num_rest)
            cv2.setMouseCallback(wndName, onMouse)
            key = cv2.waitKey()
            key = key & 0xFF

            if key == 0x1B: #ESC
                endOf = True
                break

            if key >= ord('1') and key <= ord('9'):
                currentClass = key - ord('1')
                currentClass = max(currentClass, 0)
                currentClass = min(len(className) - 1, currentClass)
                current_labeled_cls = currentClass
                continue

            if key == ord('c'):
                # clear 时不是删除所有的框框,而是只删除当前标注类别的框. 
                for idx in range(len(objs)-1, -1, -1):
                    if currentClass == objs[idx][2]:
                        del objs[idx]
                continue

            if key == ord('k'):
                currentClass = 0
                objs = [] 
                continue
            if key == ord('y'):
                copyPreObjs(pre_labeled_file_name)
                continue
            
            if key == 82 or key == 44:   #up
                i = i - 2
                break

            if key == 84 or key == 46:   #down
                break

            if key == ord('p'):
                i = i - 2
                # if len(objs)>0:
                #     del objs[len(objs)-1]
                break

            if key == ord('s'): #s
                for obj_idx in range(len(objs)-1, -1, -1):
                    # xmin xmax
                    xmin = min(objs[obj_idx][0][0], objs[obj_idx][1][0])
                    xmax = max(objs[obj_idx][0][0], objs[obj_idx][1][0])
                    ymin = min(objs[obj_idx][0][1], objs[obj_idx][1][1])
                    ymax = max(objs[obj_idx][0][1], objs[obj_idx][1][1])
                    if xmax - xmin < 25 and ymax - ymin < 25:
                        print('invalid bbox with: xmin={}, xmax={}, ymin={}, ymax={}'.format(xmin, xmax, ymin, ymax))
                        print('Remove it!!!')
                        del objs[obj_idx]
                
                saveXML("%s/%s.xml" %(path, imgs[i][0][:pos]), objs, currentClass, show.shape[1], show.shape[0])
                break

        if endOf: break
        i = i+1


if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("--path", "-p", help="sepcify the path to dataset", required=True)
    args = vars(ap.parse_args())
    path = args["path"]

    imgs = os.listdir(path)
    print('1', imgs[:3])
    imgs = sort_as_filename(imgs)

    print('2', imgs[:3])
    for i in range(len(imgs)-1, -1, -1):
        if (not imgs[i].lower().endswith("jpg")) and not imgs[i].lower().endswith("png") and (not imgs[i].lower().endswith("jpeg")):
            print(imgs[i])
            del imgs[i]

    imgs = [(imgs[i], path + "/" + imgs[i]) for i in range(len(imgs))]

    if len(imgs) == 0:
        print('empty imgs dir.')
        exit(1)

    do_label(imgs)
