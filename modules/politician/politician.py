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

    def ideas_timeline(self):
        """
        (Politician) -> dict
        Function for creating a timeline of politician's main ideas.
        """
        pass
