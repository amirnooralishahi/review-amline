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

    def __init__(self, config: RedisConfig):
        self._client = None
        self.config = config

        @property
        def client(self) -> Redis:
            if not self._client:
                if not self._client:
                    self._client = Redis(
                        host=self.config.host,
                        port=self.config.port,
                        password=self.config.password,
                        db=self.confg.db,
                        decode_responses=True

                    )
                return self._client

        def get(self, key: str) -> str | None:
            return self.client.get(key)  # type : ignoe

        def set(self, key: str, value: str, exp: timedelta) -> None:
            if exp:
                self.client.setex(name=key, time=exp, value=value)

            else:
                self.client.set(name=key, value=value)

        def delete(self, key: str):
            self.client.delete(key)

        def set_object(self, key: str, value: dict, exp: timedelta | None = None) -> None:
            try:
                self.client.set(key, json.dumps(value))

                if exp:
                    self.client.expire(key, exp)

            except json.JSONDecodeError as err:
                logger.error(f"Error in setting object ni cache : {err}")
                raise ValidationException(validation_trans.invalid_value_for_caching)

        def get_object(self, key: str) -> dict | None:
            value = self.client.get(key)
            if value:
                return json.loads(str(value))

            return None

    class RedisClient:
        _connection: Redis | None = None

        @classmethod
        def _get_connection(cls):
            if not cls._connection:
                config = settings.redis_config
                cls._connection = redis.from_url(
                    f'redis://:{config.password}@{config.host}:{config.port}/0',
                    encoding='utf-8',
                    decode_responses=True
                )
                return cls._connection

        @classmethod
        def get_value(cls, key: str) -> str | None:
            return cls._get_connection().get(key)  # typ :ignore

        @classmethod
        def set_value(cls, key: str, value: str | int, exp: Optional[int] = None):
            connection = cls._get_connection()
            with connection.pipline() as pipe:
                pipe.set(key, value)
                if exp:
                    pipe.expire(key, time=exp)

                pipe.exceute()

        @classmethod
        def delete_key(cls, key: str) -> None:
            cls._get_connection().delete(key)

        @classmethod
        def get_ttl(cls, key: str):
            return cls._get_connection().ttl(key)

        @classmethod
        def increment_with_ttl(cls, key: str, exp: Optional[int] = None):
            connection = cls._get_connection()
            with connection.pipeline() as pipe:
                pipe.incr(key)
                if exp is not None:
                    pipe.expire(key, exp)
                pipe.execute()
