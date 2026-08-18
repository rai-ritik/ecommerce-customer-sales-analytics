-- =============================================================================
-- 04_kpi_analysis.sql
-- Calculate overall sales KPIs
-- =============================================================================

USE ecommerce_retail;

SELECT 
    'Revenue' AS kpi,
    CONCAT('£', FORMAT(SUM(revenue), 2)) AS value
FROM clean_sales WHERE revenue > 0
UNION ALL
SELECT 'Orders', FORMAT(COUNT(DISTINCT invoice_no), 0)
FROM clean_sales WHERE revenue > 0
UNION ALL
SELECT 'Products', FORMAT(COUNT(DISTINCT stock_code), 0)
FROM clean_sales WHERE revenue > 0
UNION ALL
SELECT 'Countries', FORMAT(COUNT(DISTINCT country), 0)
FROM clean_sales WHERE revenue > 0
UNION ALL
SELECT 'Customers', FORMAT(COUNT(DISTINCT customer_id), 0)
FROM clean_sales WHERE revenue > 0 AND customer_id IS NOT NULL;
