#!/usr/bin/env python3

from email.message import EmailMessage
import os.path
import mimetypes
import smtplib

def generate_email(subject_line,body, attachment_path=False):
    message = EmailMessage()
    message['From'] = "automation@example.com"
    message['To'] = "student-03-95c0c5d6b715@example.com"
    #message['Subject'] = "Upload Completed - Online Fruit Store"
    message['Subject'] = subject_line

    #message.set_content("All fruits are uploaded to our website successfully. A detailed list is attached to this email.")
    message.set_content(body)
    if attachment_path:
        # attachment_path = "processed.pdf"
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_type, filename=os.path.basename(attachment_path))


    return message
def send_email(package):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(package)
    mail_server.quit()
