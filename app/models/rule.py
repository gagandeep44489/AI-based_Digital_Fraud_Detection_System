from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Rule(Base):
    __tablename__ = "rules"

    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(String(128), unique=True, nullable=False, index=True)
    category = Column(String(64), nullable=False, default="general")
    weight = Column(Integer, nullable=False, default=25)
    description = Column(Text, nullable=False)
