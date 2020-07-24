from starlette.config import Config

config: Config = Config(env_file='/src/core/.env')

CELERY_BROKER_URL: str = config(key='CELERY_BROKER_URL')
CELERY_RESULT_BACKEND: str = config(key='CELERY_RESULT_BACKEND')
SENTRY_DSN: str = config(key='SENTRY_DSN')
