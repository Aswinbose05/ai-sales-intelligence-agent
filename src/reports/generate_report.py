"""
Generate Final Sales Intelligence Report
"""

import os
import pandas as pd

from src.ranking.scoring_agent import ScoringAgent


def generate_report():

    scorer = ScoringAgent()

    ranked = scorer.rank_companies()

    os.makedirs("outputs", exist_ok=True)

    rows = []

    for company in ranked:

        rows.append({
            "Company": company["company"],
            "Intent Score": company["score"],
            "Confidence": company["confidence"],
            "Signals": ", ".join(company["signals"])
        })

    df = pd.DataFrame(rows)

    output_path = "outputs/final_report.csv"

    df.to_csv(output_path, index=False)

    print(df)

    print(f"\n✅ Report saved to: {output_path}")

    scorer.close()


if __name__ == "__main__":
    generate_report()