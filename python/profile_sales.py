from pathlib import Path

import pandas as pd


SALES_PATH = Path("data/processed/clean_sales.parquet")
OUTPUT_PATH = Path("docs/sales_profile.csv")


def main() -> None:
    if not SALES_PATH.exists():
        raise FileNotFoundError(
            f"Processed sales dataset not found: {SALES_PATH}. "
            "Run python/clean_data.py first."
        )

    sales = pd.read_parquet(SALES_PATH)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    invoice_revenue = sales.groupby("invoice_no")["revenue"].sum()

    profile = pd.DataFrame(
        {
            "metric": [
                "sales_rows",
                "revenue",
                "units_sold",
                "orders",
                "customers_with_id",
                "unique_products",
                "unique_countries",
                "average_order_value",
                "average_order_lines_per_order",
                "repeat_customers",
                "one_time_customers",
                "first_transaction_date",
                "last_transaction_date",
            ],
            "value": [
                len(sales),
                sales["revenue"].sum(),
                sales["quantity"].sum(),
                sales["invoice_no"].nunique(),
                sales["customer_id"].nunique(),
                sales["stock_code"].nunique(),
                sales["country"].nunique(),
                invoice_revenue.mean(),
                len(sales) / sales["invoice_no"].nunique(),
                (sales.groupby("customer_id")["invoice_no"].nunique() > 1).sum(),
                (sales.groupby("customer_id")["invoice_no"].nunique() == 1).sum(),
                sales["invoice_date"].min(),
                sales["invoice_date"].max(),
            ],
        }
    )

    profile.to_csv(OUTPUT_PATH, index=False)

    print(f"Profile written to: {OUTPUT_PATH}")
    print(profile.to_string(index=False))


if __name__ == "__main__":
    main()
