import asyncio
import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict


@dataclass
class NumItem:
    oid: str
    added_at: datetime
    num: int
    timeout: int


class NumQueue:
    def __init__(self):
        self.queue = asyncio.Queue()
        self.queue_items: Dict[str, NumItem] = {}

    async def add_item(self, num: int, timeout: int) -> NumItem:
        oid = str(uuid.uuid4())
        now_time = datetime.now()
        item = NumItem(oid=oid, added_at=now_time, num=num, timeout=timeout)
        await self.queue.put(item)
        self.queue_items[oid] = item
        return item

    async def get_item(self) -> NumItem:
        return await self.queue.get()

    def remove_item(self, item: NumItem) -> None:
        del self.queue_items[item.oid]

    def items(self) -> List[NumItem]:
        return list(self.queue_items.values())


num_queue = NumQueue()
