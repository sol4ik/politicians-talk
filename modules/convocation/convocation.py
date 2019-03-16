class Convocation:
    def __init__(self, no=8, amount=450, json_path=''):
        self.no = no
        self.politicians_amount = amount
        self._politicians_list = None  # property ???
        self._ideas = None

        self._json_file = json_path

    @property
    def politicians_list(self):
        return self._politicians_list

    @politicians_list.setter
    def politicians_list(self, values):
        self._politicians_list = values

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

    def ideas_rating(self):
        """
        Function for creating a rating of the most popular ideas among politicians of current convocation.
        """
        pass
