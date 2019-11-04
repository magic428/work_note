# coding: utf-8
import cv2
import os
import copy
import argparse

'''
    截取视频, 按下 "s" 键表示开始截取, 
    按下 "q" 表示停止当前截取, 
    按下 "ESC" 表示停止程序
'''

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", help="path of video file", required=True)
args = ap.parse_args()
args = vars(args)

filename = args["path"]

cap = cv2.VideoCapture(filename)

if not cap.isOpened():
    print("{} open failed!".format(filename))

# 视频参数
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# n_frames = round(cap.get(cv2.CAP_PROP_FRAME_COUNT))
n_frames = 1000
# fps = round(cap.get(cv2.CAP_PROP_FPS))
fps = 30
fourcc = round(cap.get(cv2.CAP_PROP_FOURCC))

if not fourcc == cv2.VideoWriter_fourcc('M', 'P', '4', '2'):
#    fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', '2')
   fourcc = cv2.VideoWriter_fourcc('M', 'P', 'E', 'G')

(filename, ext) = os.path.splitext(filename)
output_filename = "{}_out{}".format(filename, ext)
print(output_filename)

vw = cv2.VideoWriter(output_filename, int(fourcc), round(fps), (width, height))
#vw = cv2.VideoWriter("a.mp4", int(fourcc), round(fps), (width, height))

grab = False
ret = True
# while n_frames or ret:
while True:

    ret, frame = cap.read()
    convas = copy.deepcopy(frame)

    if ret:
        if grab:
            cv2.putText(convas, "recording...", (10, 10), cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 255, 0))
            vw.write(frame)

        cv2.imshow("srteam", convas)
        key = cv2.waitKey(30)
        key = key & 0xFF;

        if(key == ord('s') or key == ord('S')):
            grab = True
        elif(key == ord('q') or key == ord('Q')):
            grab = False
        elif(key == 27):
            grab = False
            cap.release()
            vw.release()
            cv2.destroyAllWindows()
    else:
        break
    n_frames -= 1
