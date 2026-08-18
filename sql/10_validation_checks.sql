-- =============================================================================
-- 10_validation_checks.sql
-- Data validation and reconciliation
-- =============================================================================

USE ecommerce_retail;

-- Row counts
SELECT 'clean_sales' AS tbl, COUNT(*) AS rows FROM clean_sales
UNION ALL SELECT 'returns_cancellations', COUNT(*) FROM returns_cancellations
UNION ALL SELECT 'rfm_customers', COUNT(*) FROM rfm_customers;

-- Revenue reconciliation
SELECT 
    'Total revenue' AS check_name,
    SUM(revenue) AS total
FROM clean_sales WHERE revenue > 0;

-- Expected: £10,642,110.80
