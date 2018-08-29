import cv2
import numpy as np

def get_contour_areas(contour):
    all_areas=[]
    for cnt in contours:
        areas=cv2.contourArea(cnt)
        all_areas.append(areas)
        return all_areas

img=cv2.imread("img3.jpg")
original_img=img

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edged=cv2.Canny(gray,50,200)
cv2.imshow("Canny edged",edged)
cv2.waitKey(0)

_,contours,hierarchy=cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

print("Contour area before sorting"),
print(get_contour_areas(contours))

sorted_contours=sorted(contours,key=cv2.contourArea,reverse=True)

print("Contour area before sorting")
print(get_contour_areas(sorted_contours))

for c in sorted_contours:
    cv2.drawContours(original_img,[c],-1,(255,0,0),3)
    cv2.waitKey(0)
    cv2.imshow("Contour by are",original_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
