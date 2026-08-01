import requests
from bs4 import BeautifulSoup


class Scraper:

    def scrape(self, url):

        try:

            headers = {
                "User-Agent": (
                    "Mozilla/5.0 "
                    "(Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 "
                    "(KHTML, like Gecko) "
                    "Chrome/138.0 Safari/537.36"
                )
            }

            response = requests.get(
                url,
                headers=headers,
                timeout=10
            )

            if response.status_code != 200:
                return ""

            soup = BeautifulSoup(response.text, "lxml")

            # Remove unwanted HTML
            for tag in soup(["script", "style", "noscript"]):
                tag.decompose()

            text = soup.get_text(
                separator=" ",
                strip=True
            )

            return text

        except Exception:
            return ""