#!/usr/bin/env python3

import os
import datetime
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
import re


def generate_report(descpath, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(title)
    report_list = [ Paragraph(paragraph, styles["h1"]) ]
    blank_line = Spacer(1,20)
    report_list.append(blank_line)
    desclist = os.listdir(descpath)
    for desc in desclist:
        trimname = re.search("\w*",desc).group(0)
        with open(descpath + "/" + trimname + ".txt") as f:
            mylist = f.readlines()
            name = mylist[0]
            weight = int(re.search('[0-9]+' ,mylist[1] ).group(0))
            report_list.append(Paragraph(f"name: {name}<br />weichmreght: {weight} lbs\n"))
            report_list.append(blank_line)
    report.build(report_list)

if __name__ == "__main__":
    descpath = "supplier-data/descriptions"
    title = "processed.pdf"
    today = datetime.date.today()
    paragraph = f"Processed Update on {today}"
    generate_report(descpath, title, paragraph)