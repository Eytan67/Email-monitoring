import json
import psycopg2
from kafka import KafkaConsumer
from explosive_comsumer.database import db_session
from explosive_comsumer.models import create_email_obj, \
    create_location_obj, create_device_info_obj, create_suspicious_explosive_content_obj

consumer = KafkaConsumer(
    'messages.explosive',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='explosive_messages_group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)


for email in consumer:
    email_data = email.value
    print(f"received message: {email_data['email']}")

    try:
        email_obj = create_email_obj(email_data)
        email_id = email_obj.id

        location_obj = create_location_obj(email_data['location'], email_id)

        device_info_obj = create_device_info_obj(email_data['device_info'], email_id)

        sentences_data = ' '.join(email_data['sentences'])
        suspicious_content_obj = create_suspicious_explosive_content_obj(sentences_data, email_id)


        db_session.add(email_obj)
        db_session.add(location_obj)
        db_session.add(device_info_obj)
        db_session.add(suspicious_content_obj)
        db_session.commit()

    except Exception as e:
        db_session.rollback()
        print(f"Error processing message: {e}")
