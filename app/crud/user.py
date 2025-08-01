from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User

from uuid import UUID, uuid4
from typing import Optional
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class UserCRUD:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user_data: UserCreate) -> User:

        existing_user = await self.db.execute(
            select(User).where(User.tg_id == user_data.tg_id)
        )
        if existing_user.scalar_one_or_none():
            raise ValueError("User with this telegram_id already exists")

        new_user = User(
            uuid=uuid4(),
            tg_id=user_data.tg_id,
            is_active=user_data.is_active if hasattr(user_data, "is_active") else False,
            subscription_id=(
                user_data.subscription_id
                if hasattr(user_data, "subscription_id")
                else None
            ),
        )

        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        return new_user

    async def get_user_by_uuid(self, user_uuid: UUID) -> Optional[User]:
        result = await self.db.execute(select(User).where(User.uuid == user_uuid))
        return result.scalar_one_or_none()

    async def get_user_by_telegram_id(self, telegram_id: str) -> Optional[User]:
        result = await self.db.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        return result.scalar_one_or_none()

    async def update_user(
        self, user_uuid: UUID, user_data: UserUpdate
    ) -> Optional[User]:

        user = await self.get_user_by_uuid(user_uuid)
        if not user:
            return None

        update_values = {k: v for k, v in user_data.dict().items() if v is not None}
        if not update_values:
            return user

        await self.db.execute(
            update(User).where(User.uuid == user_uuid).values(**update_values)
        )
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def delete_user(self, user_uuid: UUID) -> bool:
        result = await self.db.execute(delete(User).where(User.uuid == user_uuid))
        await self.db.commit()
        return result.rowcount > 0

    # бан разбан
    async def activate_user(self, user_uuid: UUID) -> Optional[User]:
        return await self.update_user(user_uuid, UserUpdate(is_active=True))

    async def deactivate_user(self, user_uuid: UUID) -> Optional[User]:
        return await self.update_user(user_uuid, UserUpdate(is_active=False))