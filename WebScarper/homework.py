from bs4 import BeautifulSoup
import json
import requests

def scrape_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    item = {
        "page_title": soup.select_one("header.adPage__header h1").text.strip(),
        "price": soup.select_one("span.adPage__content__price-feature__prices__price__value").text.strip(),
        "update_time": soup.select_one("div.adPage__aside__stats__date").text.strip(),
        "balcony": soup.select_one("span.adPage__content__features__value").text.strip(),
   
    }

    CHARACTERISTICS.append(item)

urls = ["https://999.md/ro/74323770"]


FILENAME = "info.json"
CHARACTERISTICS = []

for url in urls:
    scrape_url(url)

with open(FILENAME, "w", encoding="utf-8") as file:
    json.dump(CHARACTERISTICS, file, indent=4, ensure_ascii=False)
