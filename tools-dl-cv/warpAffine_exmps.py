import cv2
import numpy as np

theta = 25 * np.pi / 180
img = cv2.imread("/home/magic/data_dl/tdmc_objs/td_all/JPEGImages/miner_00269.jpg")

# x轴的剪切shear变换，角度45°
M_shear = np.array([
    [1, -np.tan(theta), 0],
    [0, 1, 0]
], dtype=np.float32)

img_sheared = cv2.warpAffine(img, M_shear, (1000, 1500), cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=255)
cv2.imwrite('img_sheared.jpg', img_sheared)

M_rotate = np.array([
    [np.cos(-theta), -np.sin(-theta), 0],
    [np.sin(-theta), np.cos(-theta), 0]
], dtype=np.float32)

img_rotated = cv2.warpAffine(img_sheared, M_rotate, (800, 1200), cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=255)
cv2.imwrite('img_rotated.jpg', img_rotated)

