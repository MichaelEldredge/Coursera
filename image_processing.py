from PIL import Image
from os import listdir
import glob

imagelist = listdir("images")
for item in imagelist:
    impath = "images/" + item
    savename = impath[:-4] + ".jpg"
    im = Image.open(impath)
    newim = im.convert('RGB')
    newim = newim.resize((600,400))
    newim.save(savename)

