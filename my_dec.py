
import cv2
import numpy
import os, sys
#from PIL import Image, ImageDraw
#import os, sys
#import skimage                 
#import skimage.io              
#from skimage.io import imread 

if len(sys.argv)!=3:
	print("This takes two arguments.")
	exit()

infile1=str(sys.argv[1])
infile2=str(sys.argv[2])

if not os.path.isfile(infile1):
	print("That file 1 does not exist.")
	exit()

if not os.path.isfile(infile2):
	print("That file 2 does not exist.")
	exit()

img1 = cv2.imread("dog_A.png")
img2 = cv2.imread("dog_B.png")
img3 = cv2.imread("dog_C.png")
img4 = cv2.imread(infile1)
img5 = cv2.imread(infile2)

#final = cv2.subtract(img2, img1)
#final = cv2.resize(final,(r//3,c//3),interpolation=cv2.INTER_AREA)
#final = cv2.addWeighted(img1,0.7,img2,0.7,0)
overlap = cv2.add(img4, img5)
overlap = cv2.add(overlap, img1)
#r, c, x = final.shape
#cv2.imshow('img', final)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imwrite("dog_overlap.png",overlap)


#zero = skimage.io.imread("dog_overlap.png", 1)
#width=zero.shape[1]
#height=zero.shape[0]

#final.save("dog_final.png", 'PNG')

#final1=skimage.io.imread("dog_final.png",1)
#for h in range(final1.shape[0]):
#	for w in range(final1.shape[1]):
#		final1[h,w]=zero[(h*3)+1,(w*3)+1]

#cv2.imwrite("dog_final.png",final1)
#print("Done.")


a=[]
countx=0
for x in overlap:#rows in the image
	if countx%3==1:
		b=[]
		county=0
		for y in x:#pixels in a row
			if county%3==1:
				c=[]
				countz=0
				for z in y:#chanels in a pixel
					#z=0 if count==0 else z
					c.append(z)
					countz+=1
				b.append(c)
			county+=1
		a.append(b)
	countx+=1

final=numpy.array(a)
cv2.imwrite("dog_final.png",final)

