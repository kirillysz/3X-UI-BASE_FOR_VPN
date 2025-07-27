from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.core.database import get_db
from app.schemas.server import ServerAdd, ServerReponse, ServerUpdate
from app.crud.server import ServerCRUD

router = APIRouter(prefix="/servers", tags=["Сервера"])
server_crud = ServerCRUD()


@router.get("/", response_model=List[ServerReponse])
async def get_servers(db: AsyncSession = Depends(get_db)):
    servers = await server_crud.get_all_servers(db)

    if not servers:
        raise HTTPException(status_code=404, detail="Servers not found")
    return servers

@router.get("/{server_uuid}", response_model=ServerReponse)
async def get_server(server_uuid: UUID, db: AsyncSession = Depends(get_db)):
    server_data = {"uuid": server_uuid}
    server = await server_crud.check_existing(db, server_data)
    
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")
    return server

@router.post("/add", response_model=ServerReponse)
async def add(server_data: ServerAdd, db: AsyncSession = Depends(get_db)):
    is_existing = await server_crud.check_existing(db, server_data)

    if is_existing:
        raise HTTPException(status_code=400, detail="Server already exists")

    server = await server_crud.add_server(db, server_data)
    return server
    
@router.put("/update", response_model=ServerReponse)
async def update(server_uuid: UUID, update_data: ServerUpdate, db: AsyncSession = Depends(get_db)):
    updated_server = await server_crud.update_server(db, server_uuid, update_data)
    
    if not updated_server:
        raise HTTPException(status_code=404, detail="Server not found")
    
    return updated_server