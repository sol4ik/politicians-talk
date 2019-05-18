from ..idea.idea import Idea

import json


class Politician:
    """
    Class for representing politician of Ukrainian Verkhovna Rada.
    """
    def __init__(self, name='', convocation_no=[], json_path=''):
        """
        (Politician, str, list(int), str) -> None
        Initial function for the Politician object.
        """
        self.name = name
        self.convocation_no = convocation_no

        self.__presence = list()
        self.__ideas = list()

        self.__ideas_timeline = None
        self.__ideas_rating = None

        self.__json_file = json_path

    @property
    def presence(self):
        """
        (Politician) -> list(str)
        Returns list of dates when Politician was present at the sessions.
        """
        return self.__presence

    @presence.setter
    def presence(self, values):
        """
        (Politician, list()) -> None
        Setter for Politician object __presence field.
        """
        self.__presence = values

    @property
    def ideas(self):
        """
        (Politician) -> list(str)
        Returns list of Politician's ideas.
        """
        return self.__ideas

    @ideas.setter
    def ideas(self, values):
        """
        (Politician, list()) -> None
        Setter for Politician object __ideas field.
        """
        self.__ideas = values

    @property
    def json_file(self):
        """
        (Politician) -> list(str)
        Returns path to .json file on Politician object.
        """
        return self.__json_file

    @json_file.setter
    def json_file(self, value):
        """
        (Politician, list()) -> None
        Setter for Politician object __json_file field.
        """
        self.__json_file = value

    def __str__(self):
        """
        (Politician) -> str
        Returns string that describes Politician object.
        """
        return self.name

    @property
    def ideas_timeline(self):
        """
        (Politician, int) -> dict
        Returns value of Politician __ideas_timeline field.
        """
        return self.__ideas_timeline

    @ideas_timeline.setter
    def ideas_timeline(self, value=None):
        """
        (Politician) -> dict
        Function for creating a timeline of politician's main ideas.
        """
        timeline = dict()
        # '01.04.2019' : ['війна', 'Крим', 'газ']
        for idea in self.__ideas:
            if idea.session_date in timeline:
                timeline[idea.session_date].append(idea)
            else:
                timeline[idea.session_date] = [idea]
        self.__ideas_timeline = timeline

    @property
    def ideas_rating(self):
        """
        (Politician, int) -> dict
        Returns value of Politican __ideas_rating field.
        """
        return self.__ideas_rating

    @ideas_rating.setter
    def ideas_rating(self, n):
        """
        (Politician, int) -> None
        Function for creating a rating of top [n] politician's main ideas.
        """
        counter = dict()
        # 'РФ' : 2
        # 'газ': 1
        for idea in self.__ideas:
            if idea.name in counter:
                counter[idea.name] += 1
            else:
                counter[idea.name] = 1

        # get top n
        # 1: 'РФ'
        # 2: 'газ'
        top_n = dict()
        max = 0
        max_key = 0
        count = 1
        while len(top_n) != n:
            for key in counter:
                if counter[key] > max:
                    max = counter[key]
                    max_key = key
            top_n[max_key] = count
            count += 1
            counter[max_key] = 0
        self.__ideas_rating = top_n

    def to_json(self):
        """
        (Politician) -> .json file
        Function for writing all the data on Politician object to a .json file.
        """
        data = dict()
        data["politician"] = {
            "name": self.name,
            "convocation_no": ', '.join(self.convocation_no),
            "presence": self.__presence,
            "ideas": ', '.join([str(idea) for idea in self.__ideas])
        }
        with open(self.json_file, 'w') as write_file:
            json.dump(data, write_file)

    @classmethod
    def from_json(cls, file_path):
        """
        (str) -> Politician
        Function for creating a Politician object with the data from the .json file.
        """
        new_pol = Politician()

        with open(file_path) as read_file:
            data = json.load(read_file)

        new_pol.name = data["politician"]["name"]
        new_pol.convocation_no = data["politician"]["convocation_no"]
        new_pol.presence = data["politician"]["presence"]

        new_pol.ideas = []
        for el in data["politician"]["ideas"].split(','):
            idea = Idea(name=el)
            new_pol.ideas.append(idea)

        new_pol.json_file = file_path
