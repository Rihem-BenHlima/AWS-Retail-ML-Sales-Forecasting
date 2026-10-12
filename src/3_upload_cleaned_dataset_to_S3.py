import boto3

from config import BUCKET, DATASET_FILE

s3 = boto3.client("s3")

bucket = BUCKET
file_name = DATASET_FILE

# Upload the file to S3
s3.upload_file(file_name, bucket, f"processed/{file_name}")

print("File uploaded to S3 successfully!")
