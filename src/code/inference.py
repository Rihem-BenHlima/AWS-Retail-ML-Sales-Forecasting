"""RECONSTRUCTED inference entry point for the SageMaker PyTorch container.

SageMaker calls these four hooks: model_fn -> input_fn -> predict_fn -> output_fn.
Input:  JSON {"dates": ["2025-09-06", ...]}
Output: JSON list of {"ds": ..., "yhat": ...}
"""
import json
import os

import joblib
import pandas as pd


def model_fn(model_dir):
    return joblib.load(os.path.join(model_dir, "prophet_model.joblib"))


def input_fn(request_body, content_type="application/json"):
    if content_type != "application/json":
        raise ValueError(f"Unsupported content type: {content_type}")
    return pd.DataFrame({"ds": pd.to_datetime(json.loads(request_body)["dates"])})


def predict_fn(input_data, model):
    forecast = model.predict(input_data)
    return forecast[["ds", "yhat"]]


def output_fn(prediction, accept="application/json"):
    prediction["ds"] = prediction["ds"].dt.strftime("%Y-%m-%d")
    return json.dumps(prediction.to_dict(orient="records")), accept
