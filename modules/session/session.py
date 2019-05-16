from ..politician.politician import Politician
from ..idea.idea import Idea

from bs4 import BeautifulSoup
import requests

from datetime import date
import re
import os

from .exception.exception import ParseError


class Session:
    """
    Class for representation of Ukrainian Verkhovna Rada session.
    """
    def __init__(self, convocation_no=8, session_date='', announcer=''):
        """
        (Session, str, int, datetime obj, str) -> None
        Initial function for Session object.
        """
        self.__url = ''
        # to Convocation obj
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

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

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

        if text_content:

            filename = 'docs/scripts/skl{}/session_{}.txt'.format(self.convocation_no,
                                                                        self.session_date)
            filename = os.path.relpath(filename, os.getcwd())
            with open(filename, 'w') as write_file:
                write_file.write(''.join(text_content))

            self.__script = filename

        else:
            raise ParseError(self.session_date)

    def set_date(self):
        """
        (Session) -> None
        Parse the session date from the script and set it.
        """
        url = self.__url
        pattern = r'\d{8}'
        session_date = re.search(pattern, url)[0]
        session_date = session_date[:4] + '-' + session_date[4:6] + '-' + session_date[6:]
        session_date = date.fromisoformat(session_date)
        self.session_date = session_date

    def set_announcer(self):
        """
        (Session) -> none
        Parse the session announcer from the script and set it.
        """
        with open(self.__script, 'r') as read_file:
            text = ''.join(read_file.readlines())

        pos = text.find('\n')
        line = text[:pos]
        while "Засідання веде" not in line:
            pos2 = pos
            pos = text.find('\n', pos2 + 1)
            line = text[pos2:pos]
        pattern = r'[А-Я]\.[А-Я]\.[А-Я]+'
        announcer = re.search(pattern, line)

        self.announcer = announcer

    def create_politicians(self):
        """
        (Session) -> list(Politician)
        Creates and updates Politicians objects.
        Assigns them to corresponding convocation.
        """
        politicians = list()
        pattern = r'[А-Я]+\s[А-Я]\.[А-Я]\.'

        with open(self.__script, 'r') as read_file:
            for line in read_file.readlines():
                pol = re.search(pattern, line)
                if pol is not None or 'ГОЛОВУЮЧИЙ' in line:
                    if 'ГОЛОВУЮЧИЙ' in line:
                        pol = self.announcer
                    else:
                        pol = pol[0]
                    politician_obj = Politician(name=pol,
                                                convocation_no=[self.convocation_no])
                    politicians.append(politician_obj)
        return politicians

    def format(self):
        text = ''
        with open(self.__script, 'r') as read_file:
            for line in read_file.readlines():
                new_line = line

                # get rid of time comments
                time_pattern = r'\d{2}:\d{2}:\d{2}'
                if re.search(time_pattern, new_line):
                    re.sub(time_pattern, '', new_line)

                # get rid of comments in brackets
                if '(' and ')' in new_line:
                    pos = new_line.find('(')
                    pos2 = new_line.find(')')
                    new_line = new_line[:pos] + new_line[pos2+1:]
                elif '(' in new_line:
                    pos = new_line.find('(')
                    new_line = new_line[:pos]
                elif ')' in new_line:
                    pos = new_line.find(')')
                    new_line = new_line[pos+1:]

                # get rid of comments in capital letters
                comment_pattern = r'[А-Я]+'
                name_pattern = r'[А-Я]+\s[А-Я]\.[А-Я]\.'
                if re.search(comment_pattern,new_line) and re.search(name_pattern, new_line) is None and\
                        'ГОЛОВУЮЧИЙ' not in new_line:
                    re.sub(comment_pattern, '',new_line)
                text += new_line

            with (self.__script, 'w') as write_file:
                write_file.write(text)

    def to_phrases(self, politician):
        """
        (Session) -> None
        Divide the session script to phrases and analyse each.
        """
        pass

    def phrase_analysis(self, text):
        """
        (Session) -> list(Idea)
        Returns list of Ideas
        """
        ideas = list()
        return ideas
