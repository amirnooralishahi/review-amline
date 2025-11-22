class AbstractException(Exception):
    """"
    Abstract Exception class.
    This class should e inherited  by all custom exceptions.
    """

    def __init__(self,detail:str,location:list[str]=None,context:dict=None):
        super().__init__(detail)
        self.detail = detail
        self.location = location
        self.context = context
