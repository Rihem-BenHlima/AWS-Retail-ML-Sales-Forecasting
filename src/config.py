"""Shared configuration. Values come from environment variables so that no
account-specific data (account ID, role ARN, API keys) is committed."""
import os

REGION = os.environ.get("AWS_REGION", "us-east-1")  # CHANGE if you use another region
BUCKET = os.environ.get("BUCKET", "your-bucket-name")  # CHANGE: your S3 bucket (names are globally unique)
STREAM_NAME = os.environ.get("STREAM_NAME", "your-kinesis-stream")  # CHANGE: your Kinesis stream name
ENDPOINT_NAME = os.environ.get("ENDPOINT_NAME", "your-endpoint-name")  # CHANGE: name for your SageMaker endpoint

# IAM role used by SageMaker, e.g. arn:aws:iam::<account-id>:role/<your-sagemaker-role>
SAGEMAKER_ROLE = os.environ.get("SAGEMAKER_ROLE", "")  # CHANGE: required, no default

DATASET_FILE = "retail_sales_final_dataset.csv"  # CHANGE if your cleaned CSV has another name
