from enum import StrEnum
from typing import Type,TypeVar
from core.excepions import ValidationException


T = TypeVar('T',bound='B')

class BaseEnum(StrEnum):
    @classmethod
    def resolve(cls:Type[T],value:str)->T:
        """"Resolve an enum vale from string."""

        try:
            return cls(value)
        except(KeyError, ValueError):
            raise ValidationException(
                "invalid_enum_value",
                context={'ENUM':cls.__name__,"value":value},
            )

    @classmethod
    def safe_resolve(cls:Type[T],value:str |None)->T|None:
        """"Safely resolve an enm value from a string. """
        if value is None :
            return  None
        return  cls.resolve(value)
    def to_dict(self)->dict:
        return {"name":self.name, "value":self.value}
