#! /usr/bin/env python3

import os
import requests
import json
import re

lin_inst_ext = ""
post_address = "http://" + lin_inst_ext + "/fruits"
desclist = os.listdir('Descriptions')
for desc in desclist:
    trimname = re.search("\w*",desc).group(0)
    print(trimname)
    with open("Descriptions/" + trimname + ".txt") as f:
        mylist = f.readlines()
        name = mylist[0]
        weight = int(re.search('[0-9]+' ,mylist[1] ).group(0))
        description = mylist[2]
        picname = trimname + ".jpeg"
        m = json.dumps({'name':name, 'weight':weight, 'description':description, 'image_name':picname})
        requests.post(post_address, m)