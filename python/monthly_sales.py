from pathlib import Path

import pandas as pd


SALES_PATH = Path("data/processed/clean_sales.parquet")
OUTPUT_PATH = Path("docs/monthly_sales.csv")


def main() -> None:
    if not SALES_PATH.exists():
        raise FileNotFoundError(
            f"Processed sales dataset not found: {SALES_PATH}. "
            "Run python/clean_data.py first."
        )

    sales = pd.read_parquet(SALES_PATH)
    sales["month_start"] = sales["invoice_date"].dt.to_period("M").dt.to_timestamp()

    monthly_sales = (
        sales.groupby("month_start")
        .agg(
            revenue=("revenue", "sum"),
            units_sold=("quantity", "sum"),
            orders=("invoice_no", "nunique"),
            customers_with_id=("customer_id", "nunique"),
            sales_rows=("invoice_no", "size"),
        )
        .reset_index()
        .sort_values("month_start")
    )

    monthly_sales["average_order_value"] = (
        monthly_sales["revenue"] / monthly_sales["orders"]
    )
    monthly_sales["revenue_growth_pct"] = (
        monthly_sales["revenue"].pct_change() * 100
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    monthly_sales.to_csv(OUTPUT_PATH, index=False, float_format="%.2f")

    print(f"Monthly sales written to: {OUTPUT_PATH}")
    print("\nMonthly sales:")
    print(monthly_sales.to_string(index=False))


if __name__ == "__main__":
    main()
