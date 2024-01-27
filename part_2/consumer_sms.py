import json
from time import sleep
from connect_rabbitMQ import channel
from connect_db import connect
from models import Contact

channel.queue_declare(queue="task_sms", durable=True)

def sent_sms(contact_id):
    contact = Contact.objects.get(id = contact_id)
    contact.sent_sms = True
    contact.save()
    print(f"Sending SMS to {contact.phone}")
    sleep(2)
    
def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    sent_sms(message["id"])
    print(f"Done Task #{method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="task_sms", on_message_callback=callback)

print("Waiting for SMS messages. To exit press CTRL+C")
channel.start_consuming()
# py consumer_sms.py