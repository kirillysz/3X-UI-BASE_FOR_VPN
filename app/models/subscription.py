from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base
import uuid

class Subscription(Base):
    __tablename__ = "subscriptions"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    link = Column(String, nullable=False)

    users = relationship("User", back_populates="subscription_rel")