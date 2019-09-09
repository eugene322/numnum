# TODO: always check for "python manage.py check --deploy"
from os.path import dirname, abspath, join
from types import MappingProxyType
from typing import Tuple
import sentry_sdk
from corsheaders.defaults import default_methods, default_headers
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration
from core.helpers.default_apps import DEFAULT_APPS
from core.helpers.env_variables import default_env_variables
from core.helpers.i18n_settings import DEFAULT_LOCALE_PATHS, DEFAULT_LANGUAGES
from core.helpers.middlewares import DEFAULT_MIDDLEWARES
from core.helpers.rest_framework_settings import REST_FRAMEWORK_SETTINGS
from core.helpers.storages import STORAGES, DEFAULT_STORAGE
from core.helpers.templates import DEFAULT_TEMPLATES
from core.helpers.validators import DEFAULT_VALIDATORS

BASE_DIR = dirname(dirname(abspath(__file__)))
# Environment variables
env = default_env_variables
# Sentry
SENTRY_DSN: str = env.str(var='SENTRY_DSN')
sentry_sdk.init(dsn=SENTRY_DSN, integrations=(DjangoIntegration(), CeleryIntegration()))
# Django
DEBUG: bool = env.bool(var='DEBUG')
SECRET_KEY: str = env.str(var='SECRET_KEY')
APPEND_SLASH: bool = True
ALLOWED_HOSTS: Tuple = ('*',)
INSTALLED_APPS = DEFAULT_APPS
MIDDLEWARE = DEFAULT_MIDDLEWARES
ROOT_URLCONF: str = 'core.urls'
TEMPLATES = DEFAULT_TEMPLATES
WSGI_APPLICATION: str = 'core.wsgi.application'
DATABASES = MappingProxyType({'default': env.db()})
AUTH_PASSWORD_VALIDATORS = DEFAULT_VALIDATORS
# Security
SECURE_BROWSER_XSS_FILTER: bool = True
SESSION_COOKIE_SECURE: bool = False
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF: bool = True
CSRF_COOKIE_SECURE: bool = False
# Localization
LOCALE_PATHS = DEFAULT_LOCALE_PATHS
LANGUAGES = DEFAULT_LANGUAGES
LANGUAGE_CODE: str = 'en'
USE_I18N: bool = True
USE_L10N: bool = True
TIME_ZONE: str = 'Asia/Almaty'
USE_TZ: bool = True
STATIC_URL: str = '/static/'
STATIC_ROOT = join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = join(BASE_DIR, 'media')
# Corsheaders
CORS_ORIGIN_ALLOW_ALL: bool = True
CORS_ALLOW_METHODS: Tuple = default_methods
CORS_ALLOW_HEADERS: Tuple = default_headers
CORS_ALLOW_CREDENTIALS: bool = True
# Rest framework
REST_FRAMEWORK = REST_FRAMEWORK_SETTINGS
# Storage
DEFAULT_FILE_STORAGE: str = STORAGES.get(env.str(var='WHERE_TO_KEEP_MEDIA'), DEFAULT_STORAGE)
# AWS S3
AWS_ACCESS_KEY_ID = env.str(var='AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env.str(var='AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env.str(var='AWS_STORAGE_BUCKET_NAME')
AWS_AUTO_CREATE_BUCKET = env.bool(var='AWS_AUTO_CREATE_BUCKET')
AWS_DEFAULT_ACL = env.str(var='AWS_DEFAULT_ACL')
AWS_BUCKET_ACL = env.str(var='AWS_BUCKET_ACL')
AWS_S3_SIGNATURE_VERSION = env.str(var='AWS_S3_SIGNATURE_VERSION')
AWS_S3_REGION_NAME = env.str(var='AWS_S3_REGION_NAME')
AWS_S3_ENCRYPTION = env.bool(var='AWS_S3_ENCRYPTION')
AWS_QUERYSTRING_AUTH = env.bool(var='AWS_QUERYSTRING_AUTH')
# Celery
CELERY_BROKER_URL: str = env.str(var='CELERY_BROKER_URL')
CELERY_RESULT_BACKEND: str = env.str(var='CELERY_RESULT_BACKEND')
CELERY_TIMEZONE: str = 'Asia/Almaty'
CELERY_ENABLE_UTC: bool = True
CELERY_ACCEPT_CONTENT: Tuple = ('application/json',)
CELERY_TASK_SERIALIZER: str = 'json'
CELERY_RESULT_SERIALIZER: str = 'json'
CELERY_TASK_ACKS_LATE: bool = True
# Email
EMAIL_HOST = env.str(var='EMAIL_HOST')
EMAIL_PORT = env.int(var='EMAIL_PORT')
EMAIL_HOST_USER = env.str(var='EMAIL_HOST_USER')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = env.str(var='EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = env.bool(var='EMAIL_USE_TLS')
EMAIL_USE_SSL = env.bool(var='EMAIL_USE_SSL')
# Debug toolbar
if DEBUG:
    from core.helpers.debug_settings import (
        DEFAULT_DEBUG_MIDDLEWARES, DEFAULT_DEBUG_INTERNAL_IPS,
        DEFAULT_DEBUG_TOOLBAR_PANELS, DEFAULT_DEBUG_APPS
    )

    INSTALLED_APPS += DEFAULT_DEBUG_APPS
    MIDDLEWARE += DEFAULT_DEBUG_MIDDLEWARES
    INTERNAL_IPS = DEFAULT_DEBUG_INTERNAL_IPS
    DEBUG_TOOLBAR_PANELS = DEFAULT_DEBUG_TOOLBAR_PANELS
