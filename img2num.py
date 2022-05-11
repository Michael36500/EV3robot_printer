import cv2
import numpy as np

path = "img.jpg"

img = cv2.imread(path, 0)
img = img.astype(np.uint8)

th, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

for line in img:
    # print(line, "   *")
    for segment in line:
        print(segment)