class ParseError(Exception):
    """
    An exception for pasing error (couldn't access the session script).
    """
    def __init__(self, session):
        """
        (ParseError, str) -> None
        Initial function for ParseError exception.
        """
        self.__session = session

    def __str__(self):
        """
        (ParseError) -> str
        Returns string that describes ParseError exception.
        """
        return '>   ! error parsing {} session...'.format(self.__session)
