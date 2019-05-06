from bs4 import BeautifulSoup
import requests

from datetime import date, datetime
import re


class Session:
    """
    Class for representation of Ukrainian Verkhovna Rada session.
    """
    def __init__(self, url='', convocation_no=8, session_date=datetime.now(), announcer=''):
        """
        Initial function for Session object.
        """
        self.__url = url
        self.convocation_no = convocation_no

        self.session_date = session_date
        self.announcer = announcer
        self.__stenogram = None

    def __str__(self):
        pass

    @property
    def stenogram(self):
        return self.__stenogram

    @stenogram.setter
    def stenogram(self, text):
        self.__stenogram = text

    def set_date(self):
        url = self.url
        pattern = r'\d{8}'
        session_date = re.search(pattern, url)
        session_date = session_date[:4] + '-' + session_date[4:6] + '-' + session_date[6:]
        session_date = date.fromisoformat(session_date)
        self.session_date = session_date

    @staticmethod
    def parse_html(self):
        page_response = requests.get(self.url, timeout=1)
        page_content = BeautifulSoup(page_response.content, "html.parser")

        text_content = []
        for i in range(0, len(page_content.find_all("p", attrs={"align": None}))):
            paragraphs = page_content.find_all("p", attrs={"align": None})[i].text
            text_content.append(paragraphs)

        self.stenogram(text_content)

    def set_announcer(self):
        pass

    def get_url(self):
        pass

    def parse_text(self):
        return True

    def analyze(self):
        pass

    def phrase_analysis(self):
        pass
