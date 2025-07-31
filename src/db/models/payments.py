from __future__ import annotations
from src.db.base import Base

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


class Payment(Base):
    __tablename__ = 'payments'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    uuid: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        default=uuid4,
        unique=True,
        index=True
    )

    link: Mapped[str] = mapped_column(String(255), nullable=False)