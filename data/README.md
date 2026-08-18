# Dataset

## Source

This project uses the **Online Retail** dataset from the UCI Machine Learning Repository:

https://archive.ics.uci.edu/dataset/352/online+retail

The dataset contains transactions for a UK-based online retailer from December 1, 2010 through December 9, 2011.

## Local file

Place the downloaded workbook at:

```text
data/raw/online_retail_raw.xlsx
```

The raw workbook is excluded from Git because it is a large binary file.

## Dataset grain

Each row represents one product line within an invoice.

## Expected columns

| Column | Description |
|---|---|
| InvoiceNo | Invoice or transaction identifier. Values beginning with `C` represent cancellations |
| StockCode | Product identifier |
| Description | Product description |
| Quantity | Number of units purchased |
| InvoiceDate | Date and time of the transaction |
| UnitPrice | Unit price in pounds sterling |
| CustomerID | Customer identifier |
| Country | Customer’s country |

## Planned cleaning rules

The cleaning pipeline will:

1. Standardize column names.
2. Parse `InvoiceDate`.
3. Convert `Quantity` and `UnitPrice` to numeric values.
4. Identify cancelled invoices.
5. Remove invalid or non-positive sales transactions for the net-sales analysis.
6. Handle missing customer IDs explicitly.
7. Calculate revenue as `Quantity * UnitPrice`.
8. Add calendar fields.
9. Save the processed dataset and a validation report.

## Reproducibility

The raw workbook is not committed to the repository. Recreate it by downloading the file from the UCI source and saving it under `data/raw/online_retail_raw.xlsx`.
