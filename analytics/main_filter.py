import numpy as np
import cv2

filename = "1/LT05_L1TP_014033_19950123_20160926_01_T1_B5.TIF"
filename = "SaltonSeaLandSat1999.TIF"

from PIL import Image


def hops(hierarchy, index):
    counter = 0

    if index != -1:
        while hierarchy[0][index][3] > 0:
            #print(counter, index, hierarchy[0][index][3])

            index = hierarchy[0][index][3]
            counter += 1

    return counter




im = Image.open(filename)
#im.show()
#This showed the rainbow image. To convert to a numpy array, it's as simple as:
imarray = np.array(im)




im = cv2.imread(filename, cv2.IMREAD_COLOR)
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
imgray_c = cv2.cvtColor(imgray, cv2.COLOR_GRAY2BGR)
min = np.min(imgray)
max = np.max(imgray)
mean = np.mean(imgray)
print(min, max, mean)
ret, thresh = cv2.threshold(imgray, int(mean)-47, 255, cv2.THRESH_BINARY) #int(np.max(imgray))-25, 255, cv2.THRESH_BINARY)
cv2.imwrite("out2_thresh.png", thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


import random

for data in range(len(contours)):

    if hierarchy[0][data][3] > 0:
        if hops(hierarchy, data) >= 0:
            # print(contours[data])
            cv2.drawContours(imgray_c, contours[data], -1,
                             (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 5)

            M = cv2.moments(contours[data])

            # calculate x,y coordinate of center
            if M["m00"] > 0.0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

                # print(cX, cY)

print(len(im), len(im[0]))
# cv2.imshow('output', im)

cv2.imwrite("out2_contours.png", imgray_c)  # im[0:1000][0:1000]

#cv2.imwrite("out.png", thresh)

print("p", len(thresh), len(thresh[0]))

new = np.zeros((len(thresh), len(thresh[0])))
'''
for i in range(0, len(thresh)-5000, 1):
    for j in range(0, len(thresh[i])-1, 1):
        if np.sum(thresh[i - 1 : i + 1, j -1 : j +1]) > 0:
            new[i][j] = 255
    print(i)

cv2.imwrite("out.png", new)
'''