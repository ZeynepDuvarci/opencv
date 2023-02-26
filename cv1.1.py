# 26.02.2023
import cv2

img=cv2.imread('giraffe.jpg')
cv2.imshow('Original Giraffe',img)

# blue effect
img[:,:,0]=255

# green effect
#img[:,:,1]=255

# red effect
#img[:,:,2]=255 

# specific location 
img[10:125,63:170,2]=255 


cv2.imshow('Blue Giraffe',img)

cv2.waitKey(0)
cv2.destroyAllWindows()