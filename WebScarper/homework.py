import requests
from bs4 import BeautifulSoup
import json

def scrape_ad_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    ad_info = {
        "page_title": soup.select_one("header.adPage__header h1").text.strip(),
        "price": soup.select_one("span.adPage__content__price-feature__prices__price__value").text.strip(),
        "update_time": soup.select_one("div.adPage__aside__stats__date").text.strip(),
        "balcony": soup.select_one("span.adPage__content__features__value").text.strip(),
    }

    return ad_info

urls = ["https://999.md/ro/74323770"]
FILENAME = "info.json"
ad_info_list = []

for url in urls:
    ad_info = scrape_ad_info(url)
    ad_info_list.append(ad_info)

with open(FILENAME, "w", encoding="utf-8") as file:
    json.dump(ad_info_list, file, indent=4, ensure_ascii=False)
