from ..politician.politician import Politician


class Convocation:
    """
    Class for representation of politicians' Convocation.
    """
    def __init__(self, no=8, amount=450, json_path=''):
        """
        (Convocation, int, int, str) -> None
        Initial function for Convocation object.
        """
        self.no = no
        self.politicians_amount = amount
        self.__politicians_list = list()
        self.__sessions_calendar = list()
        self.__ideas = list()

        self.__ideas_rating = None

        self.__json_file = json_path

    @property
    def politicians_list(self):
        """
        (Convocation) -> list()
        Returns value of Convocation object __politicians_list field.
        """
        return self.__politicians_list

    @politicians_list.setter
    def politicians_list(self, values):
        """
        (Convocation, list()) -> None
        Setter for Convocation object __politicians_list field.
        """
        self.__politicians_list = values

    @property
    def sessions_calendar(self):
        """
        (Convocation) -> list()
        Returns value of Convocation object __sessions_calendar field.
        """
        return self.__sessions_calendar

    @sessions_calendar.setter
    def sessions_calendar(self, value):
        """
        (Convocation, list()) -> None
        Setter for Convocation object __sessions_calendar field.
        """
        self.__sessions_calendar = value

    @property
    def ideas(self):
        """
        (Convocation) -> list()
        Returns value of Convocation object __ideas field.
        """
        return self.__ideas

    @ideas.setter
    def ideas(self, values):
        """
        (Convocation, list()) -> None
        Setter for Convocation object __ideas field.
        """
        self.__ideas = values

    @property
    def json_file(self):
        """
        (Convocation) -> str
        Returns value of Convocation object __json_file field.
        """
        return self.__json_file

    @json_file.setter
    def json_file(self, value):
        """
        (Convocation, str) -> None
        Setter for Convocation object __json_file field.
        """
        self.__json_file = value

    def __str__(self):
        """
        (Convocation) -> str
        Returns string that describes Convocation object.
        """
        return "Convocation #{}".format(self.no)

    def __contains__(self, politician):
        """
        (Convocation, Politician) -> bool
        Checks if Politician is in Convocation.
        """
        return politician.name in [pol.name for pol in self.__politicians_list]

    def search_politician(self, name):
        """
        (Convocation, str) -> Politician
        Find Politician by name in the Convocation.__politicians_list.
        """
        for politician in self.__politicians_list:
            if politician.name == name:
                return politician

    def politician_calendar(self, politician):
        """
        (Convocation, Politician) -> list(list)
        Function for creating a calendar of politician's presence on the sessions.
        """
        pass

    @property
    def ideas_rating(self):
        """
        (Convocation) -> dict()
        Returns value of Convocation __ideas_rating field.
        """
        return self.__ideas_rating

    @ideas_rating.setter
    def ideas_rating(self, value=None):
        """
        (Convocation) -> dict
        Function for creating a rating of the most popular ideas among politicians of current convocation.
        """
        counter = dict()
        for idea in self.__ideas:
            if idea.name in counter:
                counter[idea.name] += 1
            else:
                counter[idea.name] = 1

        # 1: 'РФ'
        # 2: 'газ'
        rating = dict()
        max = 0
        max_key = 0
        count = 1
        while len(rating) != len(counter):
            for key in counter:
                if counter[key] > max:
                    max = counter[key]
                    max_key = key
            rating[max_key] = count
            count += 1
            counter[max_key] = 0
        return rating
