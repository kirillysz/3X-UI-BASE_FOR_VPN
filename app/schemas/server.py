from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from uuid import UUID, uuid4

class Server(BaseModel):
    host: str = Field(..., description="URL для подключения к панели")
    username: str = Field(..., description="USERNAME панели")
    password: str = Field(..., description="Пароль панели")

class ServerAdd(Server):
    label: Optional[str] = Field(None, description="Название сервера или метка")
    country: Optional[str] = Field(None, description="Страна или регион")
    is_active: Optional[bool] = Field(True, description="Активен ли сервер по умолчанию")
    uuid: Optional[UUID] = Field(default_factory=uuid4, description="Уникальный идентификатор сервера")


class ServerReponse(BaseModel):
    uuid: UUID = Field(..., description="Уникальный идентификатор сервера")

    host: str = Field(..., description="URL для подключения к панели")
    username: str = Field(..., description="USERNAME панели")
    
    label: Optional[str] = Field(None, description="Название сервера или метка")
    country: Optional[str] = Field(None, description="Страна или регион")
    is_active: bool = Field(..., description="Активен ли сервер")

    model_config = ConfigDict(from_attributes=True)