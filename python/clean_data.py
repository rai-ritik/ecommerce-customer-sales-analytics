from pathlib import Path

import pandas as pd


RAW_PATH = Path("data/raw/online_retail_raw.xlsx")
OUTPUT_DIR = Path("data/processed")

SALES_OUTPUT_PATH = OUTPUT_DIR / "clean_sales.parquet"
RETURNS_OUTPUT_PATH = OUTPUT_DIR / "returns_cancellations.parquet"
VALIDATION_PATH = OUTPUT_DIR / "cleaning_validation_report.csv"

EXPECTED_COLUMNS = [
    "InvoiceNo",
    "StockCode",
    "Description",
    "Quantity",
    "InvoiceDate",
    "UnitPrice",
    "CustomerID",
    "Country",
]


def load_raw_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Raw dataset not found: {path}")

    dataframe = pd.read_excel(path, engine="openpyxl")

    missing_columns = set(EXPECTED_COLUMNS) - set(dataframe.columns)
    unexpected_columns = set(dataframe.columns) - set(EXPECTED_COLUMNS)

    if missing_columns or unexpected_columns:
        raise ValueError(
            "Schema mismatch. "
            f"Missing columns: {sorted(missing_columns)}. "
            f"Unexpected columns: {sorted(unexpected_columns)}."
        )

    return dataframe


def standardize_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe = dataframe.rename(
        columns={
            "InvoiceNo": "invoice_no",
            "StockCode": "stock_code",
            "Description": "description",
            "Quantity": "quantity",
            "InvoiceDate": "invoice_date",
            "UnitPrice": "unit_price",
            "CustomerID": "customer_id",
            "Country": "country",
        }
    )

    dataframe["invoice_no"] = dataframe["invoice_no"].astype("string").str.strip()
    dataframe["stock_code"] = dataframe["stock_code"].astype("string").str.strip()
    dataframe["description_missing"] = dataframe["description"].isna()
    dataframe["description"] = (
        dataframe["description"]
        .astype("string")
        .str.strip()
        .fillna("Unknown product")
    )
    dataframe["country"] = dataframe["country"].astype("string").str.strip()

    dataframe["invoice_date"] = pd.to_datetime(
        dataframe["invoice_date"],
        errors="coerce",
    )
    dataframe["quantity"] = pd.to_numeric(
        dataframe["quantity"],
        errors="coerce",
    )
    dataframe["unit_price"] = pd.to_numeric(
        dataframe["unit_price"],
        errors="coerce",
    )
    dataframe["customer_id"] = pd.to_numeric(
        dataframe["customer_id"],
        errors="coerce",
    ).astype("Int64")

    return dataframe


def add_derived_fields(dataframe: pd.DataFrame) -> pd.DataFrame:
    invoice_text = dataframe["invoice_no"].str.upper()

    dataframe["is_cancellation"] = invoice_text.str.startswith("C", na=False)
    dataframe["is_negative_quantity"] = dataframe["quantity"] < 0
    dataframe["is_non_positive_price"] = dataframe["unit_price"] <= 0
    dataframe["has_customer_id"] = dataframe["customer_id"].notna()
    dataframe["revenue"] = dataframe["quantity"] * dataframe["unit_price"]

    dataframe["invoice_date_only"] = dataframe["invoice_date"].dt.date
    dataframe["year"] = dataframe["invoice_date"].dt.year.astype("Int64")
    dataframe["month"] = dataframe["invoice_date"].dt.month.astype("Int64")
    dataframe["month_name"] = dataframe["invoice_date"].dt.month_name()
    dataframe["quarter"] = dataframe["invoice_date"].dt.to_period("Q").astype(
        "string"
    )
    dataframe["weekday"] = dataframe["invoice_date"].dt.weekday.astype("Int64")
    dataframe["weekday_name"] = dataframe["invoice_date"].dt.day_name()

    return dataframe


def build_cleaning_report(
    raw_dataframe: pd.DataFrame,
    standardized_dataframe: pd.DataFrame,
    deduplicated_dataframe: pd.DataFrame,
    sales_dataframe: pd.DataFrame,
    returns_dataframe: pd.DataFrame,
) -> pd.DataFrame:
    invalid_dates = standardized_dataframe["invoice_date"].isna()
    invalid_quantities = standardized_dataframe["quantity"].isna()
    invalid_prices = standardized_dataframe["unit_price"].isna()

    report = pd.DataFrame(
        {
            "metric": [
                "raw_rows",
                "raw_columns",
                "exact_duplicate_rows",
                "rows_after_duplicate_removal",
                "missing_descriptions",
                "missing_customer_ids",
                "cancellation_rows",
                "negative_quantity_rows",
                "non_positive_unit_price_rows",
                "invalid_invoice_date_rows",
                "invalid_quantity_rows",
                "invalid_unit_price_rows",
                "returns_cancellations_rows",
                "clean_sales_rows",
                "clean_sales_rows_with_customer_id",
                "distinct_clean_sales_invoices",
                "distinct_clean_sales_products",
                "distinct_clean_sales_countries",
                "clean_sales_revenue",
                "returns_cancellations_revenue",
            ],
            "value": [
                len(raw_dataframe),
                len(raw_dataframe.columns),
                int(raw_dataframe.duplicated().sum()),
                len(deduplicated_dataframe),
                int(standardized_dataframe["description_missing"].sum()),
                int((~standardized_dataframe["has_customer_id"]).sum()),
                int(standardized_dataframe["is_cancellation"].sum()),
                int(standardized_dataframe["is_negative_quantity"].sum()),
                int(standardized_dataframe["is_non_positive_price"].sum()),
                int(invalid_dates.sum()),
                int(invalid_quantities.sum()),
                int(invalid_prices.sum()),
                len(returns_dataframe),
                len(sales_dataframe),
                int(sales_dataframe["customer_id"].notna().sum()),
                int(sales_dataframe["invoice_no"].nunique()),
                int(sales_dataframe["stock_code"].nunique()),
                int(sales_dataframe["country"].nunique()),
                float(sales_dataframe["revenue"].sum()),
                float(returns_dataframe["revenue"].sum()),
            ],
        }
    )

    return report


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    raw_dataframe = load_raw_data(RAW_PATH)
    standardized_dataframe = standardize_columns(raw_dataframe)
    standardized_dataframe = add_derived_fields(standardized_dataframe)

    deduplicated_dataframe = standardized_dataframe.drop_duplicates().copy()

    invalid_dates = deduplicated_dataframe["invoice_date"].isna()
    invalid_quantities = deduplicated_dataframe["quantity"].isna()
    invalid_prices = deduplicated_dataframe["unit_price"].isna()

    valid_base = deduplicated_dataframe.loc[
        ~(invalid_dates | invalid_quantities | invalid_prices)
    ].copy()

    returns_dataframe = valid_base.loc[
        valid_base["is_cancellation"]
        | valid_base["is_negative_quantity"]
        | valid_base["is_non_positive_price"]
    ].copy()

    sales_dataframe = valid_base.loc[
        ~valid_base["is_cancellation"]
        & ~valid_base["is_negative_quantity"]
        & ~valid_base["is_non_positive_price"]
    ].copy()

    cleaning_report = build_cleaning_report(
        raw_dataframe=raw_dataframe,
        standardized_dataframe=standardized_dataframe,
        deduplicated_dataframe=deduplicated_dataframe,
        sales_dataframe=sales_dataframe,
        returns_dataframe=returns_dataframe,
    )

    sales_dataframe.to_parquet(SALES_OUTPUT_PATH, index=False)
    returns_dataframe.to_parquet(RETURNS_OUTPUT_PATH, index=False)
    cleaning_report.to_csv(VALIDATION_PATH, index=False)

    print(f"Clean sales dataset: {SALES_OUTPUT_PATH}")
    print(f"Returns/cancellations dataset: {RETURNS_OUTPUT_PATH}")
    print(f"Cleaning report: {VALIDATION_PATH}")
    print(f"Clean sales shape: {sales_dataframe.shape}")
    print(f"Returns/cancellations shape: {returns_dataframe.shape}")


if __name__ == "__main__":
    main()
