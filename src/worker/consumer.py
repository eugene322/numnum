import asyncio

from worker.data import num_data
from worker.queue import NumQueue, NumItem


async def num_consumer(queue: NumQueue):
    while True:
        item: NumItem = await queue.get_item()
        await asyncio.sleep(item.timeout)
        num_data.add_num(item.num)
        queue.remove_item(item)
