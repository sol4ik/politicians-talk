class Idea:
    def __init__(self, name='', politician='', session_date='', context=''):
        self.name = name
        self.politician = politician
        self.session_date = session_date
        self.__context = context

    @classmethod
    def analyze(cls, text):
        """
        Class method for text analysis and creating the Idea objects.
        """
        return cls()
