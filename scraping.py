# !/bin/usr/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re

class RequestsAndBS4Gateway:
    def get_and_parse(self, url):
        soup_content = []
        req = requests.get(url)
        req.encoding = "utf-8"
        soup_content = BeautifulSoup(req.text, "lxml")
        return soup_content

    tag1 = soup_content.find("h2" , {"class":"title"})
    tag2 = soup_content.find_all("div")
    tag3 = tag2.find_all("a", href=re.compile("/photo/"))

    title = ""
    title = tag1.text
    url_list = {format(i["href"]) for i in tag3}


    tag = soup_content.find_all("div",\
          {"class":"ProductProcedure__items"})[1]
    start_price = tag.find_all("dd",\
          {"class":"ProductDetail__description"})[4]

    tag = soup.find_all('a',href=re.compile(".jpg"))
    url_list = {'http://easelfamily.toyao.net{}'\
                .format(i["href"]) for i in tag}
