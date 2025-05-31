from pydantic import BaseModel
from typing import Any

class BaseResponse(BaseModel):
    code: int = 200
    msg: str = "success"
    data: Any = None 