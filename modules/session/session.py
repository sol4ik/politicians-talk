from ..convocation.convocation import Convocation
from ..politician.politician import Politician
from ..idea.idea import Idea

from bs4 import BeautifulSoup
import requests

from datetime import date
import re
import os

from .exception.exception import ParseError

from .analyser.analyser import Analyser


class Session:
    """
    Class for representation of Ukrainian Verkhovna Rada session.
    """
    def __init__(self, convocation=Convocation(), session_date='', announcer=''):
        """
        (Session, str, int, datetime obj, str) -> None
        Initial function for Session object.
        """
        self.__url = ''
        # to Convocation obj
        self.convocation = convocation

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
        print(self.__url)
        page_response = requests.get(self.__url, timeout=5)
        page_content = BeautifulSoup(page_response.content, "html.parser")

        text_content = []
        for i in range(0, len(page_content.find_all("p"))):
            paragraphs = page_content.find_all("p")[i].text
            text_content.append(paragraphs)

        if text_content:

            filename = 'docs/scripts/skl{}/session_{}.txt'.format(self.convocation.no,
                                                                  self.session_date)
            filename = os.path.relpath(filename, os.getcwd())
            with open(filename, 'w') as write_file:
                write_file.write('\n'.join(text_content))

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
        self.convocation.sessions_calendar.append(session_date)

    def set_announcer(self):
        """
        (Session) -> none
        Parse the session announcer from the script and set it.
        """
        pattern = r'[А-Я]\.[А-Я]\.[А-Я]+'
        with open(self.__script, 'r') as read_file:
            for line in read_file.readlines():
                if "веде" in line or "Веде" in line:
                    announcer = re.search(pattern, line)
                    self.announcer = announcer[0]
                    break

    def create_politicians(self):
        """
        (Session) -> set(Politician)
        Creates and updates Politicians objects.
        Assigns them to corresponding convocation.
        """
        politicians_names = [pol.name for pol in self.convocation.politicians_list]
        politicians = set()
        pattern = r'[А-Я]+\s[А-Я]\.[А-Я]\.'

        with open(self.__script, 'r') as read_file:
            for line in read_file.readlines():
                pol = re.search(pattern, line)
                if pol is not None or 'ГОЛОВУЮЧИЙ' in line:
                    if 'ГОЛОВУЮЧИЙ' in line:
                        pol = self.announcer
                    else:
                        pol = pol[0]
                    if pol not in politicians_names:
                        politician_obj = Politician(name=pol,
                                                    convocation_no=[self.convocation.no])
                        politicians.add(politician_obj)
                        politicians_names.append(pol)

        return politicians

    def format(self):
        to_del_words = ''
        with open(os.path.relpath('modules/session/docs/to_del_words.txt',
                                  os.getcwd()), 'r') as read_file:
            for line in read_file.readlines():
                to_del_words = to_del_words + line[:-1] + ' '

        text = ''
        with open(self.__script, 'r') as read_file:
            for line in read_file.readlines():
                new_line = line

                # get rid of time comments
                time_pattern = r'\d{2}:\d{2}:\d{2}'
                if re.search(time_pattern, new_line):
                    new_line = re.sub(time_pattern, '', new_line)

                # get rid of comments in brackets
                brackets_pattern = r'\([^\(\)]+\)'
                if re.search(brackets_pattern, new_line):
                    new_line = re.sub(brackets_pattern, '', new_line)

                # get rid of comments in capital letters
                comment_pattern = r'[А-Я]+'
                name_pattern = r'[А-Я]+\s[А-Я]\.[А-Я]\.'
                if re.search(comment_pattern, new_line) and re.search(name_pattern, new_line) is None and\
                        'ГОЛОВУЮЧИЙ' not in new_line:
                    re.sub(comment_pattern, '', new_line)

                #  get rid of insignificant words
                words = new_line.split(' ')
                new_line = ''
                for word in words:
                    if word.lower() not in to_del_words:
                        new_line = new_line + ' ' + word

                # merge 'не' with the related word
                new_line = re.sub(' не ', ' не^', new_line)

                if new_line == '\n':
                    continue
                text += new_line

            with open(self.__script, 'w') as write_file:
                write_file.write(text)

    def to_phrases(self):
        """
        (Session) -> None
        Divide the session script to phrases and analyse each.
        """
        phrase = ''
        name_pattern = r'[А-Я]+\s[А-Я]\.[А-Я]\.'

        with open(self.__script, 'r') as read_file:
            for line in read_file.readlines():
                if re.search(name_pattern, line) or 'ГОЛОВУЮЧИЙ' in line:
                    if phrase:
                        if 'ГОЛОВУЮЧИЙ' not in phrase:
                            politician = re.search(name_pattern, phrase)[0]
                            phrase = re.sub(name_pattern, '', phrase)
                        else:
                            politician = self.announcer
                            phrase = re.sub('ГОЛОВУЮЧИЙ', '', phrase)

                        print('_____________________________________')
                        print(phrase)
                        self.__phrase_analysis(politician, phrase)
                    phrase = ''
                    phrase += line

    def __phrase_analysis(self, politician, phrase):
        """
        (Session) -> list(Idea)
        Returns list of Ideas
        """
        politician = self.convocation.search_politician(politician)

        analyser = Analyser(phrase)
        analyser.analyse()
        topics = analyser.topics
        for topic in topics:
            idea = Idea(name=topic, politician=politician, session_date=self.session_date)
            idea.context = phrase

            politician.ideas.append(idea)

