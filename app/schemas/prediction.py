from datetime import datetime
from pydantic import BaseModel


class PredictionResponse(BaseModel):
    id: int
    message_id: int
    result: str
    confidence: float
    category: str
    explanation: str
    risk_score: int
    created_at: datetime

    model_config = {"from_attributes": True}
