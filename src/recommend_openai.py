"""Generate AI-powered business recommendations from the forecast (OpenAI).
Set OPENAI_API_KEY in your environment - never hard-code it."""
import json

from openai import OpenAI

client = OpenAI()  # reads OPENAI_API_KEY


def get_recommendations(forecast_path="forecast.json"):
    # 1. Load forecast
    with open(forecast_path) as f:
        forecast = json.load(f)

    # 2. Build the prompt
    forecast_str = json.dumps(forecast, indent=2)
    prompt = f"""
You are an expert retail analyst.
Forecasted sales data:
{forecast_str}

Give actionable business recommendations:
- inventory adjustments
- marketing actions
- staffing guidance
- risk alerts
- expected revenue trends
Be concise and insightful.
"""

    # 3. Call OpenAI LLM
    response = client.responses.create(
        model="gpt-4.1-mini",  # CHANGE: any OpenAI model your key can use
        input=prompt,
    )
    return response.output_text
