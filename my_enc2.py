import random
from PIL import Image, ImageDraw
import os, sys, cv2
import numpy as np

share_files = []
shares=[]
temp_shares=[]



def __init__():
    if len(sys.argv)!=1:
        print("This takes one argument; the image to be split.")
        exit()
    #infile=str(sys.argv[1])
    global infile
    infile ="dog.jpeg"

    if not os.path.isfile(infile):
        print("That file does not exist.")
        exit()

    global img
    img = cv2.imread(infile)

    global file
    global ext
    file, ext = os.path.splitext(infile)


    global n; global k
    n=int(input("Number of Shares to be made :"))
    k=int(input("Number of Shares need to get picture :"))

    global rows, columns, channels
    rows, columns, channels = img.shape



def create_shares():
    for i in range(1,n+1):
        share_files.append(file+str(i)+".png")
        r=[]
        for row in img:
            col=[]
            r.append(col)
            for pix in row:
                ch=[]
                col.append(ch)
                for channel in pix:
                    ch.append(80)
        shares.append(np.array(r))

def share_mod():
    global shares
    global temp_shares
    for row in range(rows):
        for pix in range(columns):
            for channel in range(channels):
                val=img[row,pix,channel]
                nums=[]
                temp_shares=[]
                for _ in range(1,k):
                    num = random.randint(0,val)
                    nums.append(num)
                    share=shares.pop(random.randint(0,len(shares)-1))
                    share[row,pix,channel]=num
                    val-=num
                    temp_shares.append(share)
                share=shares.pop(random.randint(0,len(shares)-1))
                share[row,pix,channel]=val
                nums.append(val)
                temp_shares.append(share)

                for _ in range(0,n-k):
                    share=shares.pop(random.randint(0,len(shares)-1))
                    share[row,pix,channel]=max(nums)
                    temp_shares.append(share)
                shares=temp_shares



def save_shares():
    for i in range(len(shares)):
        cv2.imwrite(share_files[i],shares[i])


__init__()
create_shares()
share_mod()
save_shares()