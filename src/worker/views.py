from dataclasses import asdict
from typing import List

from fastapi import APIRouter

from worker.data import num_data
from worker.queue import num_queue
from worker.serializers import NumItemOutSerializer, NumItemSerializer

worker_router = APIRouter()


@worker_router.post(
    path='/worker/', status_code=201,
    response_model=NumItemOutSerializer
)
async def add_worker_item(item: NumItemSerializer):
    new_item = await num_queue.add_item(num=item.num, timeout=item.timeout)
    return asdict(new_item)


@worker_router.get(
    path='/worker/', status_code=200,
    response_model=List[int]
)
async def worker_items():
    return num_data.nums()


@worker_router.get(
    path='/worker/queue/', status_code=200,
    response_model=List[NumItemOutSerializer]
)
async def worker_queue_items():
    return [asdict(item) for item in num_queue.items()]
