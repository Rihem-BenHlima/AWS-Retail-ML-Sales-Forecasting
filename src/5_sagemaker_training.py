"""Train the Prophet model (locally on the Cloud9 instance), package it as a
model artifact and upload it to S3. Top/bottom of the file are reconstructed;
the data-preparation and fit section is taken from the slides."""
import os
import tarfile

import boto3
import joblib
import pandas as pd
from prophet import Prophet

from config import BUCKET, DATASET_FILE

LOCAL_MODEL_DIR = "./model"
MODEL_FILENAME = "prophet_model.joblib"
ARCHIVE = "prophet_model.tar.gz"
S3_KEY = "pipeline/model/prophet_model.tar.gz"  # CHANGE if you want another location in your bucket

print("Running local training...")

file_path = DATASET_FILE
df = pd.read_csv(file_path)
df.columns = df.columns.str.lower().str.strip()
df["y"] = df["quantity"] * df["price_per_unit"]
date_col = "date" if "date" in df.columns else "invoicedate"
df = df.rename(columns={date_col: "ds"})
df["ds"] = pd.to_datetime(df["ds"], errors="coerce")
df = df.dropna(subset=["ds"])
df = df.groupby("ds")["y"].sum().reset_index()

print("Prepared dataset for Prophet:", df.shape)

model = Prophet(yearly_seasonality=True, weekly_seasonality=True)
model.fit(df)

os.makedirs(LOCAL_MODEL_DIR, exist_ok=True)
local_model_path = os.path.join(LOCAL_MODEL_DIR, MODEL_FILENAME)
joblib.dump(model, local_model_path)
print(f"Local model saved at {local_model_path}")

# Package the model as a .tar.gz artifact
with tarfile.open(ARCHIVE, "w:gz") as tar:
    tar.add(local_model_path, arcname=MODEL_FILENAME)
print(f"Packaged model as {ARCHIVE}")

# Upload the artifact to S3
boto3.client("s3").upload_file(ARCHIVE, BUCKET, S3_KEY)
print(f"Uploaded model artifact to S3: s3://{BUCKET}/{S3_KEY}")
