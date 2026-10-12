"""RECONSTRUCTED from the project slides (only the console output was visible).

Cleans the raw Kaggle "Online Sales Dataset" locally and keeps only the
columns needed for forecasting: date, product_category, quantity, price_per_unit.
Adjust RENAME to match the column names of the CSV you downloaded.
"""
import sys

import pandas as pd

RAW_FILE = sys.argv[1] if len(sys.argv) > 1 else "retail_sales_dataset.csv"
OUT_FILE = "retail_sales_final_dataset.csv"

# raw column name (lower-cased) -> standardized name
RENAME = {
    "invoicedate": "date",
    "date": "date",
    "description": "product_category",
    "product category": "product_category",
    "quantity": "quantity",
    "units sold": "quantity",
    "unitprice": "price_per_unit",
    "unit price": "price_per_unit",
    "price per unit": "price_per_unit",
}
KEEP = ["date", "product_category", "quantity", "price_per_unit"]

df = pd.read_csv(RAW_FILE)
rows_before = len(df)

# Standardize column names
df.columns = df.columns.str.strip().str.lower()
df = df.rename(columns=RENAME)

# Remove irrelevant / redundant columns
df = df[KEEP]

# Clean values
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna()
df = df[(df["quantity"] > 0) & (df["price_per_unit"] > 0)]

df.to_csv(OUT_FILE, index=False)
print(f"Cleaned dataset saved as {OUT_FILE}")
print(f"Rows before: {rows_before}, after cleaning: {len(df)}")
print(f"Columns kept: {list(df.columns)}")
