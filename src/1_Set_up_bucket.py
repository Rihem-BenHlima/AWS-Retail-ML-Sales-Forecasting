from datetime import datetime

from config import REGION, BUCKET, SAGEMAKER_ROLE

# AWS region and role
region = REGION
role = SAGEMAKER_ROLE  # export SAGEMAKER_ROLE=arn:aws:iam::<account-id>:role/<your-sagemaker-role>

# Your existing bucket
bucket = BUCKET

# Generate run ID based on current timestamp
run_id = datetime.now().strftime("%Y%m%d-%H%M%S")
print("Run ID:", run_id)

# S3 paths used by the pipeline
processing_input = f"s3://{bucket}/processed/"
processing_output = f"s3://{bucket}/pipeline/input/"
training_output = f"s3://{bucket}/models/{run_id}/"

print("Processing input path:", processing_input)
print("Processing output path:", processing_output)
print("Training output path:", training_output)
