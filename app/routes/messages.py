from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.message import Message
from app.models.prediction import Prediction
from app.models.rule import Rule
from app.models.user import User
from app.schemas.message import MessageCreate, MessageResponse
from app.services.rule_engine import DEFAULT_RULES, evaluate_message
from app.utils.deps import get_current_user

router = APIRouter(prefix="/messages", tags=["Messages"])


@router.post("", response_model=MessageResponse, status_code=status.HTTP_201_CREATED)
def create_message(
    payload: MessageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> MessageResponse:
    message = Message(user_id=current_user.id, content=payload.content, source=payload.source.lower())
    db.add(message)
    db.flush()

    db_rules = db.query(Rule).all()
    rule_map = {rule.keyword.lower(): rule.weight for rule in db_rules} if db_rules else DEFAULT_RULES

    detection = evaluate_message(payload.content, rule_map)
    prediction = Prediction(
        message_id=message.id,
        result=detection.result,
        confidence=detection.confidence,
        category=detection.category,
        explanation=detection.explanation,
        risk_score=detection.risk_score,
    )
    db.add(prediction)
    db.commit()
    db.refresh(message)
    return message
