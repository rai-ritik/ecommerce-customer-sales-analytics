# E-Commerce Customer & Sales Analytics

An end-to-end portfolio project for analyzing transactional e-commerce sales, customer behavior, product performance, geographic revenue, and customer value using Excel, MySQL, and Power BI.

> **Project status:** In progress — dataset setup is complete; cleaning, SQL analysis, RFM segmentation, and dashboard deliverables are being completed incrementally.

## Overview

This project analyzes the **Online Retail** transactional dataset from a UK-based, non-store online retailer. The analysis is designed to answer practical business questions:

- How much revenue is generated over time?
- Which countries and products contribute the most revenue?
- Which customers drive the greatest commercial value?
- How frequently do customers return?
- Which customers are champions, loyal, at-risk, or lost?
- What actions could improve retention, revenue, and product performance?

The project follows a reproducible analytics workflow:

```text
Raw workbook → Data validation and cleaning → SQL analysis → RFM segmentation → Dashboard → Business recommendations
```

## Project goals

The project aims to demonstrate practical skills in:

- Transactional data cleaning and quality validation.
- Exploratory sales and customer analysis.
- MySQL aggregation, joins, CTEs, and window functions.
- RFM customer segmentation.
- KPI design and business metric definition.
- Power BI data modeling, DAX, and dashboard design.
- Communicating analytical results to a non-technical audience.

## Dataset

The project uses the [Online Retail dataset from the UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail). The source describes transactions occurring between **December 1, 2010 and December 9, 2011** for a UK-based online retailer. [web:28]

The dataset is line-item transactional data. Each row represents one product line within an invoice.

### Expected raw data

| Property | Description |
|---|---|
| Source | UCI Machine Learning Repository |
| File | `Online Retail.xlsx` |
| Local path | `data/raw/online_retail_raw.xlsx` |
| Approximate raw rows | 541,000 |
| Time period | December 2010 to December 2011 |
| Geographic scope | Multiple countries, primarily the United Kingdom |
| Data grain | Invoice-product line |

The raw workbook is intentionally excluded from Git because it is a large binary file. See [`data/README.md`](data/README.md) for download and reproducibility instructions.

### Source columns

| Column | Description |
|---|---|
| `InvoiceNo` | Invoice or transaction identifier. Invoice numbers beginning with `C` indicate cancellations. |
| `StockCode` | Product identifier. |
| `Description` | Product description. |
| `Quantity` | Number of units in the transaction line. |
| `InvoiceDate` | Transaction date and time. |
| `UnitPrice` | Unit price in pounds sterling. |
| `CustomerID` | Customer identifier; some records are missing this value. |
| `Country` | Customer country. |

## Analytical methodology

### Data cleaning

The cleaning pipeline will document and validate the following operations:

1. Standardize column names and text fields.
2. Convert quantity and unit price to numeric values.
3. Parse invoice dates into a consistent datetime type.
4. Identify cancelled invoices using the invoice identifier.
5. Separate valid sales from returns and cancellations.
6. Handle missing customer IDs explicitly.
7. Calculate line revenue:

   `Revenue = Quantity × UnitPrice`

8. Add year, month, year-month, and day-of-week fields.
9. Produce row-count, null, duplicate, and value-range validation results.
10. Save the processed dataset outside Git and document the transformation results.

Returns and cancellations will not be silently discarded. The final methodology will distinguish between gross sales, returns, and the net-sales analysis population.

### Sales analysis

The project will calculate and visualize:

- Total revenue.
- Total orders.
- Units sold.
- Unique customers.
- Unique products.
- Average order value.
- Revenue by month and year.
- Revenue by country.
- Top products by revenue and quantity.
- Customer revenue concentration.
- Repeat-customer rate.

### RFM segmentation

Customers will be analyzed using RFM features:

- **Recency:** days since the customer’s most recent purchase.
- **Frequency:** number of distinct invoices.
- **Monetary:** total customer revenue.

Customers will be assigned interpretable segments such as:

- Champions.
- Loyal customers.
- New customers.
- At-risk customers.
- Lost or low-value customers.

The analysis date, scoring method, and segment thresholds will be documented so that the results are reproducible.

## Repository structure

```text
ecommerce-customer-sales-analytics/
├── README.md
├── .gitignore
├── data/
│   ├── README.md
│   ├── raw/
│   │   └── online_retail_raw.xlsx   # local only; ignored by Git
│   └── processed/                    # generated outputs; ignored by Git
├── sql/
│   └── analysis.sql
├── excel/
│   └── screenshots/
├── powerbi/
│   └── screenshots/
├── docs/
└── assets/
    └── images/
```

The repository structure will expand as each project phase is completed.

## Technology stack

| Tool | Purpose |
|---|---|
| Python and pandas | Data inspection, cleaning, validation, and reproducible processing |
| Excel | Initial data exploration, pivot analysis, and workbook-based reporting |
| MySQL | KPI queries, business analysis, and customer segmentation |
| Power BI | Interactive dashboarding, data modeling, and DAX measures |
| Git and GitHub | Version control, documentation, and portfolio presentation |

## Setup

### Prerequisites

- macOS, Linux, or Windows.
- Python 3.10 or newer.
- Git.
- MySQL Workbench or another MySQL client for SQL analysis.
- Power BI Desktop or Power BI Service for the dashboard phase.

### Clone the repository

```bash
git clone https://github.com/rai-ritik/ecommerce-customer-sales-analytics.git
cd ecommerce-customer-sales-analytics
```

### Create the Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pandas openpyxl
```

### Obtain the dataset

Download the Online Retail workbook from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail), then save it as:

```text
data/raw/online_retail_raw.xlsx
```

The raw workbook is ignored by Git and must be downloaded locally for analysis.

## Current workflow

The project is being completed in the following phases:

- [x] Recreate the local repository from GitHub.
- [x] Create the `project-completion` working branch.
- [x] Download and place the raw dataset locally.
- [x] Add dataset-source documentation and Git ignore rules.
- [ ] Inspect and validate the raw workbook.
- [ ] Build the reproducible cleaning pipeline.
- [ ] Add data-quality validation outputs.
- [ ] Complete exploratory sales analysis.
- [ ] Organize and validate the SQL analysis scripts.
- [ ] Implement RFM customer segmentation.
- [ ] Complete the Excel analysis workbook.
- [ ] Build and document the Power BI dashboard.
- [ ] Write verified business insights and recommendations.
- [ ] Add screenshots and finalize the portfolio case study.

## Planned dashboard

The Power BI dashboard will contain at least two analytical pages.

### Executive overview

- Revenue, order, customer, and average-order-value KPIs.
- Monthly revenue trend.
- Revenue by country.
- Top products.
- Date and country filters.

### Customer intelligence

- Customer segment distribution.
- Revenue by RFM segment.
- Top customers.
- Repeat versus one-time customers.
- Customer retention or cohort analysis.
- Customer-level detail table.

Dashboard screenshots and DAX documentation will be added under [`powerbi/`](powerbi/) once the dashboard is complete.

## Planned outputs

- Cleaned analysis dataset.
- Data-quality validation report.
- SQL KPI and business-analysis queries.
- RFM customer-segmentation output.
- Excel analysis workbook.
- Power BI dashboard.
- DAX measure documentation.
- Business insights and recommendations.
- Portfolio case-study documentation.

## Limitations

- This is historical transaction data from 2010–2011, not a current business dataset.
- The data represents purchases and invoice lines; it does not include website sessions, marketing attribution, product cost, inventory, or customer demographics beyond country.
- Missing customer IDs limit customer-level analysis for some transactions.
- Revenue analysis depends on the documented treatment of cancellations, returns, and invalid prices.
- RFM segments are analytical groupings, not confirmed customer personas.
- Power BI files may require compatible Microsoft tooling to open and edit.

## Reproducibility principles

To keep the project trustworthy:

- Every transformation will have a documented rule.
- KPI definitions will be explicit.
- Raw and processed row counts will be reconciled.
- Cancellations and returns will be handled transparently.
- Generated datasets and large binary files will not be committed accidentally.
- README claims will be updated only after the corresponding artifact exists.

## License and attribution

The analysis code and documentation in this repository are provided for educational and portfolio purposes. The underlying dataset belongs to its original provider and is used according to the terms stated by the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail).

## Author

**Rai Ritik**

- GitHub: [@rai-ritik](https://github.com/rai-ritik)
- Repository: [ecommerce-customer-sales-analytics](https://github.com/rai-ritik/ecommerce-customer-sales-analytics)
