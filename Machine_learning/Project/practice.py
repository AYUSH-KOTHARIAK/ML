import cv2
import matplotlib.pylab as py
vid=cv2.VideoCapture()
img=vid.read()
cv2.imshow('camera',img)
cv2.waitKey(0)
cv2.destroyAllWindows()