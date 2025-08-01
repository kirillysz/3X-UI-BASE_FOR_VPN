import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.subscription import SubCreate, SubUpdate
from app.crud.subcription import SubCRUD

router = APIRouter(prefix="/subscribes", tags=["subscribes"])


@router.post("/", response_model=SubCreate)
async def create_sub(sub_data: SubCreate, db: AsyncSession = Depends(get_db)):
    crud = SubCRUD(db)
    try:
        return await crud.create_subscription(sub_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/delete")
async def delete_sub(subscription_uuid: uuid.UUID, db: AsyncSession = Depends(get_db)):
    crud = SubCRUD(db)
    try:
        return await crud.delete_subscription(subscription_uuid)
    except ValueError as e:
        raise HTTPException(status_code=400, detail="error")