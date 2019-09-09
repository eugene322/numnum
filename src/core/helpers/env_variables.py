from environ import Env

default_env_variables = Env(
    DEBUG=(bool, True), DATABASE_URL=(str, 'psql://user:pass@postgres:5432/db'),
    SECRET_KEY=(str, 'B81543719AB276D3268D4A293FC2A492E2B4996CCE2D6624B529351A26'),
    SESSION_COOKIE_SECURE=(bool, False),
    # Media
    WHERE_TO_KEEP_MEDIA=(str, 'LOCAL'),
    # AWS
    AWS_ACCESS_KEY_ID=(str, 'NOT_NEEDED_WITHOUT_AWS_S3'), AWS_AUTO_CREATE_BUCKET=(bool, True),
    AWS_SECRET_ACCESS_KEY=(str, 'NOT_NEEDED_WITHOUT_AWS_S3'), AWS_DEFAULT_ACL=(str, 'private'),
    AWS_STORAGE_BUCKET_NAME=(str, 'NOT_NEEDED_WITHOUT_AWS_S3'), AWS_BUCKET_ACL=(str, 'private'),
    AWS_S3_SIGNATURE_VERSION=(str, 's3v4'), AWS_S3_REGION_NAME=(str, 'eu-west-2'),
    AWS_S3_ENCRYPTION=(bool, True), AWS_QUERYSTRING_AUTH=(bool, False),
    # Celery
    CELERY_BROKER_URL=(str, 'amqp://user:pass@rabbitmq:5672//'),
    CELERY_RESULT_BACKEND=(str, 'db+postgresql://user:pass@postgres:5432/db'),
    # Email
    EMAIL_HOST=(str, 'smtp.yandex.ru'), EMAIL_HOST_USER=(str, 'auction@thefactory.kz'),
    EMAIL_PORT=(int, 587), EMAIL_HOST_PASSWORD=(str, 'KzA9duEGZWUSse7M'),
    EMAIL_USE_TLS=(bool, True), EMAIL_USE_SSL=(bool, False),
    # Sentry
    SENTRY_DSN=(str, ''),
    # Auth settings
    CLIENT_URL=(str, '0.0.0.0:8080'),
    # HOST_URL
    HOST_URL=(str, '0.0.0.0'),
)
Env.read_env()
