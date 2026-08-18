# Business Insights

## Scope

This document summarizes evidence-based findings from the E-Commerce Customer & Sales Analytics project. All insights derive from validated outputs in the `docs/` directory and reproducible Python pipelines. The analysis covers 524,878 clean sales transactions from December 1, 2010 through December 9, 2011, representing £10,642,110.80 in revenue.

---

## Finding 1: Revenue is heavily concentrated among Champions

### Evidence

- **Champions**: 941 customers (21.69% of RFM customers) contribute £5,741,913.58 (64.61% of RFM revenue).
- **Lost or low-value customers**: 824 customers (18.99%) contribute only £188,415.28 (2.12%).
- **Loyal customers**: 457 customers (10.53%) contribute £901,405.29 (10.14%).

### Interpretation

A small, highly engaged segment drives nearly two-thirds of identifiable customer revenue. The bottom segment comprises a similar number of customers but generates minimal revenue.

### Recommended action

- Prioritize retention programs for Champions (exclusive offers, early access, loyalty tiers).
- Design win-back campaigns for Lost or low-value customers with low-cost incentives.
- Investigate what distinguishes Champions' purchase patterns (product mix, order frequency, recency).

### Caveat

RFM analysis includes only 4,338 customers with identified CustomerIDs. Customers with missing IDs are excluded from segmentation but contribute to overall revenue.

---

## Finding 2: The United Kingdom dominates revenue

### Evidence

- **United Kingdom**: £9,001,744.09 (84.59% of total revenue).
- **Netherlands**: £285,446.34 (2.68%).
- **EIRE**: £283,140.52 (2.66%).
- **Germany**: £228,678.40 (2.15%).
- **France**: £209,625.37 (1.97%).
- **Total countries**: 38.

### Interpretation

Revenue is highly concentrated in the UK market. The top five countries account for approximately 94% of revenue, with the UK alone representing over 84%.

### Recommended action

- Deepen UK market penetration through targeted promotions and localized campaigns.
- Evaluate expansion strategies for Netherlands, EIRE, Germany, and France to diversify revenue.
- Investigate why 33 other countries contribute less than 6% combined (pricing, shipping, marketing).

### Caveat

Country-level analysis includes all clean sales. Some countries may have small sample sizes, making percentages volatile.

---

## Finding 3: Revenue accelerated in the second half of 2011

### Evidence

- **November 2011**: £1,503,866.78 revenue, 2,769 orders, 751,377 units sold, 1,664 identified customers (strongest month).
- **September 2011**: 39.40% month-over-month revenue increase (largest growth).
- **December 2011**: 57.59% decline versus November, but data ends on December 9 (incomplete month).
- **Analysis period**: 13 calendar months (December 2010 partial through December 2011 partial).

### Interpretation

Sales momentum built through 2011, peaking in November. The December decline reflects incomplete data, not an actual downturn.

### Recommended action

- Plan inventory and marketing capacity for Q4 peaks, especially November.
- Investigate drivers of September's 39.40% growth (promotions, seasonality, new products).
- Use full-year data in future analyses to avoid partial-month distortions.

### Caveat

December 2010 and December 2011 are incomplete (data ends December 9, 2011). Month-over-month comparisons involving December are not apples-to-apples.

---

## Finding 4: Repeat customers are important

### Evidence

- **Total identified customers**: 4,338.
- **Repeat customers**: 2,845 (65.58%).
- **One-time customers**: 1,493 (34.42%).
- **Average order value**: £533.17.
- **Average order lines per order**: 26.30.

### Interpretation

Nearly two-thirds of identified customers made multiple purchases, indicating strong retention potential. High average order value and line count suggest basket-building opportunities.

### Recommended action

- Implement loyalty programs targeting one-time customers to convert them to repeat buyers.
- Analyze what differentiates repeat from one-time customers (product categories, acquisition channel, geography).
- Use RFM scores to identify at-risk repeat customers for proactive engagement.

### Caveat

Customer counts exclude 135,080 transactions with missing CustomerIDs. True repeat rates may differ if those transactions were attributable.

---

## Finding 5: Lost or low-value customers are numerous but low-revenue

### Evidence

- **Lost or low-value customers**: 824 customers (18.99% of RFM customers).
- **Revenue contribution**: £188,415.28 (2.12% of RFM revenue).
- **Average revenue per customer in this segment**: £228.66.

### Interpretation

This segment represents a large number of customers with minimal revenue impact. They may be dormant, low-spend, or one-time buyers with poor recency/frequency/monetary scores.

### Recommended action

- Test low-cost reactivation campaigns (email reminders, small discounts).
- Accept that some customers will remain low-value; focus resources on higher-potential segments.
- Monitor whether Lost customers migrate to other segments over time.

### Caveat

RFM analysis date is 2011-12-10. Customers classified as "Lost" may have been active earlier in the year but not recently.

---

## Finding 6: Cannot-lose customers require targeted reactivation

### Evidence

- **Cannot lose them**: 248 customers (5.72% of RFM customers).
- **Revenue contribution**: £334,793.25 (3.77% of RFM revenue).
- **Average revenue per customer in this segment**: £1,349.97.

### Interpretation

This segment has historically high monetary value but is at risk due to poor recency or frequency. They represent meaningful revenue (£334k) that could be lost without intervention.

### Recommended action

- Prioritize personalized win-back campaigns (dedicated outreach, high-value offers).
- Investigate why these customers became inactive (service issues, product changes, competitive offers).
- Track reactivation rates and revenue recovery post-campaign.

### Caveat

"Cannot lose them" is an RFM label based on scoring thresholds. Actual churn risk depends on external factors not captured in transaction data.

---

## Product and data-quality notes

### Top product

- **DOTCOM POSTAGE**: £206,248.77 revenue, 706 units sold (highest-revenue product).
- **Total distinct products**: 3,922.

### Data-quality flags from cleaning

- **Exact duplicate rows removed**: 5,268.
- **Cancellation/return rows separated**: 11,763 unique rows (overlapping conditions).
- **Missing CustomerIDs**: 135,080 rows (25.0% of clean sales).
- **Missing descriptions**: 1,454 rows.
- **Negative quantities**: 10,624 rows (flagged, some retained as valid returns).
- **Non-positive unit prices**: 2,517 rows (flagged, some retained).

### Interpretation

The dataset required substantial cleaning. Cancellations and returns are preserved separately for analysis but excluded from core KPIs. Missing CustomerIDs limit customer-level insights to 74.6% of clean sales rows.

### Recommended action

- Document data-quality assumptions in all downstream reports.
- Use `returns_cancellations.parquet` for return-rate analysis.
- Treat products with missing descriptions cautiously in product-level insights.

### Caveat

Extreme values (e.g., unit prices up to £38,970, quantities up to 80,995) were retained after flagging. Some may represent data errors rather than true transactions.

---

## Limitations

1. **Partial December 2011**: Data ends December 9, 2011. December metrics are incomplete and not comparable to full months.
2. **Missing CustomerIDs**: 135,080 clean-sales rows (25.6%) lack CustomerIDs, excluding them from customer and RFM analysis.
3. **Single-year snapshot**: Analysis covers only 12 months. Seasonal patterns beyond this period are unknown.
4. **UK concentration**: 84.59% of revenue is from the UK. Insights may not generalize to other markets.
5. **No external context**: No marketing spend, pricing changes, or competitive data to explain trends.
6. **RFM scoring date**: RFM uses 2011-12-10 as the analysis date. Scores reflect that point in time only.
7. **Overlapping return conditions**: The 11,763 returns/cancellations rows have overlapping flags (cancellations, negative quantities, etc.), so counts are not additive.

---

## Reproducibility

All findings derive from committed, reproducible pipelines:

- **Data cleaning**: `python/clean_data.py` → `data/processed/clean_sales.parquet`.
- **KPI profile**: `python/profile_sales.py` → `docs/sales_profile.csv`.
- **Monthly trends**: `python/monthly_sales.py` → `docs/monthly_sales.csv`.
- **Country analysis**: `python/country_sales.py` → `docs/country_sales.csv`.
- **Product analysis**: `python/product_sales.py` → `docs/product_sales.csv`.
- **Customer analysis**: `python/customer_sales.py` → `docs/customer_sales.csv`.
- **RFM segmentation**: `python/rfm_segmentation.py` → `docs/rfm_customers.csv`.
- **RFM summary**: `python/rfm_summary.py` → `docs/rfm_segments.csv`.

To regenerate all outputs:

```bash
# From repository root
python python/clean_data.py
python python/profile_sales.py
python python/monthly_sales.py
python python/country_sales.py
python python/product_sales.py
python python/customer_sales.py
python python/rfm_segmentation.py
python python/rfm_summary.py
```

All generated files in `data/processed/` and `docs/*.csv` are Git-ignored except for final documentation. The raw dataset (`data/raw/online_retail_raw.xlsx`) is never committed.

---

## Attribution

- **Dataset**: UCI Machine Learning Repository, "Online Retail" (https://archive.ics.uci.edu/dataset/352/online+retail).
- **License**: Dataset is publicly available for research and educational use.
- **Project**: E-Commerce Customer & Sales Analytics by Rai Ritik (https://github.com/rai-ritik/ecommerce-customer-sales-analytics).

---

## Version

- **Document created**: 2026-08-18.
- **Based on commit**: 930d41e (feat: add RFM segment summary).
- **Analysis date**: 2011-12-10 (RFM reference date).