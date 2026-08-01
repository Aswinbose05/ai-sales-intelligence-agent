"""
Intent Scoring Agent

Ranks companies based on extracted buying intent signals.
"""

from collections import defaultdict
import os
import pandas as pd

from src.database.signal_db import SignalDatabase


class ScoringAgent:

    def __init__(self):

        self.db = SignalDatabase()

        # Buying intent weights
        self.SCORES = {
            "Funding": 40,
            "Expansion": 30,
            "Hiring": 25,
            "Technology Adoption": 20,
            "Leadership Change": 15,
            "Customer Complaints": 10,
            "Shipping Problems": 8,
            "Returns Problems": 5,
        }

    def rank_companies(self):

        rows = self.db.get_all()

        companies = defaultdict(lambda: {
            "score": 0,
            "signals": set(),
            "confidence_sum": 0.0,
            "signal_count": 0
        })

        for row in rows:

            company = row[1]
            signal = row[2]

            try:
                confidence = float(row[4])
            except (TypeError, ValueError):
                confidence = 0.0

            # Ignore unknown signals
            if signal not in self.SCORES:
                continue

            # Score each signal only once
            if signal not in companies[company]["signals"]:

                companies[company]["signals"].add(signal)
                companies[company]["score"] += self.SCORES[signal]

            companies[company]["confidence_sum"] += confidence
            companies[company]["signal_count"] += 1

        ranked = []

        for company, data in companies.items():

            avg_confidence = (
                round(
                    data["confidence_sum"] / data["signal_count"],
                    2
                )
                if data["signal_count"] > 0
                else 0
            )

            ranked.append({

                "company": company,

                "score": data["score"],

                "confidence": avg_confidence,

                "signals": sorted(list(data["signals"]))

            })

        ranked.sort(

            key=lambda x: (
                x["score"],
                x["confidence"]
            ),

            reverse=True

        )

        return ranked

    def print_rankings(self):

        ranked = self.rank_companies()

        print("\n" + "=" * 90)
        print("TOP RANKED COMPANIES")
        print("=" * 90)

        if not ranked:
            print("No ranked companies found.")
            return ranked

        for i, company in enumerate(ranked, start=1):

            print(f"\n{i}. {company['company']}")
            print(f"Score       : {company['score']}")
            print(f"Confidence  : {company['confidence']}")
            print("Signals:")

            for signal in company["signals"]:
                print(f"   • {signal}")

        return ranked

    def export_csv(self):

        ranked = self.rank_companies()

        os.makedirs("outputs", exist_ok=True)

        rows = []

        for company in ranked:

            rows.append({

                "Company": company["company"],

                "Score": company["score"],

                "Confidence": company["confidence"],

                "Signals": ", ".join(company["signals"])

            })

        df = pd.DataFrame(rows)

        df.to_csv(
            "outputs/ranked_companies.csv",
            index=False
        )

        print("\n✅ Saved : outputs/ranked_companies.csv")

    def get_top_companies(self, top_n=5):

        return self.rank_companies()[:top_n]

    def get_company_details(self, company_name):

        rows = self.db.get_all()

        details = []
        seen = set()

        for row in rows:

            if row[1] != company_name:
                continue

            signal = row[2]
            evidence = row[3]

            key = (signal, evidence)

            if key in seen:
                continue

            seen.add(key)

            try:
                confidence = float(row[4])
            except (TypeError, ValueError):
                confidence = 0.0

            details.append({

                "signal": signal,

                "evidence": evidence,

                "confidence": confidence,

                "reason": row[5] if len(row) > 5 else ""

            })

        # Highest-confidence evidence first
        details.sort(
            key=lambda x: x["confidence"],
            reverse=True
        )

        return details

    def close(self):

        self.db.close()


if __name__ == "__main__":

    scorer = ScoringAgent()

    scorer.print_rankings()

    scorer.export_csv()

    scorer.close()