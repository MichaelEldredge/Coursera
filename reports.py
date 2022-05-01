#!/usr/bin/env python3

import os
import datetime
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
import re


def generate_report():
    descpath = "supplier-data/descriptions"
    today = datetime.date.today()
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate("report.pdf")
    report_list = [ Paragraph(f"Processed Update on {today}", styles["h1"]) ]
    blank_line = Paragraph("<br />")
    report_list.append(blank_line)
    desclist = os.listdir(descpath)
    for desc in desclist:
        trimname = re.search("\w*",desc).group(0)
        with open(descpath + "/" + trimname + ".txt") as f:
            mylist = f.readlines()
            name = mylist[0]
            weight = int(re.search('[0-9]+' ,mylist[1] ).group(0))
            report_list.append(Paragraph(f"name: {name}<br />weight: {weight} lbs"))
            report_list.append(blank_line)
    report.build(report_list)

if __name__ == "__main__":
    print()
    generate_report()