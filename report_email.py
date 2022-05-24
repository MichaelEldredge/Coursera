#!/usr/bin/env python3
import emails
import os
import re
import datetime

def generate_pdf():
    descpath = "supplier-data/descriptions"
    pdf = ""
    desclist = os.listdir(descpath)
    for desc in desclist:
        trimname = re.search("\w*",desc).group(0)
        with open(descpath + "/" + trimname + ".txt") as f:
            mylist = f.readlines()
            name = mylist[0]
            weight = int(re.search('[0-9]+' ,mylist[1] ).group(0))
            pdf +=  f"name: {name}<br />weight: {weight} lbs<br/><br/>"

    return pdf

#message = emails.generate_email("Upload Completed - Online Fruit Store", \
#                      "All fruits are uploaded to our website successfully. A detailed list is attached to this email.", \
#                      "processed.pdf")
#emails.send_email(message)

if __name__ == "__main__":
    pdf_body = generate_pdf()
    title = f"Process Updated on {datetime.date.today()}"
    reports.generate_report("processed.pdf", title, pdf_body)


