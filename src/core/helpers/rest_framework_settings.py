from types import MappingProxyType

REST_FRAMEWORK_SETTINGS = MappingProxyType({
    'DEFAULT_AUTHENTICATION_CLASSES': (), 'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    )
})
