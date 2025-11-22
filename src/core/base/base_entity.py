from abc import ABC
from typing import Dict,Generic , Type ,TypeVar

from core.base.snowflake_id_generator import SnowflakeIDGenerator


T=TypeVar('T',bound='BaseEntity')


class BaseEntity(Generic[T],ABC):
    id_generator = SnowflakeIDGenerator()


    def dumps(self,**kwargs):
        raise NotImplementedError


    @classmethod
    def loads(cls:Type[T],data:Dict) -> T :
        raise NotImplementedError


    @classmethod
    def entity_name(cls)->str:
        return cls.__name__

    @property
    def next_id(self)->int:
        return  self.id_generator.get_next_id()


    @classmethod
    def get_next_id(cls):
        return  cls.id_generator.get_next_id()
