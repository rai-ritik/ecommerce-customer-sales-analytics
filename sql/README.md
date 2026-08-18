# SQL Analysis Documentation

## Directory structure

sql/
├── README.md
├── 01_create_database.sql
├── 02_create_tables.sql
├── 03_import_data.sql
├── 04_kpi_analysis.sql
├── 05_product_analysis.sql
├── 06_country_analysis.sql
├── 07_time_trends.sql
├── 08_customer_analysis.sql
├── 09_rfm_segmentation.sql
└── 10_validation_checks.sql

## Usage

1. Create database: `mysql -u user -p < sql/01_create_database.sql`
2. Create tables: `mysql -u user -p < sql/02_create_tables.sql`
3. Import data: Update paths in 03_import_data.sql, then run
4. Run analysis: `mysql -u user -p ecommerce_retail < sql/04_kpi_analysis.sql`

## Expected results

- clean_sales: 524,878 rows
- returns_cancellations: 11,763 rows
- rfm_customers: 4,338 rows
- Total revenue: £10,642,110.80
- Products: 3,922
- Countries: 38
- Customers: 4,338

## Version

Created: 2026-08-18
MySQL: 8.0+
