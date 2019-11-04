import cv2
import os
import sys

root_dir = 'D:/data/videos/yjl2028_检修人员/origin/'
video_names = os.listdir(root_dir)
pic_dir_pre = 'D:/data/objs/yjl1028/'
dataset_prefix = 'yjl1028_minerY_'
dir_idx = 0
img_cnt = 0
videos_cnt = len(video_names)
cnt = 0
break_point = 34

# processing %d(%d)... (34, 50)


for video_name in video_names:
    i = 0
    video_path = root_dir + video_name

    if not os.path.exists(video_path):
        print("No Such file: {}".format(video_path))
        sys.exit(1)
    
    cap = cv2.VideoCapture(video_path)
    data_dir = "{}/{}{:>04d}/".format(pic_dir_pre, dataset_prefix, dir_idx)
    # data_dir = root_dir + "mutilObjs_" + os.path.splitext(video_name)[0]+ "/"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    while True:
        if not cap:
            print("video error")

        ret, frame = cap.read()

        # cv2.imshow("demo", frame)
        # if(27 == cv2.waitKey(1)):
        #     cv2.destroyAllWindows()
        if not ret: 
            print("split done!")
            videos_cnt -= 1 
            cnt += 1
            print("processing {}({})...".format(cnt ,len(video_names)))
            print("each video can split {} pics".format(img_cnt))
            break

        if i%20 == 0:
            # cv2.imwrite(data_dir+'mutilObjs_{:>06d}.jpg'.format(int(i/10)), frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100]) 
            img_cnt += 1
            if(img_cnt % 1000 == 0):
                dir_idx += 1
                data_dir = "{}/{}{:>04d}/".format(pic_dir_pre, dataset_prefix, dir_idx)
                if not os.path.exists(data_dir):
                    os.makedirs(data_dir)
                print("new dir...")

            cv2.imwrite(data_dir+'{}{:>06d}.jpg'.format(dataset_prefix, img_cnt), frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100]) 
        if(i == 100000):
            i = 0
        i += 1
