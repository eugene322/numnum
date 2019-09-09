from os.path import join, abspath, dirname
from django.utils.translation import gettext_lazy as _


def locale_path_for_app(app: str) -> str:
    return join(dirname(dirname(dirname(abspath(__file__)))), f'{app}/locale')


DEFAULT_LOCALE_PATHS = (
    locale_path_for_app(app='authorization'),
    locale_path_for_app(app='question'), locale_path_for_app(app='payment'),
)
DEFAULT_LANGUAGES = (
    ('en', _('English')), ('ru', _('Russian')), ('kz', _('Kazakh')),
)
