"""RECONSTRUCTED: build the HTML dashboard (Chart.js) from forecast.json and the
OpenAI recommendations. Output: forecast_visualization.html"""
import html
import json

from recommend_openai import get_recommendations

with open("forecast.json") as f:
    forecast = json.load(f)

labels = [p["ds"] for p in forecast]
values = [round(p["yhat"], 2) for p in forecast]
recommendations = html.escape(get_recommendations("forecast.json"))

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>SageMaker Sales Forecast with AI Recommendations</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<style>
  body {{ font-family: Arial, sans-serif; background: linear-gradient(135deg,#667eea,#764ba2); margin:0; padding:24px; }}
  .card {{ max-width: 900px; margin: auto; background:#fff; border-radius:16px; padding:24px; }}
  h1 {{ color:#667eea; text-align:center; font-size:1.4rem; }}
  pre {{ white-space: pre-wrap; background:#f5f7fa; padding:16px; border-radius:8px; }}
</style>
</head>
<body>
<div class="card">
  <h1>SageMaker Sales Forecast with AI Recommendations</h1>
  <canvas id="chart"></canvas>
  <h2>AI-Powered Recommendations</h2>
  <pre>{recommendations}</pre>
</div>
<script>
new Chart(document.getElementById('chart'), {{
  type: 'line',
  data: {{
    labels: {json.dumps(labels)},
    datasets: [{{ label: 'Forecasted Sales ($)', data: {json.dumps(values)},
                 borderColor: '#667eea', backgroundColor: 'rgba(102,126,234,0.1)',
                 fill: true, tension: 0.4 }}]
  }}
}});
</script>
</body>
</html>"""

with open("forecast_visualization.html", "w", encoding="utf-8") as f:
    f.write(page)
print("Dashboard written to forecast_visualization.html")
