from bs4 import BeautifulSoup
from typing import Callable

from real_estate_hunter.selenium import start_chrome_driver


def get_web_parser(marketplace_code: str) -> Callable:
    web_parsers = {
        "sreality": web_parser_sreality,
    }

    return web_parsers[marketplace_code]


def web_parser_sreality(starting_source):
    source = starting_source
    driver = start_chrome_driver()
    stats = {
        "properties_amount": 0,
        "properties_with_price": 0,
        "properties_without_price": 0,
        "properties_price_together": 0
    }

    while True:
        driver.get(source)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        source_results = soup.find_all("div", class_="property ng-scope")
        stats["properties_amount"] += len(source_results)

        for result in source_results:
            # property_size = result.find("a", class_="title").attrs["href"].split("/")[4]
            property_price = result.find("span", class_="norm-price").text.replace("\xa0", "").replace("Kč", "")
            try:
                stats["properties_price_together"] += int(property_price)
                stats["properties_with_price"] += 1
            except ValueError:
                stats["properties_without_price"] += 1

        paging_buttons = soup.findAll("li", class_="paging-item ng-scope")

        if paging_buttons:
            active_pagging_button = soup.find(class_="btn-paging ng-binding active").parent
            next_paging_button = active_pagging_button.find_next_sibling("li", class_="paging-item ng-scope")

            if next_paging_button:
                next_source_path = next_paging_button.find("a").attrs["href"]
                source = "https://www.sreality.cz" + next_source_path

            else:
                break
        else:
            break

    driver.quit()
    return stats["properties_amount"]

