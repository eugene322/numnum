from datetime import datetime

from pydantic import BaseModel, conint


class NumItemSerializer(BaseModel):
    num: int
    timeout: conint(ge=0)


class NumItemOutSerializer(NumItemSerializer):
    oid: str
    added_at: datetime
