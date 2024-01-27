import json
from time import sleep
from connect_rabbitMQ import channel
from connect_db import connect
from models import Contact

channel.queue_declare(queue="task_email", durable=True)

def sent_email(contact_id):
    contact = Contact.objects.get(id = contact_id)
    contact.sent_email = True
    contact.save()
    print(f"Sending email to {contact.email}")
    sleep(2)

def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    sent_email(message["id"])
    print(f"Done Task #{method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="task_email", on_message_callback=callback)

print("Waiting for Email messages. To exit press CTRL+C")
channel.start_consuming()
# py consumer_email.py