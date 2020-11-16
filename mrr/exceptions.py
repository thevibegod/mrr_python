class ApiCallException(Exception):
    """
    API Call was unsuccessful.
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
