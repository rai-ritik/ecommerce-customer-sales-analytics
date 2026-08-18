# Power BI DAX Measures

## Overview

This document defines the DAX measures for the E-Commerce Customer & Sales Analytics Power BI dashboard. All measures are designed to work with the data model described in `data_model.md`.

## Date table

Create a date table for time-based analysis:

```dax
Date = 
ADDCOLUMNS (
    CALENDAR ( DATE ( 2010, 12, 1 ), DATE ( 2011, 12, 9 ) ),
    "Year", YEAR ( [Date] ),
    "Month", MONTH ( [Date] ),
    "MonthName", FORMAT ( [Date], "MMM YYYY" ),
    "YearMonth", FORMAT ( [Date], "YYYY-MM" ),
    "Day", DAY ( [Date] ),
    "DayOfWeek", WEEKDAY ( [Date], 2 ),
    "DayName", FORMAT ( [Date], "dddd" )
)
```

## Core KPI measures

### Total Revenue

```dax
Total Revenue = 
SUM ( clean_sales[revenue] )
```

### Revenue (Positive Only)

```dax
Revenue = 
CALCULATE (
    SUM ( clean_sales[revenue] ),
    clean_sales[revenue] > 0
)
```

### Total Orders

```dax
Total Orders = 
CALCULATE (
    DISTINCTCOUNT ( clean_sales[invoice_no] ),
    clean_sales[revenue] > 0
)
```

### Total Units Sold

```dax
Total Units Sold = 
CALCULATE (
    SUM ( clean_sales[quantity] ),
    clean_sales[revenue] > 0
)
```

### Total Products

```dax
Total Products = 
CALCULATE (
    DISTINCTCOUNT ( clean_sales[stock_code] ),
    clean_sales[revenue] > 0
)
```

### Total Countries

```dax
Total Countries = 
CALCULATE (
    DISTINCTCOUNT ( clean_sales[country] ),
    clean_sales[revenue] > 0
)
```

### Total Customers

```dax
Total Customers = 
CALCULATE (
    DISTINCTCOUNT ( clean_sales[customer_id] ),
    clean_sales[revenue] > 0,
    NOT ISBLANK ( clean_sales[customer_id] )
)
```

### Average Order Value (AOV)

```dax
Average Order Value = 
DIVIDE (
    [Revenue],
    [Total Orders],
    0
)
```

### Average Order Lines

```dax
Average Order Lines = 
DIVIDE (
    CALCULATE (
        COUNTROWS ( clean_sales ),
        clean_sales[revenue] > 0
    ),
    [Total Orders],
    0
)
```

## Time-based measures

### Revenue by Month

```dax
Revenue by Month = 
CALCULATE (
    [Revenue],
    USERELATIONSHIP ( 'Date'[Date], clean_sales[invoice_date] )
)
```

### Month-over-Month Growth

```dax
Revenue MoM Growth % = 
VAR CurrentMonth = [Revenue]
VAR PreviousMonth = 
    CALCULATE (
        [Revenue],
        PREVIOUSMONTH ( 'Date'[Date] )
    )
RETURN
    DIVIDE (
        CurrentMonth - PreviousMonth,
        PreviousMonth,
        0
    )
```

### Year-to-Date Revenue

```dax
Revenue YTD = 
TOTALYTD (
    [Revenue],
    'Date'[Date]
)
```

## Country measures

### Revenue by Country

```dax
Revenue by Country = 
[Revenue]
```

### Country Revenue Share

```dax
Country Revenue Share % = 
DIVIDE (
    [Revenue],
    CALCULATE ( [Revenue], ALL ( clean_sales[country] ) ),
    0
)
```

### Top 10 Countries Revenue

```dax
Top 10 Countries Revenue = 
CALCULATE (
    [Revenue],
    TOPN (
        10,
        VALUES ( clean_sales[country] ),
        [Revenue],
        DESC
    )
)
```

## Product measures

### Revenue by Product

```dax
Revenue by Product = 
[Revenue]
```

### Product Revenue Share

```dax
Product Revenue Share % = 
DIVIDE (
    [Revenue],
    CALCULATE ( [Revenue], ALL ( clean_sales[stock_code] ) ),
    0
)
```

### Top 20 Products Revenue

```dax
Top 20 Products Revenue = 
CALCULATE (
    [Revenue],
    TOPN (
        20,
        VALUES ( clean_sales[stock_code] ),
        [Revenue],
        DESC
    )
)
```

### Units Sold per Product

```dax
Units Sold = 
CALCULATE (
    SUM ( clean_sales[quantity] ),
    clean_sales[revenue] > 0
)
```

## Customer measures

### Revenue by Customer

```dax
Revenue by Customer = 
[Revenue]
```

### Orders per Customer

```dax
Orders per Customer = 
DIVIDE (
    [Total Orders],
    [Total Customers],
    0
)
```

### Repeat Customers

```dax
Repeat Customers = 
CALCULATE (
    COUNTROWS (
        FILTER (
            VALUES ( clean_sales[customer_id] ),
            CALCULATE (
                DISTINCTCOUNT ( clean_sales[invoice_no] ),
                clean_sales[revenue] > 0
            ) > 1
        )
    ),
    clean_sales[revenue] > 0,
    NOT ISBLANK ( clean_sales[customer_id] )
)
```

### One-Time Customers

```dax
One-Time Customers = 
CALCULATE (
    COUNTROWS (
        FILTER (
            VALUES ( clean_sales[customer_id] ),
            CALCULATE (
                DISTINCTCOUNT ( clean_sales[invoice_no] ),
                clean_sales[revenue] > 0
            ) = 1
        )
    ),
    clean_sales[revenue] > 0,
    NOT ISBLANK ( clean_sales[customer_id] )
)
```

### Repeat Customer Rate

```dax
Repeat Customer Rate % = 
DIVIDE (
    [Repeat Customers],
    [Total Customers],
    0
)
```

## RFM measures

### RFM Customer Count

```dax
RFM Customer Count = 
DISTINCTCOUNT ( rfm_customers[customer_id] )
```

### RFM Revenue

```dax
RFM Revenue = 
SUM ( rfm_customers[monetary] )
```

### Revenue by Segment

```dax
Revenue by Segment = 
[RFM Revenue]
```

### Customer Count by Segment

```dax
Customers by Segment = 
[RFM Customer Count]
```

### Segment Revenue Share

```dax
Segment Revenue Share % = 
DIVIDE (
    [RFM Revenue],
    CALCULATE ( [RFM Revenue], ALL ( rfm_customers[segment] ) ),
    0
)
```

### Segment Customer Share

```dax
Segment Customer Share % = 
DIVIDE (
    [RFM Customer Count],
    CALCULATE ( [RFM Customer Count], ALL ( rfm_customers[segment] ) ),
    0
)
```

### Champions Revenue

```dax
Champions Revenue = 
CALCULATE (
    [RFM Revenue],
    rfm_customers[segment] = "Champions"
)
```

### Champions Count

```dax
Champions Count = 
CALCULATE (
    [RFM Customer Count],
    rfm_customers[segment] = "Champions"
)
```

### At-Risk Customers Revenue

```dax
At-Risk Revenue = 
CALCULATE (
    [RFM Revenue],
    rfm_customers[segment] = "At-risk customers"
)
```

### Lost Customers Revenue

```dax
Lost Customers Revenue = 
CALCULATE (
    [RFM Revenue],
    rfm_customers[segment] = "Lost or low-value customers"
)
```

## Formatting

Apply the following formatting to measures:

| Measure | Format | Decimal Places |
|---------|--------|----------------|
| Revenue measures | Currency (£) | 2 |
| Count measures | Whole Number | 0 |
| Percentage measures | Percentage | 1 or 2 |
| AOV | Currency (£) | 2 |
| MoM Growth | Percentage | 1 |

## Version

- **Created:** 2026-08-18
- **Based on commit:** 7530f9d (feat: add organized SQL analysis pipeline)
- **Power BI Desktop:** Recommended version 2024 or later
