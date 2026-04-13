from datetime import datetime
from pydantic import BaseModel, Field


class FeedbackCreate(BaseModel):
    prediction_id: int
    is_correct: bool
    comment: str | None = Field(default=None, max_length=1000)


class FeedbackResponse(BaseModel):
    id: int
    prediction_id: int
    is_correct: bool
    comment: str | None
    created_at: datetime

    model_config = {"from_attributes": True}
