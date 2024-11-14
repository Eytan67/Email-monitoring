import json
from kafka import KafkaProducer


producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

def detect(sentences):
    for sentence in sentences:
        if 'explos' in sentence:
            return 'explos'
        elif 'hostage' in sentence:
            return 'hosta'

def route_message(email):
    diagnosis = detect(email.get('sentences'))
    if diagnosis == 'explos':
        print('is_explos')
        producer.send('messages.explosive', email)
    elif diagnosis == 'hosta':
        print('is_host')
        producer.send('messages.hostage', email)
    else:
        print('is_none')
