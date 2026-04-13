from datetime import datetime

from pydantic import BaseModel, Field


class MessageCreate(BaseModel):
    content: str = Field(min_length=5, max_length=5000)
    source: str = Field(min_length=2, max_length=64)


class MessageResponse(BaseModel):
    id: int
    content: str
    source: str
    created_at: datetime

    model_config = {"from_attributes": True}
