from typing import List, Optional
from pydantic import BaseModel

class Todolist(BaseModel):
    notes: str
    created_at: str