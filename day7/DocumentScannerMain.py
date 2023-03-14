import utils
import cv2
import numpy as np

webCamFeed = True
cap= cv2.VideoCapture(0)
cap.set(10,160)
heightImg=640
widthImg=480

utils.initializeTrackbars()
count=0