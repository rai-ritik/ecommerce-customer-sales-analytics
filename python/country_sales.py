from pathlib import Path

import pandas as pd


SALES_PATH = Path("data/processed/clean_sales.parquet")
OUTPUT_PATH = Path("docs/country_sales.csv")


def main() -> None:
    if not SALES_PATH.exists():
        raise FileNotFoundError(
            f"Processed sales dataset not found: {SALES_PATH}. "
            "Run python/clean_data.py first."
        )

    sales = pd.read_parquet(SALES_PATH)

    country_sales = (
        sales.groupby("country")
        .agg(
            revenue=("revenue", "sum"),
            units_sold=("quantity", "sum"),
            orders=("invoice_no", "nunique"),
            customers_with_id=("customer_id", "nunique"),
            sales_rows=("invoice_no", "size"),
            unique_products=("stock_code", "nunique"),
        )
        .reset_index()
        .sort_values("revenue", ascending=False)
    )

    total_revenue = country_sales["revenue"].sum()
    country_sales["revenue_share_pct"] = (
        country_sales["revenue"] / total_revenue * 100
    )
    country_sales["average_order_value"] = (
        country_sales["revenue"] / country_sales["orders"]
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    country_sales.to_csv(OUTPUT_PATH, index=False, float_format="%.2f")

    print(f"Country sales written to: {OUTPUT_PATH}")
    print("\nTop 10 countries by revenue:")
    print(country_sales.head(10).to_string(index=False))


if __name__ == "__main__":
    main()
