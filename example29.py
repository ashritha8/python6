import cv2
import numpy as np

img=cv2.imread("lena.jpg")
cv2.imshow('Origin Image',img)
cv2.waitKey(0)

kernel_3X3=np.ones((3,3), np.float32)/9

blurred=cv2.filter2D(img,-1,kernel_3X3)
cv2.imshow('3*3 Kernel Blurring',blurred)
cv2.waitKey(0)

kernel_15X15=np.ones((15,15),np.float32)/225

blurred2=cv2.filter2D(img,-1,kernel_15X15)
cv2.imshow('15*15 Kernel Blurring',blurred2)
cv2.waitKey(0)
