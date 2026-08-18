from pathlib import Path

import pandas as pd


SALES_PATH = Path("data/processed/clean_sales.parquet")
OUTPUT_PATH = Path("docs/product_sales.csv")


def main() -> None:
    if not SALES_PATH.exists():
        raise FileNotFoundError(
            f"Processed sales dataset not found: {SALES_PATH}. "
            "Run python/clean_data.py first."
        )

    sales = pd.read_parquet(SALES_PATH)

    product_sales = (
        sales.groupby("stock_code")
        .agg(
            description=("description", "first"),
            revenue=("revenue", "sum"),
            units_sold=("quantity", "sum"),
            orders=("invoice_no", "nunique"),
            customers_with_id=("customer_id", "nunique"),
            sales_rows=("invoice_no", "size"),
        )
        .reset_index()
        .sort_values("revenue", ascending=False)
    )

    product_sales["revenue_share_pct"] = (
        product_sales["revenue"] / product_sales["revenue"].sum() * 100
    )

    product_sales["average_unit_price"] = (
        product_sales["revenue"] / product_sales["units_sold"]
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    product_sales.to_csv(OUTPUT_PATH, index=False)

    print(f"Product sales written to: {OUTPUT_PATH}")
    print("\nTop 20 products by revenue:")
    print(product_sales.head(20).to_string(index=False))


if __name__ == "__main__":
    main()
