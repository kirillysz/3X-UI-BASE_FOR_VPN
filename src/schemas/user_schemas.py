from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


class UserBase(BaseModel):
    tg_id: str
    is_active: bool = False


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    tg_id: Optional[str] = None
    is_active: Optional[bool] = None
    subscription_id: Optional[UUID] = Field(
        None, example="5e98744c-4910-4b3e-acb3-ba3beb93df9c"
    )


class UserInDB(UserBase):
    uuid: UUID
    subscription_id: Optional[UUID] = None

    class Config:
        from_attributes = True
