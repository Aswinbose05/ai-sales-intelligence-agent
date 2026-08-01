"""
Process all companies in companies.csv
"""

import pandas as pd

from src.pipeline.process_company import process_company
from src.database.signal_db import SignalDatabase


def load_companies():

    df = pd.read_csv("data/companies.csv")

    return df["company"].tolist()


if __name__ == "__main__":

    # Clean previous signals
    db = SignalDatabase()

    try:
        print("Cleaning previous signals...")
        db.delete_all()
    finally:
        db.close()

    companies = load_companies()

    print("=" * 80)
    print(f"Found {len(companies)} Companies")
    print("=" * 80)

    total_signals = 0

    for index, company in enumerate(companies, start=1):

        print(f"\n[{index}/{len(companies)}] {company}")

        try:

            signals = process_company(company)

            total_signals += len(signals)

            print(f"Signals Found : {len(signals)}")

        except Exception as e:

            print("ERROR :", e)

    print("\n")
    print("=" * 80)
    print("PROCESS COMPLETED")
    print("=" * 80)

    print("Total Signals :", total_signals)

    # Reopen database to check final row count
    db = SignalDatabase()

    try:
        print("Database Rows :", db.count())
    finally:
        db.close()