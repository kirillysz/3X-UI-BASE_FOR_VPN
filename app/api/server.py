from uuid import UUID

from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.database import get_db
from app.models.server import Server
from app.schemas.server import ServerAdd, ServerReponse, ServerUpdate
from app.crud.server import ServerCRUD

router = APIRouter(prefix="/servers", tags=["Сервера"])


@router.get("/", response_model=List[ServerReponse])
async def get_servers(db: AsyncSession = Depends(get_db)):
    server_crud = ServerCRUD(db)
    servers = await server_crud.get_all_servers()

    if not servers:
        raise HTTPException(status_code=404, detail="Servers not found")
    return servers

@router.get("/{server_uuid}", response_model=ServerReponse)
async def get_server(server_uuid: UUID, db: AsyncSession = Depends(get_db)):
    server_crud = ServerCRUD(db)

    result = await server_crud.execute(
        select(Server).where(Server.uuid == server_uuid)
    )
    existing_server = result.scalar_one_or_none()

    if not existing_server:
        raise HTTPException(status_code=404, detail="Server not found")

    return ServerReponse.model_validate(existing_server)

@router.post("/add", response_model=ServerReponse)
async def add(server_data: ServerAdd, db: AsyncSession = Depends(get_db)):
    server_crud = ServerCRUD(db)

    result = await db.execute(
        select(Server).where(Server.uuid == server_data.uuid)
    )
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Server already exists")

    server = await server_crud.add_server(server_data)
    return server

@router.put("/update", response_model=ServerReponse)
async def update(server_uuid: UUID, update_data: ServerUpdate, db: AsyncSession = Depends(get_db)):
    server_crud = ServerCRUD(db)
    updated_server = await server_crud.update_server(server_uuid, update_data)
    
    if not updated_server:
        raise HTTPException(status_code=404, detail="Server not found")
    
    return updated_server

@router.delete("/delete", response_model=dict)
async def delete(server_uuid: UUID, db: AsyncSession = Depends(get_db)):
    server_crud = ServerCRUD(db)
    is_deleted = await server_crud.delete_server(server_uuid)

    if not is_deleted:
        raise HTTPException(status_code=404, detail="Server not found")

    return {"detail": "Server deleted successfully"}
