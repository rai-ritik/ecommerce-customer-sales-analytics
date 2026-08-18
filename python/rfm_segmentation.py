from pathlib import Path

import pandas as pd


SALES_PATH = Path("data/processed/clean_sales.parquet")
OUTPUT_PATH = Path("docs/rfm_customers.csv")

ANALYSIS_DATE = pd.Timestamp("2011-12-10")


def quintile_score(series: pd.Series, reverse: bool = False) -> pd.Series:
    ranks = series.rank(method="first", ascending=True)

    scores = pd.qcut(
        ranks,
        q=5,
        labels=[1, 2, 3, 4, 5],
    ).astype(int)

    if reverse:
        scores = 6 - scores

    return scores


def assign_segment(row: pd.Series) -> str:
    r_score = row["r_score"]
    f_score = row["f_score"]
    m_score = row["m_score"]

    if r_score >= 4 and f_score >= 4 and m_score >= 4:
        return "Champions"
    if r_score >= 3 and f_score >= 4 and m_score >= 3:
        return "Loyal customers"
    if r_score >= 4 and f_score <= 2:
        return "New customers"
    if r_score >= 3 and f_score >= 3 and m_score <= 3:
        return "Potential loyalists"
    if r_score <= 2 and f_score >= 3:
        return "At-risk customers"
    if r_score <= 2 and f_score <= 2 and m_score >= 3:
        return "Cannot lose them"
    if r_score <= 2 and f_score <= 2 and m_score <= 2:
        return "Lost or low-value customers"

    return "Other customers"


def main() -> None:
    if not SALES_PATH.exists():
        raise FileNotFoundError(
            f"Processed sales dataset not found: {SALES_PATH}. "
            "Run python/clean_data.py first."
        )

    sales = pd.read_parquet(SALES_PATH)
    sales = sales.loc[sales["customer_id"].notna()].copy()

    rfm = (
        sales.groupby("customer_id")
        .agg(
            last_purchase_date=("invoice_date", "max"),
            frequency=("invoice_no", "nunique"),
            monetary=("revenue", "sum"),
            units_sold=("quantity", "sum"),
            products_purchased=("stock_code", "nunique"),
            country=("country", "first"),
        )
        .reset_index()
    )

    rfm["recency"] = (
        ANALYSIS_DATE - rfm["last_purchase_date"].dt.normalize()
    ).dt.days

    rfm["r_score"] = quintile_score(rfm["recency"], reverse=True)
    rfm["f_score"] = quintile_score(rfm["frequency"], reverse=False)
    rfm["m_score"] = quintile_score(rfm["monetary"], reverse=False)

    rfm["rfm_score"] = (
        rfm["r_score"] + rfm["f_score"] + rfm["m_score"]
    )
    rfm["rfm_code"] = (
        rfm["r_score"].astype(str)
        + rfm["f_score"].astype(str)
        + rfm["m_score"].astype(str)
    )
    rfm["segment"] = rfm.apply(assign_segment, axis=1)

    rfm = rfm.sort_values(
        ["rfm_score", "monetary"],
        ascending=[False, False],
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    rfm.to_csv(OUTPUT_PATH, index=False)

    print(f"RFM output written to: {OUTPUT_PATH}")
    print(f"Analysis date: {ANALYSIS_DATE.date()}")
    print("\nSegment counts:")
    print(rfm["segment"].value_counts().to_string())
    print("\nTop 20 customers by RFM score:")
    print(rfm.head(20).to_string(index=False))


if __name__ == "__main__":
    main()
