import json, boto3, base64, os

# Create an S3 client using boto3 (AWS SDK for Python)
s3 = boto3.client('s3')

# Replace this with your actual S3 bucket name (or set the BUCKET env var in Lambda)
BUCKET = os.environ.get("BUCKET", "your-bucket-name")  # CHANGE: your S3 bucket

def lambda_handler(event, context):
    all_records = []
    for record in event['Records']:
        # Decode the Base64-encoded Kinesis data payload
        payload = base64.b64decode(record["kinesis"]["data"]).decode('utf-8')
        all_records.append(payload)

    # Combine all records into a single string (newline separated)
    body = "\n".join(all_records)

    # Upload the combined data as a CSV file to your S3 bucket
    s3.put_object(
        Bucket=BUCKET,
        Key=f"processed/output-{context.aws_request_id}.csv",
        Body=body
    )

    # Return a success message and count of records processed
    return {"statusCode": 200, "records": len(all_records)}
