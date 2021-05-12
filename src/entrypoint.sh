#!/bin/bash
case "$PROCESS" in
"DEV_FASTAPI")
    uvicorn core.main:app --reload --host 0.0.0.0 --port 8000
    ;;
"FASTAPI")
    uvicorn core.main:app --host 0.0.0.0 --port 8000 \
    --proxy-headers --workers 8 --limit-max-requests 2048
    # workers = (2*CPU)+1
    ;;
*)
    echo "NO PROCESS SPECIFIED!"
    exit 1
    ;;
esac
