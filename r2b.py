import cv2

img1=cv2.imread('dog.jpeg', 1)

img = cv2.resize(img1, (20, 20), interpolation=cv2.INTER_AREA)

cv2.imwrite("rs_dog.jpeg", img)

gray_img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray_dog.jpeg", gray_img)

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray_rs_dog.jpeg", gray_img)

ret, bw = cv2.threshold(gray_img, 160, 255, cv2.THRESH_BINARY)
cv2.imwrite("bw_dog.jpeg", bw)

f=open("array.txt",'w')
for s in bw:
	for v in s:
		c = str(v)
		f.write("%5s"%c)
		f.write("    ")
	f.write("\n")

f.close()
cv2.imshow('img', bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
