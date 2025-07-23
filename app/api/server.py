from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.core.database import get_db
from app.schemas.server import ServerAdd, ServerReponse
from app.crud.server import ServerCRUD

router = APIRouter()
server_crud = ServerCRUD()

@router.get("/servers/{server_uuid}", response_model=ServerReponse)
async def get_server(server_uuid: UUID, db: AsyncSession = Depends(get_db)):
    server_data = {"uuid": server_uuid}
    server = await server_crud.check_existing(db, server_data)
    
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")
    return server
