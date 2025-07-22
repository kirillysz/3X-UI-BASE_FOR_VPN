from src.xui.base import XUIClientBase
from py3xui import Client


class XUIClient(XUIClientBase):

    async def ensure_init(self) -> None:
        await self.init()

    async def get_by_email(self, email: str) -> Client | None:
        await self.init()
        try:
            return await self.client.client.get_by_email(email=email)
        
        except Exception as e:
            self.logger.error(f"Ошибка при получении клиента с email {email}: {e}", exc_info=True)
            return None
    
    async def add(self, inbound_id: int, clients: list[Client]) -> bool:
        await self.init()
        try:
            await self.client.client.add(inbound_id=inbound_id, clients=clients)
            return True
        
        except Exception as e:
            self.logger.error(f"Ошибка при добавлении клиента(ов) {clients} в подключение c ID {inbound_id}: {e}", exc_info=True)
            return False

    async def update(self, client_uuid: str, client: Client) -> bool:
        await self.init()
        try:
            await self.client.client.update(client_uuid=client_uuid,client=client)
            return True
        
        except Exception as e:
            self.logger.error(f"Ошибка при обновлении клиента {client_uuid}: {e}", exc_info=True)
            return False
    
    async def delete(self, inbound_id: int, client_uuid: str) -> bool:
        await self.init()
        try:
            await self.client.client.delete(inbound_id=inbound_id, client_uuid=client_uuid)
            return True
        
        except Exception as e:
            self.logger.error(f"Ошибка при удалении клиента {client_uuid} из подключения {inbound_id}: {e}", exc_info=True)
            return False

    async def delete_depleted(self, inbound_id: int) -> bool:
        await self.init()
        try:
            await self.client.client.delete_depleted(inbound_id=inbound_id)
            return True
        
        except Exception as e:
            self.logger.error(f"Ошибка при удалении истек. клиентов в подключении {inbound_id}: {e}", exc_info=True)
            return False

    async def reset_ips_by_email(self, email: str) -> bool:
        await self.init()
        try:
            await self.client.client.reset_ips(email=email)
            return True
        
        except Exception as e:
            self.logger.error(f"Ошибка при чистке IP-адресов у клиента {email}: {e}", exc_info=True)
            return False
        
    async def reset_stats_by_email(self, inbound_id: int, email: str) -> bool:
        await self.init()
        try:
            await self.client.client.reset_stats(inbound_id=inbound_id, email=email)
            return True
        
        except Exception as e:
            self.logger.error(f"Ошибка при сбросе статистики в подключении {inbound_id} для клиента {email}: {e}", exc_info=True)
            return False
        
    
