import cv2;
import matplotlib.pyplot as plt


im = cv2.imread("car.jpg")
cv2.imshow('image',im)
cv2.waitKey(0)
plt.imshow('image',im)
plt.plot()
print(type(im))