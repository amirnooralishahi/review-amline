from os import getenv
from pathlib import Path
from dotenv import load_dotenv
from core.types import (
    AmlineURLs,
    BaleURLs,
    ElasticSearchConfig,
    FinnotechConfig,
    JWTConfig,
    KaveNegarConfig,
    KenarDivarURLs,
    MinioConfig,
    RedisConfig,
    SMSTemplates,
    TelegramURLs,
    TSMConfig,
    TsmsURLs
)

BASE_DIR = Path(__file__).resolve().parent.parent

IS_PRODUCTION = getenv('IS_PRODUCTION','False') == "True"

if IS_PRODUCTION:
    load_dotenv(BASE_DIR / ".env.production")
else:
    load_dotenv(BASE_DIR/ '.env.staging')

EMPTY_STRING , ZERO = str(), int()

DEBUG = getenv("APP_DEBUG","False")=="True"

APP_NAME = (getenv("APP_NAME",EMPTY_STRING),)
APP_URL = (getenv('APP_URL',EMPTY_STRING),)
APP_VERSION = getenv('APP_VERSION',ZERO)
APP_ENV = getenv('APP_ENV',EMPTY_STRING)

CLI_PASSWORD = getenv('CLI_PASSWORD',EMPTY_STRING)

SECRET_KEY = getenv('SECRET_KEY',EMPTY_STRING)

DATABASE_URL = getenv('DATABASE_URL',EMPTY_STRING)
VOIP_DATABASE_URL = getenv('VOIP_DATABASE_URL',EMPTY_STRING)

PDF_GENERATOR_SERVICE_URL = getenv('PDF_GENERATOR_SERVICE_URL',EMPTY_STRING)

minio_config= MinioConfig(
    endpoint = getenv('MINIO_ENDPOINT',EMPTY_STRING),
    access_key = getenv('MINIO_ACCESS_KEY',EMPTY_STRING),
    secret_key = getenv('MINIO_SECRET_KEY',EMPTY_STRING),
)