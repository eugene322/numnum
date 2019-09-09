from datetime import timedelta
from types import MappingProxyType

REST_FRAMEWORK_SETTINGS = MappingProxyType({
    'DEFAULT_AUTHENTICATION_CLASSES': (), 'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ), 'DATETIME_FORMAT': '%s.%f', 'DATETIME_INPUT_FORMATS': '%s.%f',
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.SearchFilter',)
})
