#!/bin/bash
wait_for () {
    for _ in `seq 0 100`; do
        (echo > /dev/tcp/$1/$2) >/dev/null 2>&1
        if [[ $? -eq 0 ]]; then
            echo "$1:$2 accepts connections"
            break
        fi
        sleep 1
    done
}
populate_env_variables () {
  set -o allexport
  [[ -f core/.env ]] && source core/.env
  set +o allexport
  echo "env variables are populated"
}
populate_env_variables
case "$MODE" in
"SAFETY")
    safety check
    ;;
"MYPY")
    mypy .
    ;;
"BANDIT")
    bandit -r .
    ;;
"FLAKE8")
    flake8 .
    ;;
"TEST")
    wait_for "${DB_HOST}" "${DB_PORT}"
    pytest -v --cov . --cov-report term-missing --cov-fail-under=100 \
    --color=yes -n 6 --no-migrations --reuse-db -W error
    ;;
"SERVER")
    wait_for "${DB_HOST}" "${DB_PORT}"
    python manage.py collectstatic --noinput && python manage.py migrate
    case "$WEB_SERVER" in
        "GUNICORN")
        gunicorn -c gunicorn.conf.py core.wsgi
        ;;
        "UVICORN")
        uvicorn core.asgi:application --host 0.0.0.0 --port 8000 --workers 8
        ;;
        *)
        echo "NO WEB_SERVER SPECIFIED!"
        exit 1
        ;;
    esac
    ;;
"DEV")
    wait_for "${DB_HOST}" "${DB_PORT}"
    python manage.py migrate && python manage.py runserver 0.0.0.0:8000
    ;;
"CELERY")
    wait_for "${DB_HOST}" "${DB_PORT}"
    wait_for "${BROKER_HOST}" "${BROKER_PORT}"
    celery -A core worker -B --loglevel=INFO --concurrency=1
    ;;
"CELERY_SCHEDULER")
    wait_for "${DB_HOST}" "${DB_PORT}"
    wait_for "${BROKER_HOST}" "${BROKER_PORT}"
    celery -A core beat --loglevel=INFO
    ;;
"CELERY_CONSUMER")
    wait_for "${DB_HOST}" "${DB_PORT}"
    wait_for "${BROKER_HOST}" "${BROKER_PORT}"
    celery -A core worker --loglevel=INFO
    ;;
*)
    echo "NO MODE SPECIFIED!"
    exit 1
    ;;
esac
