from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from datetime import datetime
from app.db.database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    description = Column(Text)

    intent = Column(String(50), default="unknown")
    intent_confidence = Column(Float, default=0.0)

    urgency = Column(String(20), default="low")
    urgency_confidence = Column(Float, default=0.0)

    risky = Column(String(10), default="no")
    suggested_reply = Column(Text, default="")

    status = Column(String(20), default="open")  # open/closed/review
    human_override = Column(String(10), default="no")

    created_at = Column(DateTime, default=datetime.utcnow)
