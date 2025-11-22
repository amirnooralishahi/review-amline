from core.base.abstract_exception import AbstractException
from core.translates import auth_trans, perm_trans


class BadRequestException(AbstractException):
    """Raised for a ad request that cannot e processed due to client error."""


class ValidationException(BadRequestException):
    """"Raised when a provided value does not meet the expected criteria."""


class AuthenticationException(AbstractException):
    """"Raised when authentication is required to access a resource."""

    def __init__(self,
                 detail: str = auth_trans.unautorized_access,
                 location: list[str] = None,
                 context: dict = None,

                 ):
        super().__init__(detail,location,context)


class PermissionException(AbstractException):
        def __init__(self,
                     detail:str=perm_trans.user_does_not_have_enough_permission,
                     location:list[str]=None ,
                     context:dict=None )->None:
            super().__init__(detail,location,context)
            """"Raised when a user does not have permission to perform an action."""



class NotFoundException(AbstractException):#404
    """"Raised when a requested resource is not found"""


class ConflictException(AbstractException):#40
    """"Raised when a resource conflict occurs."""

class DataIntegrityException(ConflictException):
    """Raised when there is a data integrity issue."""

class ProcessingException(AbstractException): #422
    """"Raised when an operation cannot e processed."""

class ServerException(AbstractException): #500
    """Raised when a requested method or operation is not implemented."""


class NotImplementedException(AbstractException):#501
    """Raised when a requested method or operation is not implemented."""

class ServiceUnavailableException(AbstractException): #503
    """Raised when the server is currently unable to handle the request."""
