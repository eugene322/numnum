from datetime import timedelta
from types import MappingProxyType

REST_FRAMEWORK_SETTINGS = MappingProxyType({
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ), 'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ), 'DATETIME_FORMAT': '%s.%f', 'DATETIME_INPUT_FORMATS': '%s.%f',
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.SearchFilter',
    )
})

DEFAULT_SIMPLE_JWT = MappingProxyType({
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=999999),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=999999),
    'ROTATE_REFRESH_TOKENS': False, 'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256', 'VERIFYING_KEY': None, 'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id', 'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type', 'JTI_CLAIM': 'jti',
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=999999),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=999999)
})
