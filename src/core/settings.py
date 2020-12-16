from sys import path
from typing import Tuple

from sentry_sdk import init
from sentry_sdk.integrations.celery import CeleryIntegration
from starlette.config import Config

path.append('/src')

config: Config = Config(env_file='/src/core/.env')

CELERY_BROKER_URL: str = config(key='CELERY_BROKER_URL', cast=str)
CELERY_RESULT_BACKEND: str = config(key='CELERY_RESULT_BACKEND', cast=str)
SENTRY_DSN: str = config(key='SENTRY_DSN', cast=str)
init(
    dsn=SENTRY_DSN, integrations=(CeleryIntegration(),),
)

PROJECT_APPS: Tuple = ('common',)
message: str = 'no more than 5 apps per project'
assert len(PROJECT_APPS) <= 5, message  # nosec
