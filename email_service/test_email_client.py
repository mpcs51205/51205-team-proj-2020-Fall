import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

dummy_email = {'to':'mpcs.uchicago.51205@gmail.com','subject':'Holiday Wish from Team 3', 'body':'Happy Thanksgiving !'}

channel.queue_declare(queue='email_queue')
channel.basic_publish(exchange='',
                      routing_key='email_queue',
                      body=json.dumps(dummy_email))
print(" [x] Sent 'dummy email!'")
connection.close()


