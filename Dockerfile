FROM python:3.9.5-slim-buster

ADD ./src/requirements.txt \
    /src/

RUN \
# Add project dependencies
    pip install --no-cache-dir -Ur /src/requirements.txt

COPY ./src /src

WORKDIR /src
CMD ["./entrypoint.sh"]
