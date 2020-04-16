FROM python:3.8.1-alpine3.11

ENV PYTHONUNBUFFERED=1 COLUMNS=200 TZ=Asia/Almaty

ADD ./src/requirements.txt ./src/dev_requirements.txt /src/

RUN \
#    sed -i "s/dl-cdn.alpinelinux.org/mirror.neolabs.kz/g" \
#    /etc/apk/repositories && \
    apk update \
    && apk --no-cache add bash postgresql-dev \
# Django translations
    gettext \
# Add build dependencies
    && apk --no-cache add --virtual .build-deps \
    tzdata gcc musl-dev \
# For git repos in requirements
    git \
# Set timezone
    && ln -fs /usr/share/zoneinfo/Asia/Almaty /etc/localtime \
    && echo "Asia/Almaty" > /etc/timezone \
# Upgrade pip
    && pip install --upgrade pip \
# Add project dependencies
    && pip install \
    --no-cache-dir -Ur /src/requirements.txt \
    --no-cache-dir -Ur /src/dev_requirements.txt \
# Remove build dependencies
    && apk del .build-deps

COPY ./src /src

WORKDIR /src
CMD ["/src/entrypoint.sh"]
