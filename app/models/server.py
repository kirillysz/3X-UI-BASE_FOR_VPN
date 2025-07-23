from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID as PGUUID

from app.core.database import Base
import uuid

class Server(Base):
    __tablename__ = "servers"

    uuid = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)

    host = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    label = Column(String, nullable=True)
    country = Column(String, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
