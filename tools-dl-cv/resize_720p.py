import cv2
import os
import argparse

if __name__ == "__main__":
    # Standard data directory
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", "-p", help="sepcify the path to dataset", required=True)
    args = vars(ap.parse_args())
    path = args["path"]
    if path[-1] == os.sep:
        path = path[:-1]

    root_dir = path
    print("root_dir: ", root_dir)
    dirs = os.listdir(root_dir)
    for dir_name in dirs:
        print("Processing ", dir_name, "...")
        dir_path = os.path.join(root_dir, dir_name)
        img_names = os.listdir(dir_path)
        for img_name in img_names:
            if(img_name.endswith(".jpg")):
                img_path = os.path.join(dir_path, img_name)
                # print(img_path)
                img = []
                img = cv2.resize(cv2.imread(img_path), (1536, 864))
                # img = cv2.resize(cv2.imread(img_path), (1280, 720))
                # print(img.shape)
                cv2.imwrite(img_path, img, [cv2.IMWRITE_JPEG_QUALITY, 100])