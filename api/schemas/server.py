from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4

class ServerModel(BaseModel):
    host: str = Field(..., description="URL для подключения к панели")
    username: str = Field(..., description="USERNAME панели")
    password: str = Field(..., description="Пароль панели")

class ServerAddModel(ServerModel):
    label: Optional[str] = Field(None, description="Название сервера или метка")
    country: Optional[str] = Field(None, description="Страна или регион")
    type: Optional[str] = Field("xray", description="Тип VPN панели (например, xray, v2ray)")
    is_active: Optional[bool] = Field(True, description="Активен ли сервер по умолчанию")
