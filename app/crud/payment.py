from typing import Optional
from sqlalchemy.future import select
from sqlalchemy import update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID, uuid4

from app.models.payment import Payment
from app.schemas.payment import PaymentCreate, PaymentUpdate


class PaymentCRUD:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_payment(self, payment_data: PaymentCreate) -> Payment:

        existing_payment = await self.db.execute(
            select(Payment).where(
                Payment.payment_id_in_blockchain
                == payment_data.payment_id_in_blockchain
            )
        )
        if existing_payment.scalar_one_or_none():
            raise ValueError("Payment with this blockchain ID already exists")

        new_payment = Payment(
            uuid=uuid4(),
            payment_id_in_blockchain=payment_data.payment_id_in_blockchain,
            status=payment_data.status,
            user_id=payment_data.user_id,
        )

        self.db.add(new_payment)
        await self.db.commit()
        await self.db.refresh(new_payment)
        return new_payment

    async def update_payment_status(
        self, payment_uuid: UUID, new_status: str
    ) -> Optional[Payment]:

        result = await self.db.execute(
            update(Payment)
            .where(Payment.uuid == payment_uuid)
            .values(status=new_status)
            .returning(Payment)
        )
        await self.db.commit()
        return result.scalar_one_or_none()

    async def delete_payment(self, payment_uuid: UUID) -> bool:

        result = await self.db.execute(
            delete(Payment).where(Payment.uuid == payment_uuid)
        )
        await self.db.commit()
        return result.rowcount > 0

    async def get_payment(self, payment_uuid: UUID) -> Optional[Payment]:

        result = await self.db.execute(
            select(Payment).where(Payment.uuid == payment_uuid)
        )
        return result.scalar_one_or_none()