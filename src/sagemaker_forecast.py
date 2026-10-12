"""RECONSTRUCTED helper imported by upload_forecast.py (not visible in the slides)."""
import json

import boto3

from config import REGION, ENDPOINT_NAME

runtime = boto3.client("sagemaker-runtime", region_name=REGION)


def get_forecast(dates):
    """Call the SageMaker endpoint with a list of 'YYYY-MM-DD' dates."""
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT_NAME,
        ContentType="application/json",
        Body=json.dumps({"dates": dates}),
    )
    return json.loads(response["Body"].read().decode("utf-8"))
