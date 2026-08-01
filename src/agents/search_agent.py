from src.search.search_engine import SearchEngine


class SearchAgent:

    def __init__(self):
        self.engine = SearchEngine()

    def search(self, company, query, max_results=3):

        print(f"Searching -> {query}")

        return self.engine.search(
            query,
            max_results=max_results
        )