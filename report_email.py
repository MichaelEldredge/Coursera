#!/usr/bin/env python3
import emails

message = emails.generate_email("Upload Completed - Online Fruit Store", \
                      "All fruits are uploaded to our website successfully. A detailed list is attached to this email.", \
                      "processed.pdf")
emails.send_email(message)
