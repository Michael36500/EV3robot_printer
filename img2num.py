import cv2
import numpy as np

#####################
# DĚLÁM ARRAY ČÍSEL #
#####################

out = []
arli = []

path = "img.jpg"

img = cv2.imread(path, 0)
img = img.astype(np.uint8)

th, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
for line in img:
    # print(line, "   *")
    for sgm in line:
        if sgm == 255:
            sgm = 1
        arli.append (sgm)
    print(arli)
    out.append (arli)
    arli = []
print(out)