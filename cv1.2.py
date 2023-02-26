# 26.02.2023
import cv2

img=cv2.imread('giraffe.jpg')
cv2.imshow('Original Giraffe',img)

# converting to grayscale
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Giraffe',gray)

# bluring
blur= cv2.GaussianBlur(img,(3,3),cv2.BORDER_DEFAULT)
cv2.imshow('Blurry Giraffe',blur)

# edge cascade
canny= cv2.Canny(img,125,175)
cv2.imshow('Giraffe Edges', canny) 

# blur edge cascade
# for reducing edges
canny= cv2.Canny(blur,125,175)
cv2.imshow('Blurry Giraffe Edges', canny) 

# dilating the image
dilated= cv2.dilate(canny,(3,3),iterations=1)
cv2.imshow('Dilated Giraffe',dilated)

# eroding
eroded=cv2.erode(dilated,(3,3),iterations=1)
cv2.imshow('Eroded Giraffe',eroded)

# resize
# INTER_AREA is useful while you're shrinking
# INTER_LINEAR is useful while enlarging
# INTER_CUBIC slow but higher quality
resized= cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized Giraffe',resized)

# cropping
cropped=img[10:125,63:170]
cv2.imshow('Cropped Giraffe',cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()