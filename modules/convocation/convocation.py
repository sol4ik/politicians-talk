class Convocation:
    def __init__(self, number=8, amount=450):
        self.number = number
        self._politicians_amount = amount
        self._politicians_list = None
        self._ideas = None

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

    # ???
    def to_json(self):
        pass
