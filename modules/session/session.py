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
        (Session, str, int, datetime obj, str) -> None
        Initial function for Session object.
        """
        self.__url = url
        self.convocation_no = convocation_no

        self.session_date = session_date
        self.announcer = announcer
        self.__script = None

    def __str__(self):
        """
        (Session) -> str
        Returns string describing the Session object.
        """
        txt = ''

        return txt

    def get_url(self):
        """
        (Session) -> str
        Returns Session object url.
        """
        return self.__url

    @property
    def script(self):
        """
        (Session) -> str
        Returns Session object script text.
        """
        return self.__script

    @script.setter
    def script(self, text):
        """
        (Session, str) -> None
        Setter for a Session __script field.
        """
        self.__script = text

    def parse_html(self):
        """
        (Session) -> None
        Parse the script text from the API.
        """
        page_response = requests.get(self.__url, timeout=1)
        page_content = BeautifulSoup(page_response.content, "html.parser")

        text_content = []
        for i in range(0, len(page_content.find_all("p", attrs={"align": None}))):
            paragraphs = page_content.find_all("p", attrs={"align": None})[i].text
            text_content.append(paragraphs)

        self.script(text_content)

    def set_date(self):
        """
        (Session) -> None
        Parse the session date from the script and set it.
        """
        url = self.__url
        pattern = r'\d{8}'
        session_date = re.search(pattern, url)
        session_date = session_date[:4] + '-' + session_date[4:6] + '-' + session_date[6:]
        session_date = date.fromisoformat(session_date)
        self.session_date = session_date

    def set_announcer(self):
        """
        (Session) -> none
        Parse the session announcer from the script and set it.
        """
        pass

    def parse_text(self):
        """
        (Session) -> none
        Parse the session speech text from the script and set it.
        """
        pass

    def analyze(self):
        """
        (Session) -> none
        Analyze the script text.
        """
        pass

    def phrase_analysis(self):
        """

        :return:
        """
        pass
