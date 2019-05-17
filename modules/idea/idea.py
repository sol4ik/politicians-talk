class Idea:
    """
    Class for representation of political Idea.
    """
    def __init__(self, name='', politician='', session_date=''):
        """
        (Idea, str, Politician, str) -> None
        Initial function for Idea object.
        """
        self.name = name
        self.politician = politician
        self.session_date = session_date
        self.__context = None

    @property
    def context(self):
        """
        (Idea) -> str
        Returns Idea object __context field value.
        """
        return self.__context

    @context.setter
    def context(self, value):
        """
        (Idea, list()) -> None
        Setter for Idea object __context field.
        """
        self.__context = value

    def __str__(self):
        """
        (Idea) -> str
        Returns string that describes Idea object.
        """
        return self.name
