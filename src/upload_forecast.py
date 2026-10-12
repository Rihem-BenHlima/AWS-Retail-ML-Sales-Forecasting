import json
import boto3
from datetime import datetime, timedelta
from sagemaker_forecast import get_forecast

from config import BUCKET

# 1. Generate the next 30 days (CHANGE the range to forecast a different horizon)
dates = [(datetime.today() + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(30)]

# 2. Call SageMaker endpoint
forecast = get_forecast(dates)

# 3. Save forecast locally
with open("forecast.json", "w") as f:
    json.dump(forecast, f, indent=2)

# 4. Upload forecast.json to S3
s3_key = "dashboard/forecast.json"  # CHANGE if you want another S3 path

s3 = boto3.client("s3")
s3.upload_file("forecast.json", BUCKET, s3_key)
print(f"Forecast uploaded to s3://{BUCKET}/{s3_key}")
