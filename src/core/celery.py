import sys

from celery import Celery

from .settings import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

sys.path.append('/src')

celery_app = Celery(
    main='core', broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)
