from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from uuid import UUID

class UserBase(BaseModel):
    telegram_id: str
    is_active: bool = False
    subscription: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)

class UserResponse(UserBase):
    uuid: UUID

class UserCreate(BaseModel):
    telegram_id: str
    subscription: Optional[int] = None

class UserUpdate(BaseModel):
    is_active: Optional[bool]
    subscription: Optional[int]

