from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.feedback import Feedback
from app.models.prediction import Prediction
from app.models.user import User
from app.schemas.feedback import FeedbackCreate, FeedbackResponse
from app.utils.deps import get_current_user

router = APIRouter(prefix="/feedback", tags=["Feedback"])


@router.post("", response_model=FeedbackResponse, status_code=status.HTTP_201_CREATED)
def create_feedback(
    payload: FeedbackCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> FeedbackResponse:
    prediction = db.query(Prediction).filter(Prediction.id == payload.prediction_id).first()
    if not prediction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prediction not found")

    feedback = Feedback(
        user_id=current_user.id,
        prediction_id=payload.prediction_id,
        is_correct=payload.is_correct,
        comment=payload.comment,
    )
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback
