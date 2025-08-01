from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import relationship

from app.core.database import Base

import uuid

class User(Base):
    __tablename__ = "users"

    uuid = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    telegram_id = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, default=False)

    payments = relationship("Payment", back_populates="user", cascade="all, delete-orphan")

    subscription_id = Column(PGUUID(as_uuid=True), ForeignKey("subscriptions.uuid"), nullable=True)
    subscription_rel = relationship("Subscription", back_populates="users")
