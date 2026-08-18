# Data Documentation

## Dataset

This project uses the Online Retail dataset from the UCI Machine Learning Repository:

https://archive.ics.uci.edu/dataset/352/online+retail

The dataset contains invoice-line transactions for a UK-based, non-store online retailer. The observed period is:

- Start: 2010-12-01
- End: 2011-12-09
- Raw rows: 541,909
- Raw columns: 8
- Countries: 38

The raw workbook is stored locally at:

```text
data/raw/online_retail_raw.xlsx
```

The raw file is intentionally ignored by Git because of its size and licensing/redistribution considerations.

## Source columns

| Column | Description | Observed type | Data-quality notes |
|---|---|---|---|
| InvoiceNo | Invoice or transaction identifier. Values beginning with `C` indicate cancellations. | object | Must remain text. |
| StockCode | Product or item identifier. | object | Contains numeric-looking and alphanumeric codes. |
| Description | Product description. | object | 1,454 values are missing. |
| Quantity | Number of units on the invoice line. | int64 | Negative values occur and require return/cancellation handling. |
| InvoiceDate | Invoice date and time. | datetime64 | No missing values observed. |
| UnitPrice | Price per unit in GBP. | float64 | Non-positive and extreme values require validation. |
| CustomerID | Customer identifier. | float64 | 135,080 values are missing. |
| Country | Customer country. | str | 38 distinct countries are present. |

## Initial quality assessment

| Check | Result |
|---|---:|
| Raw rows | 541,909 |
| Exact duplicate rows | 5,268 |
| Missing descriptions | 1,454 |
| Missing customer IDs | 135,080 |
| Distinct invoices | 25,900 |
| Distinct products | 4,070 |
| Distinct countries | 38 |
| Minimum quantity | -80,995 |
| Maximum quantity | 80,995 |
| Minimum unit price | -11,062.06 |
| Maximum unit price | 38,970.00 |

## Analytical data layers

The cleaning process will create separate logical layers:

### Raw data

The original workbook, preserved without modification.

### Clean sales data

Valid purchase lines used for sales, product, country, and time-trend analysis.

### Cancellation and return data

Rows associated with cancellations, returns, reversals, or other negative-value transactions. These will be counted and retained separately rather than silently discarded.

### Customer-analysis data

Clean sales rows with a valid customer identifier. This layer will support customer value analysis, repeat-purchase analysis, and RFM segmentation.

## Cleaning rules

The reproducible cleaning pipeline will:

1. Standardize column names to lowercase snake_case.
2. Convert invoice and product identifiers to strings.
3. Parse invoice dates as datetime values.
4. Convert quantity, unit price, and customer identifiers to numeric values.
5. Create an `is_cancellation` flag from invoice numbers beginning with `C`.
6. Create a `revenue` field using `quantity * unit_price`.
7. Count exact duplicates before removing them.
8. Remove exact duplicates from the clean analytical sales dataset.
9. Replace missing product descriptions with `Unknown product` while preserving a missing-description flag.
10. Exclude rows with invalid or non-positive quantities from completed-sales analysis.
11. Exclude rows with invalid or non-positive unit prices from completed-sales analysis.
12. Exclude missing customer identifiers from customer-level and RFM analysis.
13. Preserve a validation report containing row counts and removal counts for every rule.

No records will be removed without being counted and documented.

## Derived fields

The processed dataset is expected to include:

- `invoice_no`
- `stock_code`
- `description`
- `quantity`
- `invoice_date`
- `unit_price`
- `customer_id`
- `country`
- `revenue`
- `is_cancellation`
- `is_return_or_negative_quantity`
- `invoice_date_only`
- `year`
- `month`
- `month_name`
- `quarter`
- `weekday`
- `weekday_name`

Additional fields may be added when required by the analysis.

## Revenue definition

For completed-sales analysis:

```text
revenue = quantity * unit_price
```

Revenue will be calculated at invoice-line level and aggregated for monthly, country, product, invoice, and customer analysis.

Cancellation and return values will not be mixed into completed-sales KPIs unless the analysis explicitly concerns net sales or return behavior.

## RFM definition

RFM analysis will use customers with valid customer identifiers and valid completed-sales records:

- Recency: days since the customer's most recent purchase.
- Frequency: number of distinct invoices.
- Monetary: total completed-sales revenue.

The analysis date, scoring direction, scoring method, and segment rules will be documented when the RFM pipeline is implemented.

## Limitations

- Missing customer identifiers prevent customer-level analysis for approximately one quarter of raw rows.
- The dataset does not provide product cost, margin, marketing attribution, or payment information.
- Negative quantities and unusual prices require business interpretation.
- Exact duplicates may represent accidental duplication or legitimate repeated lines; the cleaning report will record their treatment.
- The dataset represents one retailer and should not automatically be generalized to all e-commerce businesses.
