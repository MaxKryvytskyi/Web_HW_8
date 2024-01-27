from faker import Faker
from datetime import datetime 
from connect_db import connect
from connect_rabbitMQ import channel, connection
from models import Contact
from random import choice
import json
import pika

fake = Faker()

favorites_messages = ["Email", "SMS"]

channel.exchange_declare(exchange="task_contact", exchange_type="direct")
channel.queue_declare(queue="task_email", durable=True)
channel.queue_declare(queue="task_sms", durable=True)
channel.queue_bind(exchange="task_contact", queue="task_email")
channel.queue_bind(exchange="task_contact", queue="task_sms")

def create_contacts(num):
    contacts = []
    for _ in range(num):
        contact = Contact(
            fullname = fake.name(),
            address = fake.company(), 
            email = fake.email(),
            phone = fake.msisdn(),
            favorites_messages = choice(favorites_messages),
            sent_email = False,
            sent_sms = False)
        contact.save()
        contacts.append(contact)
    return contacts

def queue_messages_email(contact):
    message = {
            "id": f"{contact.id}",
            "Task": "Email",
            "date": datetime.now().isoformat()
        }
    channel.basic_publish(
            exchange="task_contact",
            routing_key="task_email",
            body=json.dumps(message).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))

    print(" [x] Sent %r" % message)

def queue_messages_sms(contact):
    message = {
            "id": f"{contact.id}",
            "Task": "SMS",
            "date": datetime.now().isoformat()
        }
    channel.basic_publish(
            exchange="task_contact",
            routing_key="task_sms",
            body=json.dumps(message).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
    print(" [x] Sent %r" % message)

def main():
    contacts = create_contacts(20)

    for contact in contacts:
        if contact.favorites_messages == "email" and contact.email:
            queue_messages_email(contact)
            
        elif contact.favorites_messages == "sms" and contact.phone:
            queue_messages_sms(contact)
    connection.close()
    
if __name__ == "__main__":
    main()
    # py producer.py