import asyncio

from fastapi import FastAPI

from worker.consumer import num_consumer
from worker.views import worker_router
from worker.queue import num_queue

app: FastAPI = FastAPI()


@app.on_event("startup")
def startup():
    # Start consumer for num_queue
    asyncio.ensure_future(num_consumer(num_queue))


app.include_router(
    prefix='/api', router=worker_router,
)
