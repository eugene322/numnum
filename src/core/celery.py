from celery import Celery

from .settings import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

celery_app: Celery = Celery(
    main='core', broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)
