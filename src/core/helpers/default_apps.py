from typing import Tuple

DJANGO_APPS: Tuple[str, ...] = (
    'django.contrib.admin', 'django.contrib.staticfiles',
    'django.contrib.contenttypes', 'django.contrib.auth',
    'django.contrib.messages', 'django.contrib.sessions',
)
SIDE_APPS: Tuple[str, ...] = (
    'corsheaders', 'rest_framework', 'django_extensions',
    'django_filters', 'django_fsm',
)
PROJECT_APPS: Tuple[str, ...] = ()
DEFAULT_APPS: Tuple[str, ...] = DJANGO_APPS + SIDE_APPS + PROJECT_APPS
