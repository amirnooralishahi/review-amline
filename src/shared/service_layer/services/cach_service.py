from abc import ABC, abstractmethod
import json
from datetime import timedelta
from typing import Optional
import redis
from redis import Redis
from core import settings
from core.excepions import ValidationException
from core.logger import Logger
from core.translates import validation_trans
from core.types import RedisConfig

logger = Logger('chach-service')


class CacheService(ABC):
    def pop(self, key: str) -> str | None:
        value = self.get(key)
        if value:
            self.delete(key)
        return value

    @abstractmethod
    def get(self, key: str) -> str | None:
        ...

    @abstractmethod
    def set(self, key: str, value: str, exp: timedelta) -> None:
        ...

    @abstractmethod
    def delete(self, key: str) -> None:
        ...

    @abstractmethod
    def set_object(self, key: str, value: dict, exp: timedelta | None = None) -> None: ...

    @abstractmethod
    def get_object(self, key: str) -> dict | None: ...

class RedisCacheService(CacheService):
    _client: Redis | None

