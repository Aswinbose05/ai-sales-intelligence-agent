from src.search.scraper import Scraper


class ScraperAgent:

    def __init__(self):
        self.scraper = Scraper()

    def scrape(self, url):

        return self.scraper.scrape(url)