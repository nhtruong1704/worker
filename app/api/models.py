from pydantic import BaseModel
from typing import List, Optional

class WorkIn(BaseModel):
    name: str
    phone: str
    pay: str
    genre: str


class WorkOut(WorkIn):
    id: int
