from starlette.config import Config

config = Config(env_file='/src/core/.env')

CELERY_BROKER_URL = config(key='CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = config(key='CELERY_RESULT_BACKEND')
SENTRY_DSN = config(key='SENTRY_DSN')
