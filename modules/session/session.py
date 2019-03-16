from bs4 import BeautifulSoup
import requests

import datetime


class Session:
    """
    Class for representation of Ukrainian Verkhovna Rada session.
    """
    def __init__(self, url='', convocation_no=8, date=datetime.datetime.now(), announcer=''):
        """
        Initial function for Session object.
        """
        self.url = url
        self.convocation_no = convocation_no

        self.date = date
        self.announcer = announcer
        self._stenogram = None

    @property
    def stenogram(self):
        return self._stenogram

    @stenogram.setter
    def stenogram(self, text):
        self._stenogram = text

    def parse_html(self):
        page_response = requests.get(self.url, timeout=1)
        page_content = BeautifulSoup(page_response.content, "html.parser")

        text_content = []
        for i in range(0, len(page_content.find_all("p", attrs={"align": None}))):
            paragraphs = page_content.find_all("p", attrs={"align": None})[i].text
            text_content.append(paragraphs)

        self.stenogram(text_content)

    def parse_text(self, stenogram_text):
        lst = []
        return lst
