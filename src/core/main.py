from fastapi import FastAPI
from sentry_sdk import init
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from starlette.middleware.cors import CORSMiddleware

from .settings import SENTRY_DSN

main_app = FastAPI()
main_app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=['*'], allow_credentials=True,
    allow_methods=['*'], allow_headers=['*'],
)

init(dsn=SENTRY_DSN)

app = SentryAsgiMiddleware(app=main_app)
