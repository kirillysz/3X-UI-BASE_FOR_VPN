from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from src.cruds.payment_crud import PaymentCRUD
from src.schemas.payment_schema import PaymentCreate, PaymentInDB, PaymentUpdate
from src.db.database import get_db

router = APIRouter(prefix="/payments", tags=["payments"])


@router.post("/", response_model=PaymentInDB)
async def create_payment(
    payment_data: PaymentCreate, db: AsyncSession = Depends(get_db)
):

    crud = PaymentCRUD(db)
    try:
        return await crud.create_payment(payment_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{payment_uuid}")
async def delete_payment(payment_uuid: UUID, db: AsyncSession = Depends(get_db)):

    crud = PaymentCRUD(db)
    if not await crud.delete_payment(payment_uuid):
        raise HTTPException(status_code=404, detail="Payment not found")
    return {"status": "success", "message": "Payment deleted"}


@router.patch("/{payment_uuid}/status", response_model=PaymentInDB)
async def update_payment_status(
    payment_uuid: UUID, status_update: PaymentUpdate, db: AsyncSession = Depends(get_db)
):

    crud = PaymentCRUD(db)
    if not status_update.status:
        raise HTTPException(status_code=400, detail="Status is required")

    updated_payment = await crud.update_payment_status(
        payment_uuid, status_update.status
    )
    if not updated_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return updated_payment
