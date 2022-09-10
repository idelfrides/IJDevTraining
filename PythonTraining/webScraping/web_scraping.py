#!/usr/bin/env python3
# -*- conding: utf-8 -*-

"""### Web scraping module"""

# from bs4 import BeautifulSoup
import requests
from PythonTraining.libs import lib_manager


class WebScraper():
    """# Web scraping class"""

    def __init__(self) -> None:
        pass

    def scraping_weather(self, url: str = "https://www.climatempo.com.br/", filename: str = "weather_scraper.html") -> None:
        """# Weather scraping 

        Args:
            url (_type_, optional): _description_. Defaults to "https://www.climatempo.com.br/".
            filename (str, optional): _description_. Defaults to "weather_scraper.text".
        """

        html_ = requests.get(url).text
        # soup = BeautifulSoup(html, 'html.parser')
        # soup = BeautifulSoup(html_, 'html.parser')

        full_path = "/".join([lib_manager.get_cwdir(), "utils", filename])

        with open(file=full_path, mode="w", encoding="utf-8") as file_:
            file_.write(html_)

        # print(soup.prettify())
        # print(f''' Teste formatacoao: {variavel} outra coisa: {variavel} ''')
        # temperature = soup.find_all("iframe", class_='_block _margin-b-5 -gray')
        # li_list = soup.find("div", class_='mosaic mosaic-provider-jobcards mosaic-provider-hydrated') #  class_='_block _margin-b-5 -gray')
        # # import pdb; pdb.set_trace()

        # for li in li_list:
        #     print('-'*80)
        #     print(li)

        # print(temperature.string)

        return

    def scraping_product(self) -> None:
        """# Scrapoing product"""
        print("Scrapoing product")
