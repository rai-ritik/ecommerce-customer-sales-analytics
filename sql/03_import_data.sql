-- =============================================================================
-- 03_import_data.sql
-- Import cleaned data from CSV files into MySQL
-- =============================================================================

USE ecommerce_retail;

-- Load clean_sales from CSV (update path to your file)
-- LOAD DATA INFILE '/path/to/clean_sales.csv'
-- INTO TABLE clean_sales
-- FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n'
-- IGNORE 1 ROWS;

-- Verify imports
SELECT 'clean_sales' AS table_name, COUNT(*) AS row_count FROM clean_sales
UNION ALL
SELECT 'returns_cancellations', COUNT(*) FROM returns_cancellations
UNION ALL
SELECT 'rfm_customers', COUNT(*) FROM rfm_customers;

-- Expected: 524878, 11763, 4338
