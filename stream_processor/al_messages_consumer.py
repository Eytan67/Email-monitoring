import json
from kafka import KafkaConsumer

from producer import route_email
from mongodb_connection import get_mongo_connection


consumer = KafkaConsumer(
    'messages.all',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='all_messages_group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for email in consumer:
    email = email.value
    route_email(email)
    collection = get_mongo_connection()
    collection.insert_one(email)

