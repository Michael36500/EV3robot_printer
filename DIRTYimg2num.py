import cv2
import numpy as np
from datetime import datetime

############################################################################################################################################################
#!! pozor na orientaci, teď je normálně (hlavou vzhůru)
# dám začátek programu
Time = datetime.now()
print(Time)
# micstart = Time.microsecond
# secstart = Time.second

#####################
# DĚLÁM ARRAY ČÍSEL #
#####################
out = []
multiout = []
arli = []

path = "img.jpg"

img = cv2.imread(path, 0)
img = img.astype(np.uint8)

# protože pro další blok potřebuji jednodimenziální pole, ale může se hodit více, tak dělám pole OUT (jedno) a MULTIOUT (multi)


th, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
# print(img)
for line in img:
    # print(line, "   *")
    for sgm in line:
        if sgm == 255:
            sgm = 1
        arli.append (sgm)
        out.append(sgm)
    out.append(2)
    arli.append(2)
    # print(arli)
    multiout.append (arli)
    arli = []
# out = multidimenzionální pole [[][]]

# print(out)

############################
# ZJEDNODUŠENÍ + ZRYCHLENÍ #
############################    

inp = out

out = []

hled = 0    # hledané
cis = 0   # počet stejných za sebou




for pos in inp:
    # if pos == hled:
    #     cis = cis + 1
    # else:
    #     hled = 1
    #     vys.append (cis)
    #     cis = 1
    if pos == 2:
        out.append (cis)
        cis = 0
        out.append (-1)
        hled = 0
        continue


    if pos != hled:
        hled = 1 if hled == 0 else 0 
        out.append (cis)
        cis = 0

    cis = cis + 1


out.append (cis)
# for line in inp:
#     for char in line:
#         # if char == 2:
#         #     out.append(p_rad)
#         #     p_rad = 0
#         if char == 2:
#             out.append (p_rad)
#             p_rad = 0
#             out.append (-1)
#             hled = 0
#             continue

#         if char != hled:
#             hled = 1 if hled == 0 else 0
#             out.append (p_rad)
#             p_rad = 0

#         p_rad = p_rad + 1


#         # if char == hled:
#         #     p_rad = p_rad + 1

#         # if char != hled:
#         #     out.append(p_rad)
#         #     p_rad = 0
#             # hled = 1 if hled == 0 else 0
print(out)

# konec
Time = datetime.now()
print(Time)
# micend = Time.microsecond
# secend = Time.second
# print(micend - micstart)
# print(secend - secstart)