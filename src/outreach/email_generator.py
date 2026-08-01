"""
Cold Email Generator
"""

import os

from src.ranking.scoring_agent import ScoringAgent


class EmailGenerator:

    def __init__(self):

        self.scorer = ScoringAgent()

    def generate_email(self, company):

        details = self.scorer.get_company_details(company["company"])

        evidence = []

        for item in details[:3]:
            evidence.append(f"• {item['evidence']}")

        evidence_text = "\n".join(evidence)

        subject = f"Helping {company['company']} Scale Logistics"

        body = f"""
Subject: {subject}

Hi Team,

I recently came across {company['company']} while researching growing eCommerce brands.

A few things stood out:

{evidence_text}

As brands grow, shipping operations become increasingly complex.

ClickPost helps brands improve:

• Delivery visibility
• Shipping automation
• Returns management
• Customer communication

I'd love to schedule a short call to understand your logistics strategy and explore whether ClickPost could help.

Best Regards,

Aswin
""".strip()

        return body

    def generate_all(self):

        companies = self.scorer.get_top_companies(5)

        os.makedirs("outputs", exist_ok=True)

        with open(
            "outputs/emails.md",
            "w",
            encoding="utf-8"
        ) as f:

            f.write("# Cold Emails\n\n")

            for company in companies:

                f.write(f"## {company['company']}\n\n")

                f.write(self.generate_email(company))

                f.write("\n\n---\n\n")

        print("✅ Saved outputs/emails.md")

        self.scorer.close()


if __name__ == "__main__":

    generator = EmailGenerator()

    generator.generate_all()