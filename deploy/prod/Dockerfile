FROM python:3.6.9-alpine3.10

ENV PYTHONUNBUFFERED=1 COLUMNS=200 TZ=Asia/Almaty

WORKDIR /src
COPY ./src /src
# Set timezone
RUN apk add tzdata && cp /usr/share/zoneinfo/Asia/Almaty /etc/localtime && \
    echo "Asia/Almaty" > /etc/timezone && apk del tzdata && \
# Add yandex alpine mirrors
    echo http://mirror.yandex.ru/mirrors/alpine/v3.10/main > /etc/apk/repositories; \
    echo http://mirror.yandex.ru/mirrors/alpine/v3.10/community >> /etc/apk/repositories && \
# Add system dependencies
    apk update && apk add bash postgresql-client gcc musl-dev postgresql-dev \
    gettext libressl-dev curl-dev zlib-dev jpeg-dev && \
# Add project dependencies
    pip install --upgrade pip && pip install -U -r requirements.txt && \
# Make entrypoint executable
    chmod +x entrypoint.sh && \
# Remove pycache
    find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf && \
# Remove unused files
    rm -rf requirements.txt requirements_dev.txt \
    .pytest_cache .mypy_cache `find -type d -name tests` \
    pytest.ini conftest.py .coverage .coveragerc celerybeat-schedule
