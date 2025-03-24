import boto3
import json
import time
import random
from datetime import datetime, timedelta

# Firehose stream name and region
FIREHOSE_STREAM_NAME = 'your-firehose-name'
REGION = 'us-east-1'  # Change as needed

# Initialize Firehose client
firehose = boto3.client('firehose', region_name=REGION)

def generate_trip_event():
    now = datetime.utcnow()
    pickup_time = now - timedelta(minutes=random.randint(1, 15))
    dropoff_time = pickup_time + timedelta(minutes=random.randint(5, 20))
    
    trip = {
        "trip_id": f"cab_{random.randint(100000, 999999)}",
        "pickup_time": pickup_time.strftime("%Y-%m-%d %H:%M:%S"),
        "dropoff_time": dropoff_time.strftime("%Y-%m-%d %H:%M:%S"),
        "PULocationID": random.randint(1, 265),
        "DOLocationID": random.randint(1, 265),
        "passenger_count": random.randint(1, 4),
        "fare_amount": round(random.uniform(5.0, 75.0), 2),
        "payment_type": random.choice([1, 2])  # 1 = Card, 2 = Cash
    }
    return trip

def send_to_firehose(record):
    response = firehose.put_record(
        DeliveryStreamName=FIREHOSE_STREAM_NAME,
        Record={'Data': json.dumps(record) + "\n"}
    )
    print(f"[{datetime.utcnow()}] Sent trip_id={record['trip_id']} status={response['ResponseMetadata']['HTTPStatusCode']}")

if __name__ == "__main__":
    print("🚖 Streaming NYC Taxi trips to Firehose...")

    while True:
        trip = generate_trip_event()
        send_to_firehose(trip)
        time.sleep(1)  # Simulate 1 record per second
