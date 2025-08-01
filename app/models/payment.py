from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import relationship

from app.core.database import Base
import uuid

class Payment(Base):
    __tablename__ = "payments"

    uuid = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    payment_id_in_blockchain = Column(String, unique=True, nullable=False)
    status = Column(String, nullable=False, default="not_paid")
    user_id = Column(PGUUID(as_uuid=True), ForeignKey("users.uuid"), nullable=False)

    
    user = relationship("User", back_populates="payments")