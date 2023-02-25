#25.02.2023

# if you have this issue "ModuleNotFoundError: No module named 'cv2'" 
# you can try delete module and install again

# if your code is working but cv2 is red then you should go  Control+Shift+p
# and chose Preferences: Open User Settings(JSON) 
# add "python.linting.pylintArgs": ["--generate-members"], on top. 

import cv2
import numpy as np

# image to numpy array
img=cv2.imread("giraffe.jpg")
# gray version 
img0=cv2.imread("giraffe.jpg",0)

# save new image
cv2.imwrite("graygiraffe.jpg",img0)

# copy image
img1=img.copy()

# imshow(frame label, image array that you want to show)
cv2.imshow("Giraffe", img)
cv2.imshow("Gray Giraffe", img0)

# if you want to see array
# print(img)
print("Image size:",img.size)
print("Image data type:",img.dtype)
print("Image shape:",img.shape)

print("Gray image shape",img0.shape)
print("Gray image size:",img0.size)
print("Gray image data type:",img0.dtype)

# b,g,r -> blue, green, red 
# color values must be in 0-255, 1 pixel is 8 bit
blue,green,red=img[:,:,0],img[:,:,1],img[:,:,2]

#you can notice slight difference between images
cv2.imshow("Blue",blue)
cv2.imshow("Green",blue)
cv2.imshow("Red",blue)

# if you want to see bgr value of a certain pixel
print(img[(50,30)])
# output : [249 226 200]

# changing certain pixel to red pixel
img[50,30]=[0,0,255]
cv2.imshow("Red Pixel",img)

img[0:50,30]=[0,0,255]
cv2.imshow("Red Vertical Line",img)

img[0:50,0:30]=[0,0,255]
cv2.imshow("Red Rectangle",img)

cv2.waitKey(0)
cv2.destroyAllWindows()