from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.database import get_db
from src.schemas.user_schemas import UserCreate, UserUpdate, UserInDB
from src.cruds.user_crud import UserCRUD

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserInDB)
async def create_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    crud = UserCRUD(db)
    try:
        return await crud.create_user(user_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{user_uuid}", response_model=UserInDB)
async def read_user(user_uuid: UUID, db: AsyncSession = Depends(get_db)):
    crud = UserCRUD(db)
    user = await crud.get_user_by_uuid(user_uuid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_uuid}", response_model=UserInDB)
async def update_user(
    user_uuid: UUID, user_data: UserUpdate, db: AsyncSession = Depends(get_db)
):
    crud = UserCRUD(db)
    user = await crud.update_user(user_uuid, user_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/{user_uuid}")
async def delete_user(user_uuid: UUID, db: AsyncSession = Depends(get_db)):
    crud = UserCRUD(db)
    success = await crud.delete_user(user_uuid)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
