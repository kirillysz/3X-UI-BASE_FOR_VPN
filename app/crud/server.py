from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional, List

from app.models.server import Server
from app.schemas.server import ServerAdd, ServerReponse


class ServerCRUD:
    @staticmethod
    async def check_existing(db: AsyncSession, server_data: Server) -> Optional[ServerReponse]:
        query = select(Server).where(
            Server.uuid == server_data.get("uuid")
        )
        result = await db.execute(query)
        existing_server = result.scalars().first()

        if not existing_server:
            return None
        
        return ServerReponse.model_validate(existing_server)

    @staticmethod
    async def get_all_servers(db: AsyncSession) -> Optional[List[ServerReponse]]:
        query = select(Server)
        result = await db.execute(query)
        servers = result.scalars().all()

        if not servers:
            return None
        
        return [ServerReponse.model_validate(server) for server in servers]
        
    @staticmethod
    async def add_server(db: AsyncSession, server_data: ServerAdd) -> ServerReponse:
        new_server = Server(**server_data.model_dump())
        db.add(new_server)

        await db.commit()
        await db.refresh(new_server)

        return ServerReponse.model_validate(new_server)