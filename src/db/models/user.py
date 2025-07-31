from __future__ import annotations
from typing import List,TYPE_CHECKING
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.db.base import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import Integer,String


from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String


from sqlalchemy import UUID, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import uuid4
from typing import Optional


class User(Base):
    __tablename__ = 'users'
    
    uuid: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid4, 
        unique=True, 
        index=True
    )

    telegram_id: Mapped[str] = mapped_column(
        String(50), 
        nullable=False, 
        unique=True
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, 
        default=False, 
        nullable=False
    )

    subscription_id: Mapped[Optional[int]] = mapped_column(
        Integer, 
        ForeignKey('subscriptions.id'),
        nullable=True
    ) 
    
    
    

    