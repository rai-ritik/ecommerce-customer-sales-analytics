## 📊 Power BI Dashboard

The dashboard provides two comprehensive views of the e-commerce analytics: **Executive Overview** for high-level business metrics and **Customer Intelligence** for deep customer segmentation analysis.

### Executive Overview

![Executive Overview](docs/images/dashboard_executive_overview.png)

**Key Visuals:**
- **KPI Cards:** Total Revenue (£10.6M), Total Orders (19,960), Avg Order Value (£533), Total Customers (4,338), Repeat Rate (65.58%)
- **Monthly Revenue Trend:** Line chart showing growth from Dec 2010 to Dec 2011, peaking at £1.5M in November 2011
- **Top 10 Countries by Revenue:** Horizontal bar chart with UK dominating at £9M (84.59% of total revenue)
- **Top 10 Products by Revenue:** Table showing DOTCOM POSTAGE as top product (£206K revenue, 706 units)
- **Monthly Orders vs Revenue:** Combo chart comparing order volume and revenue trends

### Customer Intelligence

![Customer Intelligence](docs/images/dashboard_customer_intelligence.png)

**Key Visuals:**
- **Customer KPIs:** Identified Customers (4,338), Repeat Customers (2,845), One-time Customers (1,493), Repeat Rate (65.58%), Avg Revenue per Customer (£2,453)
- **RFM Segments Distribution:** Donut chart showing 8 customer segments, with Champions (21.69%) and Lost/low-value (18.99%) as largest groups
- **Revenue by RFM Segment:** Horizontal bar chart revealing Champions drive 64.61% of revenue (£5.74M)
- **RFM Segment Performance Matrix:** Detailed table with customer count, share, revenue, and revenue share for all 8 segments
- **Top 10 Customers by Revenue:** Table showing customer 14646 as top spender (£280K, 526 orders)

### Dashboard Features

**Data Model:**
- Star schema with 4 dimension tables (Date, Customer, Product, Country) and 1 fact table (Sales)
- Relationships: 1-to-many from dimensions to fact table
- Date table with full time intelligence support

**Key DAX Measures:**
- `Total Revenue` = SUM(Revenue)
- `Total Orders` = DISTINCTCOUNT(InvoiceNo)
- `Avg Order Value` = DIVIDE(Total Revenue, Total Orders)
- `Repeat Customers` = Customers with >1 order
- `Repeat Customer Rate` = Repeat Customers / Total Customers
- RFM segment calculations (Recency, Frequency, Monetary scoring)

**Interactive Elements:**
- Slicers for date range, country, and customer segment
- Cross-filtering between all visuals
- Tooltips with detailed context

### How to Use This Dashboard

1. **Open in Power BI Desktop:** Load `powerbi/ecommerce_customer_analytics.pbix`
2. **Refresh Data:** Ensure `data/processed/clean_sales.parquet` is up to date
3. **Navigate Pages:** Use tabs at bottom to switch between Executive Overview and Customer Intelligence
4. **Apply Filters:** Use slicers to filter by date range, country, or customer segment
5. **Export Reports:** File → Export → Export to PDF for sharing insights

### Business Insights from Dashboard

**Revenue Performance:**
- Total revenue: £10.6M across 19,960 orders
- Strong growth trajectory: £150K (Dec 2010) → £1.5M (Nov 2011)
- UK market dominates: 84.59% of revenue, but 37 other countries show expansion opportunities

**Customer Behavior:**
- 65.58% repeat customer rate indicates strong customer loyalty
- Champions segment (21.69% of customers) generates 64.61% of revenue
- Top customer (14646) contributes £280K (2.6% of total revenue)

**Product Strategy:**
- DOTCOM POSTAGE is top revenue generator (£206K)
- High-value decorative items (cakestands, ornaments, garlands) in top 10
- Average order value of £533 suggests bulk purchasing behavior

**Actionable Recommendations:**
1. **Retain Champions:** Implement VIP loyalty program for 941 champion customers
2. **Reactivate At-risk:** Target 663 at-risk customers with win-back campaigns
3. **Expand Internationally:** Leverage UK success to grow Germany, France, Netherlands markets
4. **Bundle Products:** Create bundles featuring top products to increase AOV further

---

**Dashboard Created:** 2026-08-18  
**Tool:** Power BI Desktop  
**Data Source:** UCI Online Retail (clean_sales.parquet)  
**Analysis Period:** Dec 1, 2010 - Dec 9, 2011
