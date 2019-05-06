import json


class Politician:
    """
    Class for representing politician of Ukrainian Verkhovna Rada.
    """
    def __init__(self, name='', convocation_no=[], json_path=''):
        self.name = name
        self.convocation_no = convocation_no
        self._presence = None
        self._ideas = None

        self._json_file = json_path

    @property
    def presence(self):
        return self._presence

    @presence.setter
    def presence(self, values):
        self._presence = values

    @property
    def ideas(self):
        return self._ideas

    @ideas.setter
    def ideas(self, values):
        self._ideas = values

    @property
    def json_file(self):
        return self._json_file

    @json_file.setter
    def json_file(self, value):
        self._json_file = value

    def __str__(self):
        pass

    def ideas_timeline(self):
        """
        (Politician) -> dict
        Function for creating a timeline of politician's main ideas.
        """
        pass

    def ideas_rating(self, n):
        """
        (Politician) -> dict
        Function for creating a rating of top [n] politician's main ideas.
        """
        pass

    def presence_calendar(self):
        """
        (Politician) -> list(list)
        Function for creating a calendar of politician's presence on the sessions.
        """
        pass

    def to_json(self):
        """
        (Politician) -> .json file
        Function for writing all the data on Politician object to a .json file.
        """
        pass

    @classmethod
    def from_json(cls, file_path):
        """
        (str) -> Politician
        Function for creating a Politician object with the data from the .json file.
        """
        pass
