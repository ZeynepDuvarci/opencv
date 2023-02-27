#27.02.2023
import cv2
import numpy as np

img=cv2.imread('resourcesAndOutputs/giraffe.jpg')
cv2.imshow('Giraffe',img)

#translation- shifting an image along the x and y axis
def translate(img, x, y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    #width-hight
    dimensions=(img.shape[1],img.shape[0])
    return cv2.warpAffine(img,transMat,dimensions)

# -x --> left
# -y --> up
#  x --> right
#  y --> down

translated=translate(img, -50, 50)

cv2.imshow('Translated Giraffe',translated)

# rotation
def rotate(img,angle, rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
        
    rotMat=cv2.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    
    return cv2.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,45)
cv2.imshow('Rotated Giraffe',rotated)

# flipping
#  0 - flip vertically
#  1 - flip horizontally
# -1 - flip an image both vertically and horizontally
flip= cv2.flip(img, 0)
cv2.imshow('Flipped Giraffe',flip)

cv2.waitKey(0)
cv2.destroyAllWindows()