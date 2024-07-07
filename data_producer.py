from kafka import KafkaProducer
import json
import time
import random

def generate_data():
    return {
        'timestamp': time.time(),
        'value': random.randint(1, 100)
    }

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    data = generate_data()
    producer.send('real-time-data', value=data)
    print(f"Sent data: {data}")
    time.sleep(1)
