from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String, Text, func
from sqlalchemy.orm import relationship

from app.database import Base


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    message_id = Column(Integer, ForeignKey("messages.id", ondelete="CASCADE"), nullable=False, unique=True)
    result = Column(String(16), nullable=False)
    confidence = Column(Numeric(5, 4), nullable=False)
    category = Column(String(64), nullable=False)
    explanation = Column(Text, nullable=False)
    risk_score = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    message = relationship("Message", back_populates="prediction")
    feedback_items = relationship("Feedback", back_populates="prediction", cascade="all, delete-orphan")
