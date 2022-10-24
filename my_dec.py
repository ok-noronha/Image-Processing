# Taking two images and combining them into one.
import cv2
import numpy
import os, sys

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

img4 = cv2.imread(infile1)
img5 = cv2.imread(infile2)

overlap = cv2.add(img4, img5)
cv2.imwrite("dog_overlap.png",overlap)

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
				for z in y:#channels in a pixel
					c.append(z)
					countz+=1
				b.append(c)
			county+=1
		a.append(b)
	countx+=1

final=numpy.array(a)
cv2.imwrite("dog_final.png",final)
