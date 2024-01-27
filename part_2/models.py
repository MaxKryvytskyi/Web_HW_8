from mongoengine import Document
from mongoengine.fields import StringField, BooleanField

class Contact(Document):
    fullname = StringField(required=True)
    address = StringField()
    email = StringField(required=True)
    phone = StringField(required=True)
    favorites_messages = StringField()
    sent_email = BooleanField(default=False)
    sent_sms = BooleanField(default=False)