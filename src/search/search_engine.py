from ddgs import DDGS


class SearchEngine:

    def __init__(self):
        self.ddgs = DDGS()

    def search(self, query, max_results=5):

        try:

            results = self.ddgs.text(
                query,
                max_results=max_results
            )

            return list(results)

        except Exception as e:

            print(e)

            return []