from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional

from app.models.server import Server
from app.schemas.server import ServerAdd, ServerReponse


class ServerCRUD:
    @staticmethod
    async def check_existing(db: AsyncSession, server_data: dict) -> Optional[ServerReponse]:
        query = select(Server).where(
            Server.uuid == server_data.get("uuid")
        )
        result = await db.execute(query)
        existing_server = result.scalars().first()

        if not existing_server:
            return None
        
        return ServerReponse.model_validate(existing_server)
