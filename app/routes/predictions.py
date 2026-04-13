from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.message import Message
from app.schemas.prediction import PredictionResponse
from app.utils.deps import get_current_user

router = APIRouter(prefix="/predictions", tags=["Predictions"])


@router.get("/{message_id}", response_model=PredictionResponse)
def get_prediction(message_id: int, db: Session = Depends(get_db), _=Depends(get_current_user)) -> PredictionResponse:
    message = db.query(Message).filter(Message.id == message_id).first()
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    if not message.prediction:
        raise HTTPException(status_code=404, detail="Prediction not found")
    return message.prediction
