class Idea:
    def __init__(self, name='', politician='', session_date=''):
        self.name = name
        self.politician = politician
        self.session_date = session_date
        self.__context = None

    @property
    def context(self):
        return self.__context

    @context.setter
    def context(self, value):
        self.__context = value

    def __str__(self):
        """
        (Idea) -> str
        Returns string that describes Idea object.
        """
        return self.name
