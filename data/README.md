# Data

This project uses a **public dataset** from Kaggle:

**[Online Sales Dataset](https://www.kaggle.com/datasets/yusufdelikkaya/online-sales-dataset)** - *Online Shopping Patterns and Retail Performance Dataset* (by Yusuf Delikkaya).

The raw data is not redistributed in this repository. Download it from Kaggle and check the dataset page for its license and terms of use.

## Description

The dataset contains anonymized online sales transactions: product purchases, customer details and order characteristics. It can be used to analyze sales trends, customer purchasing behavior and order management in e-commerce or retail, and to study the effect of discounts and payment methods on sales.

The transactions span **2020-01-01 to 2025-09-05** and include 49,782 rows.

## Columns

| Column | Description |
|---|---|
| `InvoiceNo` | Unique identifier of each sales transaction |
| `StockCode` | Product stock-keeping unit (SKU) code |
| `Description` | Short product description (for example, a product category) |
| `Quantity` | Units of the product sold in the transaction |
| `InvoiceDate` | Date and time of the sale |
| `UnitPrice` | Price per unit |
| `CustomerID` | Unique identifier of the customer |
| `Country` | Customer's country |
| `Discount` | Discount applied to the transaction, if any |
| `PaymentMethod` | Payment method used (for example, bank transfer, credit card, PayPal) |

The raw data contains quality issues, such as negative quantities and prices, missing customer IDs and discounts outside the expected range, so it needs cleaning before modeling.

## How it is used in this project

`src/2_clean_dataset.py` keeps four columns and renames them:

| Raw column | Cleaned column |
|---|---|
| `InvoiceDate` | `date` |
| `Description` | `product_category` |
| `Quantity` | `quantity` |
| `UnitPrice` | `price_per_unit` |

After cleaning, 47,293 of the 49,782 rows remain. The forecast target is daily sales: `quantity x price_per_unit`, summed per date.

## Files in this folder

`online_sales_dataset-selected-columns.csv` is a column template with the raw header only; it holds no data. Put the downloaded Kaggle CSV here (or point the scripts to it) before running the pipeline.
