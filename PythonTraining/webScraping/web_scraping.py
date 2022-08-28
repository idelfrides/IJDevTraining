#!/usr/bin/env python3
# -*- conding: utf-8 -*-


from socket import ntohl
from bs4 import BeautifulSoup
import requests

class WebScraper(object):

    def __init__(self) -> None:
        pass


    def scraping_weather(self, url=None, filename=None):
       #  import pdb; pdb.set_trace()

        if not url:
            url = 'https://www.climatempo.com.br/'

        if not filename:
            filename = 'weather_scraper.text'

        html = requests.get(url).text

        # soup = BeautifulSoup(html, 'html.parser')
        soup = BeautifulSoup(html, 'html.parser')

        print(soup.prettify())


        # print(f''' Teste formatacoao: {variavel} outra coisa: {variavel} ''')


        # temperature = soup.find_all("iframe", class_='_block _margin-b-5 -gray')
        # li_list = soup.find("div", class_='mosaic mosaic-provider-jobcards mosaic-provider-hydrated') #  class_='_block _margin-b-5 -gray')
        # # import pdb; pdb.set_trace()
#
        # for li in li_list:
        #     print('-'*80)
        #     print(li)

        # print(temperature.string)

        return




    def scraping_product(self):
        pass
