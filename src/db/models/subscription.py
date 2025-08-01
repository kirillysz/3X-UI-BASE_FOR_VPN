from __future__ import annotations
import uuid
from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from src.db.base import Base

class Subscription(Base):
    __tablename__ = 'subscriptions'
    
    
    uuid: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, primary_key=True)
    link: Mapped[str] = mapped_column(String(255))
    
    
    users: Mapped[List["User"]] = relationship(
        "User", 
        back_populates="subscription",
        cascade="all, delete-orphan",
        passive_deletes=True
    )
    
    
    
    