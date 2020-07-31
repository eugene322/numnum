from sys import path
from typing import Tuple

from starlette.config import Config

path.append('/src')

config: Config = Config(env_file='/src/core/.env')

CELERY_BROKER_URL: str = config(key='CELERY_BROKER_URL', cast=str)
CELERY_RESULT_BACKEND: str = config(key='CELERY_RESULT_BACKEND', cast=str)
SENTRY_DSN: str = config(key='SENTRY_DSN', cast=str)

PROJECT_APPS: Tuple = ('common',)
