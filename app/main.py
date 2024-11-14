from flask import Flask, jsonify, request, abort
from kafka import KafkaProducer
import json


app = Flask(__name__)

producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
@app.route('/api/email', methods=['POST'])
def get_emails():
    data = request.json
    if not data:
        abort(400, description="Missing data")
    producer.send('messages.all', data)
    print(data)
    return jsonify(), 200

if __name__ == '__main__':
    app.run(debug=True)