import uuid
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.subscription import Subscription

from fastapi import HTTPException

from uuid import UUID, uuid4
from typing import Optional
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.models.subscription import Subscription
from src.schemas.subs_schema import SubCreate,SubBase,SubUpdate
from src.db.models.user import User



class SubCRUD:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_subscription(self, sub_data: SubCreate) -> Subscription:
        
        existing_sub = await self.db.execute(
            select(Subscription).where(Subscription.link == sub_data.link)
        )
        if existing_sub.scalar_one_or_none():
            raise ValueError("Sub already exists")

        
        new_sub = Subscription(
            uuid=uuid4(),
            link=sub_data.link,
            
        )
        
        self.db.add(new_sub)
        await self.db.commit()
        await self.db.refresh(new_sub)
        return new_sub
    
    async def delete_subscription(self, subscription_uuid: uuid.UUID) -> bool:
    
    
        result = await self.db.execute(
            select(Subscription)
            .where(Subscription.uuid == subscription_uuid)
        )
        subscription = result.scalar_one_or_none()
        
        if not subscription:
            return False
        
        
        await self.db.execute(
            update(User)
            .where(User.subscription_id == subscription_uuid)
            .values(subscription_id=None)
        )
        
        
        await self.db.delete(subscription)
        await self.db.commit()
        return True

    