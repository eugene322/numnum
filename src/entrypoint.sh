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
clear_old_files () {
  rm -rf celerybeat.pid celerybeat-schedule
}
clear_old_files
populate_env_variables
case "$PROCESS" in
"LINT")
    mypy . && flake8 . && bandit -r . && safety check
    ;;
"TEST")
    pytest -v --cov . --cov-report term-missing --cov-fail-under=100 \
    --color=yes --mypy -n 4 -W error
    ;;
"DEV_FASTAPI")
    uvicorn core.main:app --reload --host 0.0.0.0 --port 8000
    ;;
"DEV_CELERY")
    wait_for "${BROKER_HOST}" "${BROKER_PORT}"
    celery -A core worker -B --loglevel=INFO --concurrency=1
    ;;
"FASTAPI")
    uvicorn core.main:app --host 0.0.0.0 --port 8000 \
    --proxy-headers --workers 5 # workers = (2*CPU)+1
    ;;
"CELERY")
    wait_for "${BROKER_HOST}" "${BROKER_PORT}"
    case "$NODE" in
    "SCHEDULER")
        celery -A core beat --loglevel=INFO
        ;;
    "CONSUMER")
        celery -A core worker --loglevel=INFO \
        --concurrency=3 --max-tasks-per-child=2048
        ;;
    *)
        echo "NO NODE SPECIFIED!"
        exit 1
        ;;
    esac
    ;;
*)
    echo "NO MODE SPECIFIED!"
    exit 1
    ;;
esac
