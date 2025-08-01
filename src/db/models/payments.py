from __future__ import annotations
import uuid
from typing import Optional
from sqlalchemy import Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from src.db.base import Base




class Payment(Base):
    __tablename__ = 'payments'
    
    uuid: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True
    )
    payment_id_in_blockchain: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(255))
    
    
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('users.uuid'),
        nullable=False
    )
    
    user: Mapped["User"] = relationship("User", back_populates="payments")