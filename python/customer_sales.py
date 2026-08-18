from pathlib import Path

import pandas as pd


SALES_PATH = Path("data/processed/clean_sales.parquet")
OUTPUT_PATH = Path("docs/customer_sales.csv")


def main() -> None:
    if not SALES_PATH.exists():
        raise FileNotFoundError(
            f"Processed sales dataset not found: {SALES_PATH}. "
            "Run python/clean_data.py first."
        )

    sales = pd.read_parquet(SALES_PATH)
    customer_sales = sales.loc[sales["customer_id"].notna()].copy()

    customer_summary = (
        customer_sales.groupby("customer_id")
        .agg(
            revenue=("revenue", "sum"),
            orders=("invoice_no", "nunique"),
            units_sold=("quantity", "sum"),
            products_purchased=("stock_code", "nunique"),
            countries=("country", "nunique"),
            first_purchase_date=("invoice_date", "min"),
            last_purchase_date=("invoice_date", "max"),
            sales_rows=("invoice_no", "size"),
        )
        .reset_index()
        .sort_values("revenue", ascending=False)
    )

    customer_summary["average_order_value"] = (
        customer_summary["revenue"] / customer_summary["orders"]
    )
    customer_summary["is_repeat_customer"] = customer_summary["orders"] > 1
    customer_summary["customer_lifetime_days"] = (
        customer_summary["last_purchase_date"]
        - customer_summary["first_purchase_date"]
    ).dt.days

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    customer_summary.to_csv(OUTPUT_PATH, index=False)

    print(f"Customer sales written to: {OUTPUT_PATH}")
    print("\nTop 20 customers by revenue:")
    print(customer_summary.head(20).to_string(index=False))


if __name__ == "__main__":
    main()
