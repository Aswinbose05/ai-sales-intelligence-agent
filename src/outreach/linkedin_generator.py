"""
LinkedIn Message Generator
"""

import os

from src.ranking.scoring_agent import ScoringAgent
from src.outreach.templates import SIGNAL_TEXT


class LinkedInGenerator:

    def __init__(self):

        self.scorer = ScoringAgent()

    def generate_message(self, company):

        observations = []

        for signal in company["signals"]:

            if signal in SIGNAL_TEXT:
                observations.append(SIGNAL_TEXT[signal])

        observation_text = ", ".join(observations)

        return f"""
Hi Team,

I was researching fast-growing eCommerce brands and came across {company['company']}.

I noticed that your company {observation_text}.

As brands grow, delivery visibility, returns management, and post-purchase communication become increasingly important.

ClickPost helps eCommerce brands automate shipping operations while improving customer experience.

I'd love to connect and learn how your logistics team is approaching these challenges.

Best,
Aswin
""".strip()

    def generate_all(self):

        companies = self.scorer.get_top_companies(5)

        os.makedirs("outputs", exist_ok=True)

        with open(
            "outputs/linkedin_messages.md",
            "w",
            encoding="utf-8"
        ) as file:

            file.write("# LinkedIn Outreach Messages\n\n")

            for company in companies:

                file.write(f"## {company['company']}\n\n")

                file.write(self.generate_message(company))

                file.write("\n\n---\n\n")

        print("✅ Saved outputs/linkedin_messages.md")

        self.scorer.close()


if __name__ == "__main__":

    generator = LinkedInGenerator()

    generator.generate_all()