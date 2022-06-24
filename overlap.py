import cv2

img1 = cv2.imread("dog_A.png")
img2 = cv2.imread("dog_B.png")
img3 = cv2.imread("dog_C.png")

#final = cv2.subtract(img2, img1)
final = cv2.add(img1, img3)
r, c, x = final.shape
final = cv2.resize(final,(r//3,c//3),interpolation=cv2.INTER_AREA)
cv2.imwrite("overlp.png",final)
#final = cv2.addWeighted(img1,0.7,img2,0.7,0)
cv2.imshow('img', final)
cv2.waitKey(0)
cv2.destroyAllWindows()
