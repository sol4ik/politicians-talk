class Politician:
    """
    Class for representing politician of Ukrainian Verkhovna Rada.
    """
    def __init__(self, name='', skl=[]):
        self.name = name
        self.skl = skl
        self._presence = None  # ? or []
        self._ideas = None  # ? or []

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

    # ???
    def to_json(self):
        pass
