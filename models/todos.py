from pydantic import BaseModel
from typing import Optional


class Todo(BaseModel):
    name : Optional[str] = None
    description : Optional[str] = None
    completed : Optional[bool] = None


