from PIL import Image, ImageDraw
import os, sys
from random import SystemRandom
random = SystemRandom()
#If you want to use the more powerful PyCrypto (pip install pycrypto) then uncomment the next line and comment out the previous two lines
#from Crypto.Random import random

if len(sys.argv)!=2:
	print("This takes one argument; the image to be split.")
	exit()
infile=str(sys.argv[1])

if not os.path.isfile(infile):
	print("That file does not exist.")
	exit()

img = Image.open(infile)

f, e = os.path.splitext(infile)
out_filename_A=f+"_A.png"
out_filename_B=f+"_B.png"
out_filename_C=f+"_C.png"

img=img.convert('1')#convert image to 1 bit

#Prepare two empty slider images for drawing
width=img.size[0]*3
height=img.size[1]*3

out_image_A = Image.new('1', (width, height))
out_image_B = Image.new('1', (width, height))
out_image_C = Image.new('1', (width, height))

draw_A = ImageDraw.Draw(out_image_A)
draw_B = ImageDraw.Draw(out_image_B)
draw_C = ImageDraw.Draw(out_image_C)

patternsB = [[0,0,0,0,1,1,1,0,0],[0,1,0,0,0,0,0,1,1],[1,0,1,1,0,0,0,0,0]]
patternsW = [[0,1,0,1,0,1,1,1,0],[0,1,0,1,0,1,0,1,1],[1,1,1,1,0,1,0,1,0]]

#Cycle through pixels
for x in range(0, width//3):
	for y in range(0, height//3):
		pixel=img.getpixel((x,y))
		pats=[[0]]
		if pixel == 0:
			pats=[[0,0,0,0,1,1,1,0,0],[0,1,0,0,0,0,0,1,1],[1,0,1,1,0,0,0,0,0]]
		else:
			pats=[[0,1,0,1,0,1,1,1,0],[0,1,0,1,0,1,0,1,1],[1,1,1,1,0,1,0,1,0]]

		pat = random.choice(pats)
		pats.remove(pat)
		draw_A.point((x*3, y*3), pat[0])
		draw_A.point((x*3+1, y*3), pat[1])
		draw_A.point((x*3+2, y*3), pat[2])
		draw_A.point((x*3, y*3+1), pat[3])
		draw_A.point((x*3+1, y*3+1), pat[4])
		draw_A.point((x*3+2, y*3+1), pat[5])
		draw_A.point((x*3, y*3+2), pat[6])
		draw_A.point((x*3+1, y*3+2), pat[7])
		draw_A.point((x*3+2, y*3+2), pat[8])
		pat = random.choice(pats)
		pats.remove(pat)
		draw_B.point((x*3, y*3), pat[0])
		draw_B.point((x*3+1, y*3), pat[1])
		draw_B.point((x*3+2, y*3), pat[2])
		draw_B.point((x*3, y*3+1), pat[3])
		draw_B.point((x*3+1, y*3+1), pat[4])
		draw_B.point((x*3+2, y*3+1), pat[5])
		draw_B.point((x*3, y*3+2), pat[6])
		draw_B.point((x*3+1, y*3+2), pat[7])
		draw_B.point((x*3+2, y*3+2), pat[8])
		pat = random.choice(pats)
		pats.remove(pat)
		draw_C.point((x*3, y*3), pat[0])
		draw_C.point((x*3+1, y*3), pat[1])
		draw_C.point((x*3+2, y*3), pat[2])
		draw_C.point((x*3, y*3+1), pat[3])
		draw_C.point((x*3+1, y*3+1), pat[4])
		draw_C.point((x*3+2, y*3+1), pat[5])
		draw_C.point((x*3, y*3+2), pat[6])
		draw_C.point((x*3+1, y*3+2), pat[7])
		draw_C.point((x*3+2, y*3+2), pat[8])

out_image_A.save(out_filename_A, 'PNG')
out_image_B.save(out_filename_B, 'PNG')
out_image_C.save(out_filename_C, 'PNG')
print("Done.")
