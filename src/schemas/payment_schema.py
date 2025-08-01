from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class PaymentBase(BaseModel):
    payment_id_in_blockchain: str
    status: str = "paid"
    user_id: UUID


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    status: Optional[str] = None
    payment_id_in_blockchain: Optional[str] = None


class PaymentInDB(PaymentBase):
    uuid: UUID

    class Config:
        from_attributes = True
