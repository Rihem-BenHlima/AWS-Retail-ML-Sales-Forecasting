"""RECONSTRUCTED: deploy the packaged Prophet model to a real-time SageMaker
endpoint using the PyTorch container (the SKLearn container failed on the
pystan dependency and limited custom inference scripts).

Framework / Python versions and instance type are assumptions - adjust them
to what you used."""
from sagemaker.pytorch import PyTorchModel

from config import BUCKET, ENDPOINT_NAME, SAGEMAKER_ROLE

# CHANGE: must match the S3 key used in 5_sagemaker_training.py
model_data = f"s3://{BUCKET}/pipeline/model/prophet_model.tar.gz"

model = PyTorchModel(
    model_data=model_data,
    role=SAGEMAKER_ROLE,
    entry_point="inference.py",
    source_dir="code",  # contains inference.py + requirements.txt
    framework_version="2.1",  # CHANGE: a PyTorch version supported in your region
    py_version="py310",
)

predictor = model.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.large",  # CHANGE: pick a size/cost that fits your account
    endpoint_name=ENDPOINT_NAME,
)
print("Endpoint deployed:", ENDPOINT_NAME)
