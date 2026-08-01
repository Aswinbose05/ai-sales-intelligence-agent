from src.agents.search_agent import SearchAgent
from src.agents.scraper_agent import ScraperAgent
from src.agents.signal_agent import SignalAgent
from src.search.page_classifier import PageClassifier
from src.database.signal_db import SignalDatabase

search_agent = SearchAgent()
scraper_agent = ScraperAgent()
signal_agent = SignalAgent()
classifier = PageClassifier()
db = SignalDatabase()


SEARCH_QUERIES = {
    "Hiring": "{} careers logistics customer experience jobs",
    "Funding": "{} funding investment expansion news",
    "Complaints": "{} reddit trustpilot shipping complaints",
    "Technology": "{} AfterShip Loop Returns Redo Onward",
    "Leadership": "{} CTO CIO VP Leadership Executive"
}


IGNORE_WORDS = [
    "return policy",
    "returns",
    "refund",
    "privacy",
    "terms",
    "faq",
    "help center",
    "shipping policy",
]


SKIP_DOMAINS = [
    "linkedin.com",
    "indeed.com",
    "glassdoor.com",
    "ziprecruiter.com",
    "simplyhired.com",
]


def process_company(company):

    print("\n" + "=" * 80)
    print(f"Processing : {company}")
    print("=" * 80)

    all_signals = []

    for query_type, template in SEARCH_QUERIES.items():

        query = template.format(company)

        print(f"\nSearching [{query_type}]")
        print(query)

        try:
            results = search_agent.search(
                company,
                query,
                max_results=1
            )

        except Exception as e:
            print("Search Error:", e)
            continue

        if not results:
            continue

        for result in results:

            title = result.get("title", "")
            url = result.get("href", "")

            print("-" * 70)
            print(title)
            print(url)

            # Skip unwanted pages
            if any(word in title.lower() for word in IGNORE_WORDS):
                print("Skipped : Policy Page")
                continue

            # Skip slow websites
            if any(domain in url.lower() for domain in SKIP_DOMAINS):
                print("Skipped : Slow Domain")
                continue

            page_type = classifier.classify(title, url)

            print("Page Type :", page_type)

            if page_type == "Unknown":
                print("Skipped : Unknown")
                continue

            text = scraper_agent.scrape(url)

            if len(text) < 300:
                print("Skipped : Not enough content")
                continue

            try:

                signals = signal_agent.analyze(text)

            except Exception as e:

                print("LLM Error:", e)
                continue

            if not signals:
                print("No signals detected")
                continue

            for signal in signals:

                signal["company"] = company
                signal["query_type"] = query_type
                signal["page_type"] = page_type
                signal["title"] = title
                signal["url"] = url

                all_signals.append(signal)

                db.insert(signal)

                print("Saved ->", signal["signal_type"])

    return all_signals


if __name__ == "__main__":

    company = "Vuori"

    signals = process_company(company)

    db.close()

    print("\n")
    print("=" * 80)
    print("FINAL SIGNALS")
    print("=" * 80)

    for signal in signals:
        print(signal)