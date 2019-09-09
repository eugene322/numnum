FROM python:3.6.9-alpine3.10

ENV PYTHONUNBUFFERED=1 COLUMNS=200 TZ=Asia/Almaty

COPY ./src /src
WORKDIR /src
# Add yandex alpine mirrors
RUN echo http://mirror.yandex.ru/mirrors/alpine/v3.10/main > /etc/apk/repositories; \
    echo http://mirror.yandex.ru/mirrors/alpine/v3.10/community >> /etc/apk/repositories && \
# Set timezone
    apk add tzdata && cp /usr/share/zoneinfo/Asia/Almaty /etc/localtime && \
    echo "Asia/Almaty" > /etc/timezone && apk del tzdata && \
# Add system dependencies
    apk update && \
    apk add bash postgresql-client gcc musl-dev postgresql-dev \
    gettext libressl-dev curl-dev zlib-dev jpeg-dev && \
# Add project dependencies
    pip install --upgrade pip && pip install -U -r requirements.txt && \
# Add dev dependencies
    pip install -U -r requirements_dev.txt && \
# Make entrypoint executable
    chmod +x entrypoint.sh
