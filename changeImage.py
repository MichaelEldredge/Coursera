#!/usr/bin/env python3
from PIL import Image
from os import listdir

imagelist = listdir("supplier-data/images")
for item in imagelist:
    impath = "supplier-data/images/" + item
    if impath[len(impath)-5 :] == ".tiff":
        print("converting")
        savename = impath[:-5] + ".jpeg"
        im = Image.open(impath)
        newim = im.convert('RGB')
        newim = newim.resize((600,400))
        newim.save(savename)
