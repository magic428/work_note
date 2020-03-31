import cv2
import os
import sys

split_step = 1

root_dir = '/home/magic/ws-seafile/data/videos/small-mobilecar-vio/seg/'
video_names = os.listdir(root_dir)
pic_dir_pre = '/home/magic/ws-seafile/data/slam-vio/yjl_coalwall/dataset/sequences'
dataset_prefix = ''
dir_idx = 1
img_cnt = 0
videos_cnt = len(video_names)
cnt = 0
break_point = 34

# processing %d(%d)... (34, 50)

grab = False
ret = True
for video_name in video_names:
    i = 0
    video_path = root_dir + video_name

    if not os.path.exists(video_path):
        print("No Such file: {}".format(video_path))
        sys.exit(1)
    
    cap = cv2.VideoCapture(video_path)
    # data_dir = "{}/{}{:>04d}/".format(pic_dir_pre, dataset_prefix, dir_idx)
    # data_dir = root_dir + "mutilObjs_" + os.path.splitext(video_name)[0]+ "/"
    # if not os.path.exists(data_dir):
    #     os.makedirs(data_dir)

    while True:
        if not cap:
            print("video error")

        ret, frame = cap.read()
        cv2.imshow("srteam", frame)
        key = cv2.waitKey(30)
        key = key & 0xFF

        if(key == ord('s') or key == ord('S')):
            grab = True
        elif(key == ord('q') or key == ord('Q')):
            grab = False
        elif(key == 27):
            grab = False
            cap.release()
            vw.release()
            cv2.destroyAllWindows()

        if grab:
            if not ret: 
                videos_cnt -= 1 
                cnt += 1
                print("each video can split {} pics".format(img_cnt))
                break

            data_dir = pic_dir_pre
            data_dir = "{}/{:>02d}/image_1/".format(pic_dir_pre, dir_idx)
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)

            cv2.imwrite(data_dir+'{:>06d}.png'.format(img_cnt), frame) 
            img_cnt += 1

        if(i == 100000):
            i = 0
        i += 1

    print("split done!")
