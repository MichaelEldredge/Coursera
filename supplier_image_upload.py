#!/usr/bin/env python3
import requests
from os import listdir

url = "http://localhost/upload/"
imagelist = listdir("supplier-data/images")
for item in imagelist:
    impath = "supplier-data/images/" + item
    if impath[len(impath)-5 :] == ".jpeg":
       with open(impath, 'rb') as opened:
           r = requests.post(url, files={'file': opened})
