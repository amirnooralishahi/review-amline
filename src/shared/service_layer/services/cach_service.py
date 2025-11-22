import abc
import json
from datetime import timedelta
from typing import Optional
import redis
from redis import Redis
from core import settings
from core.excepions import  ValidationException
from core.logger import logger
from core.translates import validation_trans
from core.types import  RedisConfig

