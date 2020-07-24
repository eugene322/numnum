from typing import Dict

from fastapi import APIRouter

value_router = APIRouter()


@value_router.get(path='/values/')
def values() -> Dict:
    return {}
