import cv2
import numpy as np

with open('0.bmp', 'rb') as f:
    img1 = f.read()
with open('1.bmp', 'rb') as f:
    img2 = f.read()
pic1=cv2.imdecode(np.frombuffer(img1, dtype=np.uint8),cv2.IMREAD_ANYCOLOR)
pic2=cv2.imdecode(np.frombuffer(img2, dtype=np.uint8),cv2.IMREAD_ANYCOLOR)

img_v = cv2.vconcat([pic1, pic2])
cv2.imwrite("test.bmp", img_v)