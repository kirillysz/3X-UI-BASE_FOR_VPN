from uuid import UUID, uuid4
from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.server import Server
from app.schemas.server import ServerAdd, ServerReponse, ServerUpdate


class ServerCRUD:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def check_existing(self, server_data: Server) -> Optional[ServerReponse]:
        result = await self.db.execute(
            select(Server).where(Server.uuid == server_data.uuid)
        )
        existing_server = result.scalar_one_or_none()

        if not existing_server:
            return None

        return ServerReponse.model_validate(existing_server)

    async def get_all_servers(self) -> Optional[List[ServerReponse]]:
        result = await self.db.execute(select(Server))
        servers = result.scalars().all()

        if not servers:
            return None

        return [ServerReponse.model_validate(server) for server in servers]

    async def add_server(self, server_data: ServerAdd) -> ServerReponse:
        new_server = Server(
            uuid=uuid4(),
            **server_data.model_dump()
        )
        self.db.add(new_server)
        await self.db.commit()
        await self.db.refresh(new_server)

        return ServerReponse.model_validate(new_server)

    async def update_server(self, server_uuid: UUID, update_data: ServerUpdate) -> Optional[ServerReponse]:
        result = await self.db.execute(
            select(Server).where(Server.uuid == server_uuid)
        )
        server = result.scalar_one_or_none()

        if not server:
            return None

        update_dict = update_data.model_dump(exclude_unset=True)
        for key, value in update_dict.items():
            setattr(server, key, value)

        await self.db.commit()
        await self.db.refresh(server)

        return ServerReponse.model_validate(server)


    async def delete_server(self, server_uuid: UUID) -> bool:
        result = await self.db.execute(
            select(Server).where(Server.uuid == server_uuid)
        )
        server = result.scalar_one_or_none()

        if not server:
            return False

        await self.db.delete(server)
        await self.db.commit()
        return True
