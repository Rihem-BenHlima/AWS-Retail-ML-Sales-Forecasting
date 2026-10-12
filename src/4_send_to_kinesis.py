import boto3
import json
import csv

from config import REGION, STREAM_NAME, DATASET_FILE

# Create a Kinesis connection
kinesis = boto3.client("kinesis", region_name=REGION)

# Open your cleaned dataset
with open(DATASET_FILE, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Convert each row to JSON
        data = json.dumps(row)

        # Send the record to Kinesis
        response = kinesis.put_record(
            StreamName=STREAM_NAME,
            Data=data.encode("utf-8"),
            PartitionKey="partitionkey1"
        )
        print(f"Record sent: {response['SequenceNumber']}")

print("All records sent to Kinesis stream")
