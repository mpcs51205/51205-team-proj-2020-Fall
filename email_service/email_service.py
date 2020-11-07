import time
import requests
import smtplib
import os

gmail_user = 'mpcs.uchicago.51205@gmail.com'
gmail_password = 'donkeykong51205'

sent_from = 'mpcs.uchicago.51205@gmail.com'
to = 'mpcs.uchicago.51205@gmail.com' # user email
subject = 'test' # email subject
body = "test 51205" #email body
headers = {'User-Agent':'Mozilla/5.0'}

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, to, subject, body)

try:
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.connect('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
except:
    print("gmail server failed")
    quit()


server.sendmail(sent_from, to, email_text)
