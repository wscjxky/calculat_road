import cv2
a=cv2.imread("logo.jpg")
a=a[60:220,100:280]
cv2.imwrite("logo.png",a)