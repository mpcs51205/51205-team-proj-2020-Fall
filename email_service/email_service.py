import time
import smtplib
import os
import pika
import json
from email.message import EmailMessage

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

#server.sendmail(sent_from, to, email_text)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='email_queue')

def callback(ch, method, properties, body):
    email = json.loads(body)
    msg = EmailMessage()
    msg.set_content(email['body'])

    msg['Subject'] = email['subject']
    msg['From'] = sent_from
    msg['To'] = email['to']
    #server.sendmail(sent_from, email['to'], email_text)
    server.send_message(msg)
    print (msg)

channel.basic_consume(queue='email_queue',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
