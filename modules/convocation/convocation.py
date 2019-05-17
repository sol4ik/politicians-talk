from ..politician.politician import Politician


class Convocation:
    def __init__(self, no=8, amount=450, json_path=''):
        self.no = no
        self.politicians_amount = amount
        self.__politicians_list = list()
        self.__sessions_calendar = list()
        self.__ideas = None

        self.__json_file = json_path

    @property
    def politicians_list(self):
        return self.__politicians_list

    @politicians_list.setter
    def politicians_list(self, values):
        self.__politicians_list = values

    @property
    def sessions_calendar(self):
        return self.__sessions_calendar

    @sessions_calendar.setter
    def sessions_calendar(self, value):
        self.__sessions_calendar = value

    @property
    def ideas(self):
        return self.__ideas

    @ideas.setter
    def ideas(self, values):
        self.__ideas = values

    @property
    def json_file(self):
        return self.__json_file

    @json_file.setter
    def json_file(self, value):
        self.__json_file = value

    def __str__(self):
        """
        (Convocation) -> str
        Returns string that describes Convocation object.
        """
        return self.no

    def __contains__(self, politician):
        """
        (Convocation, Politician) -> bool
        Checks if Politician is in Convocarion.
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

    def ideas_rating(self):
        """
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
