#! /usr/bin/env python3

import os
import requests
import json
import re

url = "http://localhost/fruits/"
lin_inst_ext = "35.232.216.221"
post_address = "http://" + lin_inst_ext + "/fruits"
desclist = os.listdir("supplier-data/descriptions")
for desc in desclist:
    trimname = re.search("\w*",desc).group(0)
    print(trimname)
    with open("supplier-data/descriptions/" + trimname + ".txt") as f:
        mylist = f.readlines()
        name = mylist[0]
        weight = int(re.search('[0-9]+' ,mylist[1] ).group(0))
        description = mylist[2]
        picname = trimname + ".jpeg"
        m = {'name':name, 'weight':weight, 'description':description, 'image_name':picname}
        response = requests.post(url, json=m)
        response.raise_for_status()
