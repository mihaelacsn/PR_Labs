from bs4 import BeautifulSoup
import requests

class WebScraper:
    def __init__(self):
        self.item_urls = []  # Renamed variable
        self.base_url = "https://999.md/ro/list/real-estate/apartments-and-rooms?o_30_241=894&applied=1&eo=12900&eo=12912&eo=12885&eo=13859&ef=32&ef=33&o_33_1=776"  # Renamed variable
        self.max_page_number = 15
        self.filename = "urls.txt"

    def start_scraping(self, page_number="1"):
        return self.parse_page(page_number)

    def parse_page(self, page_number):
        url = self.base_url + f"&page={page_number}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        item_links = [a["href"] for a in soup.select(".ads-list-photo-item-title a")]

        self.item_urls.extend(item_links)

        if int(page_number) + 1 <= self.max_page_number:
            return self.parse_page(str(int(page_number) + 1))
        else:
            return self.save_items()

    def save_items(self):
        clean_list = ["https://999.md" + link for link in self.item_urls if "/booster" not in link]

        with open(self.filename, "w") as file:
            for link in clean_list:
                file.write(link + "\n")

        return {"links": clean_list}

def main():
    scraper = WebScraper()
    scraper.start_scraping()

if __name__ == "__main__":
    main()
