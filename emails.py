#!/usr/bin/env python3

from email.message import EmailMessage
import os.path
import mimetypes
import smtplib

class emails:
    def generate_email():
        message = EmailMessage()
        message['From'] = automation@example.com
        message['To'] = username@example.com
        message['Subject'] = "Upload Completed - Online Fruit Store"

        message.set_content("All fruits are uploaded to our website successfully. A detailed list is attached to this email.")
        attachment_path = "processed.pdf"
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)

        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=os.path.basename(attachment_path))

        mail_server = smtplib.SMTP('localhost')
        mail_server.send_message(message)
