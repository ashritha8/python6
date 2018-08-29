import cv2
import numpy as np

img=cv2.imread('lena.jpg')

height,width=img.shape[:2]

start_row4,start_col4=int(height*.0),int(width*.0)

end_row4,end_col4=int(height*.25),int(width*.25)

cropped=img[start_row4:end_row4,start_col4:end_col4]


start_row,start_col=int(height*.25),int(width*.25)

end_row,end_col=int(height*.50),int(width*.50)
cropped2=img[start_row:end_row,start_col:end_col]


start_row2,start_col2=int(height*.50),int(width*.50)

end_row2,end_col2=int(height*.75),int(width*.75)
cropped3=img[start_row2:end_row2,start_col2:end_col2]


start_row3,start_col3=int(height*.75),int(width*.75)

end_row3,end_col3=int(height*1.0),int(width* 1.0)
cropped4=img[start_row3:end_row3,start_col3:end_col3]










cv2.imshow('Original',img)
cv2.waitKey(0)

cv2.imshow('Cropped',cropped)
cv2.waitKey(0)
cv2.imshow('Cropped1',cropped2)
cv2.waitKey(0)
cv2.imshow('Cropped2',cropped3)
cv2.waitKey(0)
cv2.imshow('Cropped3',cropped4)
cv2.waitKey(0)

cv2.destroyAllWindows()
