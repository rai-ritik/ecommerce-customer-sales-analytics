# E-Commerce Customer & Sales Analytics

An end-to-end data analytics portfolio project analyzing transactional e-commerce data to understand sales performance, customer behavior, product performance, geographic revenue, and customer value.

[![Status](https://img.shields.io/badge/status-in%20progress-orange)](https://github.com/rai-ritik/ecommerce-customer-sales-analytics)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-analysis-4479A1?logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Power%20BI](https://img.shields.io/badge/Power%20BI-dashboard-F2C811?logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)

> **Current status:** The repository and raw dataset setup are complete. Data cleaning, SQL analysis, RFM segmentation, dashboard development, and final portfolio documentation are being completed phase by phase.

## Table of contents

- [Project overview](#project-overview)
- [Business questions](#business-questions)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Tools](#tools)
- [Repository structure](#repository-structure)
- [Setup](#setup)
- [Project workflow](#project-workflow)
- [Planned dashboard](#planned-dashboard)
- [Planned deliverables](#planned-deliverables)
- [Limitations](#limitations)
- [Attribution](#attribution)
- [Author](#author)

## Project overview

This project analyzes invoice-level transactions from the **Online Retail** dataset. It is designed as a complete business analytics workflow rather than a collection of isolated queries.

The project follows this pipeline:

```text
Raw transaction workbook
        ↓
Data validation and cleaning
        ↓
Exploratory sales analysis
        ↓
MySQL business queries
        ↓
RFM customer segmentation
        ↓
Power BI dashboard
        ↓
Business insights and recommendations
```

The final analysis will connect technical implementation with business interpretation. Each metric will have a clear definition, each transformation will be documented, and important results will be supported by reproducible queries or dashboard outputs.

## Business questions

The analysis is designed to answer the following questions:

- How does revenue change over time?
- Which countries generate the most revenue?
- Which products contribute the most revenue and units sold?
- Which customers generate the greatest monetary value?
- What is the average order value?
- How many customers make repeat purchases?
- Which customers are champions, loyal, new, at risk, or lost?
- How concentrated is revenue among products, countries, and customers?
- What actions could improve retention and sales performance?

## Dataset

The project uses the [Online Retail dataset from the UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail). The UCI source describes the dataset as transactional data from a UK-based, non-store online retailer covering **December 1, 2010 through December 9, 2011**. [web:28]

### Dataset characteristics

| Property | Description |
|---|---|
| Source | UCI Machine Learning Repository |
| Original file | `Online Retail.xlsx` |
| Local file | `data/raw/online_retail_raw.xlsx` |
| Approximate raw size | 541,000 transaction lines |
| Time period | December 2010 to December 2011 |
| Data grain | One product line within an invoice |
| Main geography | United Kingdom and other countries |

The raw workbook is intentionally excluded from Git because it is a large binary file. Download instructions are available in [`data/README.md`](data/README.md).

### Source columns

| Column | Description |
|---|---|
| `InvoiceNo` | Invoice or transaction identifier. Values beginning with `C` indicate cancellations. |
| `StockCode` | Product identifier. |
| `Description` | Product description. |
| `Quantity` | Number of units in the transaction line. |
| `InvoiceDate` | Date and time of the transaction. |
| `UnitPrice` | Unit price in pounds sterling. |
| `CustomerID` | Customer identifier; some records are missing this value. |
| `Country` | Customer country. |

### Derived columns

The processed dataset will include the following analytical fields:

| Column | Definition |
|---|---|
| `revenue` | `quantity * unit_price` |
| `year` | Calendar year extracted from `invoice_date` |
| `month` | Calendar month extracted from `invoice_date` |
| `year_month` | Year-month period for trend analysis |
| `day_of_week` | Day of week extracted from `invoice_date` |
| `is_cancelled` | Whether the invoice represents a cancellation |
| `is_valid_sale` | Whether the row qualifies for the valid-sales analysis population |

## Methodology

### Data validation and cleaning

The data pipeline will:

1. Load the raw Excel workbook.
2. Standardize column names.
3. Trim and normalize text fields.
4. Convert quantity and unit price to numeric values.
5. Parse invoice dates into a consistent datetime type.
6. Identify cancellation invoices.
7. Detect missing customer IDs and other missing values.
8. Check duplicates and invalid numeric values.
9. Calculate line-level revenue.
10. Add calendar features for time analysis.
11. Save a processed dataset and validation report.

Returns and cancellations will be handled explicitly. They will not be silently removed without being counted and documented. The project will distinguish between transaction-level records, valid positive sales, cancellations, and the final customer-analysis population.

### Sales analysis

The analysis will calculate:

- Total revenue.
- Total orders.
- Units sold.
- Unique customers.
- Unique products.
- Average order value.
- Revenue by year and month.
- Revenue by country.
- Top products by revenue.
- Top products by quantity.
- Revenue concentration by customer.
- Repeat-customer rate.

The primary order definition will be the number of distinct invoices, while revenue will be calculated from line-level quantity multiplied by unit price.

### RFM segmentation

Customer behavior will be summarized using RFM analysis:

- **Recency:** number of days since the most recent purchase.
- **Frequency:** number of distinct invoices.
- **Monetary:** total revenue generated by the customer.

The project will use documented score calculations and reproducible segment rules. Planned segments include:

- Champions.
- Loyal customers.
- New customers.
- Potential loyalists.
- At-risk customers.
- Lost or low-value customers.

RFM segments are analytical groupings for prioritization. They are not confirmed customer personas.

## Tools

| Tool | Purpose |
|---|---|
| Python and pandas | Data inspection, cleaning, validation, and reproducible processing |
| Excel | Exploratory analysis, pivot tables, and workbook-based reporting |
| MySQL | KPI queries, business analysis, CTEs, joins, and window functions |
| Power BI | Data modeling, DAX measures, interactive filtering, and dashboards |
| Git and GitHub | Version control, documentation, and portfolio delivery |

## Repository structure

```text
ecommerce-customer-sales-analytics/
├── README.md
├── .gitignore
├── data/
│   ├── README.md
│   ├── raw/
│   │   ├── .gitkeep
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

The repository will be expanded as the remaining phases are implemented.

## Setup

### Prerequisites

- Python 3.10 or newer.
- Git.
- MySQL and MySQL Workbench, or another compatible MySQL client.
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

For example, after downloading the file to `~/Downloads`:

```bash
mkdir -p data/raw
cp ~/Downloads/"Online Retail.xlsx" data/raw/online_retail_raw.xlsx
```

### Inspect the raw workbook

```bash
python - <<'PY'
import pandas as pd

path = "data/raw/online_retail_raw.xlsx"
df = pd.read_excel(path, engine="openpyxl")

print("Shape:", df.shape)
print("Columns:", list(df.columns))
print("Missing values:")
print(df.isna().sum())
PY
```

## Project workflow

The project is being completed incrementally on the `main` branch.

- [x] Recreate the local repository.
- [x] Create the project directory structure.
- [x] Obtain the raw dataset locally.
- [x] Document the dataset source and expected schema.
- [x] Add Git ignore rules for local and generated files.
- [ ] Inspect and validate the raw workbook.
- [ ] Build the reproducible cleaning pipeline.
- [ ] Generate the data-quality report.
- [ ] Complete exploratory sales analysis.
- [ ] Organize the SQL scripts into numbered analysis modules.
- [ ] Add SQL validation checks.
- [ ] Implement RFM customer segmentation.
- [ ] Complete the Excel workbook.
- [ ] Build the Power BI data model and dashboard.
- [ ] Document DAX measures.
- [ ] Add verified business insights and recommendations.
- [ ] Add screenshots and finalize the portfolio case study.

## Planned dashboard

### Executive overview

The executive page will include:

- Revenue, orders, customers, units sold, and average-order-value KPIs.
- Monthly revenue trend.
- Revenue by country.
- Top products by revenue.
- Date and country filters.

### Customer intelligence

The customer page will include:

- RFM-segment distribution.
- Revenue by segment.
- Top customers.
- Repeat versus one-time customers.
- Retention or cohort analysis.
- Customer-level detail table.

Dashboard screenshots, model documentation, and DAX measures will be added under [`powerbi/`](powerbi/) after implementation.

## Planned deliverables

- Reproducible data-cleaning pipeline.
- Processed analysis dataset.
- Data-quality validation report.
- Data dictionary and methodology documentation.
- MySQL schema and import instructions.
- KPI, product, country, trend, and customer SQL analyses.
- RFM segmentation output.
- Excel analysis workbook.
- Power BI dashboard.
- DAX measure documentation.
- Business insights and recommendations.
- Portfolio case study.

## Limitations

- The dataset contains historical transactions from 2010–2011 rather than current business activity.
- It does not include website sessions, marketing attribution, inventory levels, product cost, profit, or detailed customer demographics.
- Missing customer IDs limit customer-level and RFM analysis for some transactions.
- Treatment of cancellations and returns can change the reported totals, so the chosen rules will be documented.
- Revenue is transaction value, not profit.
- RFM segments are analytical classifications and should be validated before being used for marketing decisions.
- Power BI files may require compatible Microsoft tooling to open and edit.

## Reproducibility principles

- Every transformation must have a documented rule.
- KPI formulas must be explicit.
- Raw and processed row counts must be reconciled.
- Cancellations and returns must be handled transparently.
- Generated datasets and large binary files must not be committed accidentally.
- README claims must be updated only after the corresponding analysis artifact exists.

## Attribution

The underlying dataset is provided by the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail). Please consult the original source for its current license and attribution requirements. [web:28]

The code and documentation in this repository are created for educational and portfolio purposes.

## Author

**Rai Ritik**

- GitHub: [@rai-ritik](https://github.com/rai-ritik)
- Repository: [ecommerce-customer-sales-analytics](https://github.com/rai-ritik/ecommerce-customer-sales-analytics)
