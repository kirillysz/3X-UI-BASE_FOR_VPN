from __future__ import annotations
import uuid
from typing import Optional
from sqlalchemy import Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from src.db.base import Base

class User(Base):
    __tablename__ = 'users'
    
    uuid: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True
    )
    
    tg_id: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    
    subscription_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('subscriptions.uuid'),
        nullable=True
    )
    
    subscription: Mapped["Subscription"] = relationship("Subscription", back_populates="users")
    payments: Mapped["Payment"] = relationship("Payment", back_populates="user")
    
    
    

    