from PIL import Image, ImageDraw
import os, sys
#from random import SystemRandom
#random = SystemRandom()
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
img.save("dog_bw.png", 'PNG')


width=img.size[0]*3
height=img.size[1]*3

out_image_A = Image.new('1', (width, height))
out_image_B = Image.new('1', (width, height))
out_image_C = Image.new('1', (width, height))

draw_A = ImageDraw.Draw(out_image_A)
draw_B = ImageDraw.Draw(out_image_B)
draw_C = ImageDraw.Draw(out_image_C)

shares = [draw_A, draw_B, draw_C]

patternsB = [[1,0,1,0,0,0,0,0,1],[0,0,1,0,0,0,1,0,0],[1,0,0,0,0,0,1,0,1]]
patternsW = [[1,0,1,0,0,0,0,0,1],[0,0,1,0,1,0,1,0,0],[1,0,0,0,1,0,1,0,1]]

for x in range(0, width//3):
	for y in range(0, height//3):
		pixel=img.getpixel((x,y))
		pats=[[0]]
		if pixel != 0:
			pats=[[1,0,1,0,0,0,0,0,1],[0,0,1,0,1,0,1,0,0],[1,0,0,0,1,0,1,0,1]]
		else:
			pats=[[1,0,1,0,0,0,0,0,1],[0,0,1,0,0,0,1,0,0],[1,0,0,0,0,0,1,0,1]]

		for share in shares:
			pat = random.choice(pats)
			pats.remove(pat)
			share.point((x*3, y*3), pat[0])
			share.point((x*3+1, y*3), pat[1])
			share.point((x*3+2, y*3), pat[2])
			share.point((x*3, y*3+1), pat[3])
			share.point((x*3+1, y*3+1), pat[4])
			share.point((x*3+2, y*3+1), pat[5])
			share.point((x*3, y*3+2), pat[6])
			share.point((x*3+1, y*3+2), pat[7])
			share.point((x*3+2, y*3+2), pat[8])
		
out_image_A.save(out_filename_A, 'PNG')
out_image_B.save(out_filename_B, 'PNG')
out_image_C.save(out_filename_C, 'PNG')
print("Done.")
