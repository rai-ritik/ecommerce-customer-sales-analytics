from pathlib import Path

import pandas as pd


RFM_PATH = Path("docs/rfm_customers.csv")
OUTPUT_PATH = Path("docs/rfm_segments.csv")


def main() -> None:
    if not RFM_PATH.exists():
        raise FileNotFoundError(
            f"RFM dataset not found: {RFM_PATH}. "
            "Run python/rfm_segmentation.py first."
        )

    rfm = pd.read_csv(RFM_PATH)

    segment_summary = (
        rfm.groupby("segment")
        .agg(
            customers=("customer_id", "nunique"),
            revenue=("monetary", "sum"),
            average_recency=("recency", "mean"),
            average_frequency=("frequency", "mean"),
            average_monetary=("monetary", "mean"),
            average_rfm_score=("rfm_score", "mean"),
        )
        .reset_index()
        .sort_values("revenue", ascending=False)
    )

    total_customers = segment_summary["customers"].sum()
    total_revenue = segment_summary["revenue"].sum()

    segment_summary["customer_share_pct"] = (
        segment_summary["customers"] / total_customers * 100
    )
    segment_summary["revenue_share_pct"] = (
        segment_summary["revenue"] / total_revenue * 100
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    segment_summary.to_csv(OUTPUT_PATH, index=False)

    print(f"RFM segment summary written to: {OUTPUT_PATH}")
    print(segment_summary.to_string(index=False))


if __name__ == "__main__":
    main()
