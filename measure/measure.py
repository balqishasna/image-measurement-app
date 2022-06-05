import cv2
from numpy import angle
from object_detector import *
import numpy as np
#Load  Aruco detector
#parameters = cv2.aruco.DetectorParameters_create()
#aruco_dict = cv2.aruco.Dictionary.get(cv2.aruco.DICT_5X5_50)


img = cv2.imread("koex.jpeg")


detector = HomogeneousBgDetector()


contours = detector.detect_objects(img)

for cnt in contours:
    # Get rect
    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect

    
    # display rectangle
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
    cv2.polylines(img, [box], True, (255, 0, 0), 2)
    cv2.putText(img, "Width {}".format(round(w, 1)), (int (x), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2) 
    cv2.putText(img, "Height {}".format(round(h, 1)), (int (x), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2) 


cv2.imshow("image", img)
cv2.waitKey(0)