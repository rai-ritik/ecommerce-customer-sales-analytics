# Power BI Data Model

## Overview

This document describes the data model for the E-Commerce Customer & Sales Analytics Power BI dashboard. The model uses two main tables: `clean_sales` for transaction data and `rfm_customers` for customer segmentation.

## Data sources

### Primary tables

| Table | Source file | Rows | Key columns |
|-------|-------------|------|-------------|
| clean_sales | `data/processed/clean_sales.csv` | 524,878 | invoice_no, stock_code, customer_id, country, invoice_date, revenue |
| rfm_customers | `docs/rfm_customers.csv` | 4,338 | customer_id, segment, rfm_code, monetary |
| Date | (Calculated) | 374 | Date, Year, Month, MonthName |

### Data refresh

To refresh data:

1. Regenerate CSV files from Python:
   ```bash
   python python/clean_data.py
   python python/rfm_segmentation.py
   ```

2. In Power BI: Home → Refresh

## Table schemas

### clean_sales

| Column | Data type | Description |
|--------|-----------|-------------|
| invoice_no | Text | Invoice identifier |
| stock_code | Text | Product code |
| description | Text | Product description |
| quantity | Whole Number | Units sold |
| invoice_date | DateTime | Transaction date and time |
| unit_price | Decimal | Price per unit |
| customer_id | Text | Customer identifier (blank for some rows) |
| country | Text | Customer country |
| revenue | Decimal | quantity × unit_price |
| year | Whole Number | Calendar year |
| month | Whole Number | Calendar month (1-12) |
| day | Whole Number | Calendar day (1-31) |
| hour | Whole Number | Hour of day (0-23) |
| is_cancellation | True/False | Cancellation flag |
| is_return | True/False | Return flag |

### rfm_customers

| Column | Data type | Description |
|--------|-----------|-------------|
| customer_id | Text | Customer identifier (Primary Key) |
| recency | Whole Number | Days since last purchase |
| frequency | Whole Number | Number of distinct invoices |
| monetary | Decimal | Total revenue |
| r_score | Whole Number | Recency quintile (1-5) |
| f_score | Whole Number | Frequency quintile (1-5) |
| m_score | Whole Number | Monetary quintile (1-5) |
| rfm_score | Whole Number | Sum of r_score + f_score + m_score |
| rfm_code | Text | Three-character code (e.g., "555") |
| segment | Text | Segment label (e.g., "Champions") |

### Date (calculated table)

| Column | Data type | Description |
|--------|-----------|-------------|
| Date | Date | Unique date |
| Year | Whole Number | Calendar year |
| Month | Whole Number | Month number (1-12) |
| MonthName | Text | "MMM YYYY" format |
| YearMonth | Text | "YYYY-MM" format |
| Day | Whole Number | Day of month (1-31) |
| DayOfWeek | Whole Number | 1 (Monday) to 7 (Sunday) |
| DayName | Text | Full day name |

## Relationships

### Diagram

Date[Date] ──< clean_sales[invoice_date]
(Many-to-One, Single direction)

clean_sales[customer_id] ──> rfm_customers[customer_id]
(Many-to-One, Single direction)

### Relationship details

| From table | From column | To table | To column | Cardinality | Cross filter |
|------------|-------------|----------|-----------|-------------|--------------|
| clean_sales | invoice_date | Date | Date | Many-to-One | Single |
| clean_sales | customer_id | rfm_customers | customer_id | Many-to-One | Single |

### Relationship notes

- **Date relationship:** Filters flow from Date to clean_sales for time-based analysis.
- **Customer relationship:** Filters flow from rfm_customers to clean_sales for segment analysis.
- **Inactive relationships:** None required for this model.

## Import steps

### Step 1: Import clean_sales

1. Home → Get Data → Text/CSV
2. Select `data/processed/clean_sales.csv`
3. Click "Transform Data"
4. Verify data types:
   - invoice_no: Text
   - stock_code: Text
   - description: Text
   - quantity: Whole Number
   - invoice_date: DateTime
   - unit_price: Decimal
   - customer_id: Text
   - country: Text
   - revenue: Decimal
   - year, month, day, hour: Whole Number
   - is_cancellation, is_return: True/False
5. Click "Close & Apply"

### Step 2: Import rfm_customers

1. Home → Get Data → Text/CSV
2. Select `docs/rfm_customers.csv`
3. Click "Transform Data"
4. Verify data types:
   - customer_id: Text
   - recency, frequency: Whole Number
   - monetary: Decimal
   - r_score, f_score, m_score, rfm_score: Whole Number
   - rfm_code: Text
   - segment: Text
5. Click "Close & Apply"

### Step 3: Create Date table

1. Modeling → New Table
2. Enter the DAX formula from `dax_measures.md`
3. Mark as date table: Table tools → Mark as date table → Select Date column

### Step 4: Create relationships

1. Model view
2. Drag Date[Date] to clean_sales[invoice_date]
3. Drag rfm_customers[customer_id] to clean_sales[customer_id]
4. Set cardinality to Many-to-One
5. Set cross filter direction to Single

## Dashboard pages

### Page 1: Executive Overview

**Purpose:** High-level business KPIs and trends

**Visuals:**
- Revenue KPI card
- Orders KPI card
- Customers KPI card
- AOV KPI card
- Monthly revenue line chart
- Revenue by country bar chart (top 10)
- Top products bar chart (top 20)
- Slicers: Date range, Country

**Key measures:**
- `[Revenue]`
- `[Total Orders]`
- `[Total Customers]`
- `[Average Order Value]`
- `[Revenue by Month]`
- `[Revenue by Country]`

### Page 2: Customer Intelligence

**Purpose:** Customer behavior and RFM segmentation

**Visuals:**
- RFM segment distribution (pie or donut chart)
- Revenue by RFM segment (bar chart)
- Top customers table (top 20 by revenue)
- Repeat vs one-time customers (pie chart)
- Customer detail table (customer_id, orders, revenue, segment)
- Retention/cohort analysis (matrix or table)

**Key measures:**
- `[RFM Customer Count]`
- `[RFM Revenue]`
- `[Revenue by Segment]`
- `[Repeat Customers]`
- `[One-Time Customers]`
- `[Repeat Customer Rate %]`

## Slicers

### Recommended slicers

| Page | Slicer | Field | Type |
|------|--------|-------|------|
| Executive | Date Range | Date[Date] | Between |
| Executive | Country | clean_sales[country] | Dropdown |
| Customer | Segment | rfm_customers[segment] | Dropdown |
| Customer | Date Range | Date[Date] | Between |

### Slicer formatting

- Show "Select all" option
- Single select: Off (except where noted)
- Search enabled: On

## Performance optimization

### Best practices

1. **Use import mode** (not DirectQuery) for better performance.
2. **Remove unused columns** in Power Query to reduce model size.
3. **Disable auto date/time** in File → Options → Current File → Data Load.
4. **Use measures** instead of calculated columns where possible.
5. **Limit visuals per page** to 10-15 for optimal rendering.

### Expected model size

- clean_sales: ~50-80 MB (compressed)
- rfm_customers: <1 MB
- Date: <1 MB
- **Total:** ~50-80 MB

## Version

- **Created:** 2026-08-18
- **Based on commit:** 7530f9d (feat: add organized SQL analysis pipeline)
- **Power BI Desktop:** Recommended version 2024 or later
