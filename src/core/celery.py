from os import environ

from celery import Celery
from django.utils.timezone import localtime

environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')


class MyCelery(Celery):
    def now(self):
        return localtime()


celery_app = MyCelery('core')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
