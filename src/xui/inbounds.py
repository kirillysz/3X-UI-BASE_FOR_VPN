from src.xui.base import XUIClientBase
from py3xui import Inbound

class XUIClientInbound(XUIClientBase):
    
    async def get_all_inbounds(self) -> list[Inbound] | None:
        await self.init()
        try:
            return await self.client.inbound.get_list()
        
        except Exception as e:
            self.logger.error(f"Ошибка при получении подключений: {e}", exc_info=True)
            return None

    async def get_inbound_by_id(self, inbound_id: int) -> Inbound | None:
        await self.init()
        try:
            return await self.client.inbound.get_by_id(inbound_id=inbound_id)
        
        except Exception as e:
            self.logger.error(f"Ошибка при получении inbound c ID {inbound_id}: {e}", exc_info=True)
            return None

    async def add(self, inbound: Inbound) -> bool:
        await self.init()
        try:
            await self.client.inbound.add(inbound=inbound)
            return True
        
        except Exception as e:
            self.logger.error(f"Ошибка при добавлении inbound: {e}", exc_info=True)
            return False

    async def delete(self, inbound_id: int) -> bool:
        await self.init()
        try:
            await self.client.inbound.delete(inbound_id=inbound_id)
            return True
        
        except Exception as e:
            self.logger.error(f"Ошибка при удалении inbound с ID {inbound_id}: {e}", exc_info=True)
            return False
        
    async def update(self, inbound_id: int, inbound: Inbound) -> bool:
        await self.init()
        try:
            await self.client.inbound.update(inbound_id=inbound_id, inbound=inbound)
            return True
        
        except Exception as e:
            self.logger.error(f"Ошибка при обновлении inbound с ID {inbound_id}: {e}", exc_info=True)

    async def reset_all_stats(self) -> bool:
        await self.init()
        try:
            await self.client.inbound.reset_stats()
            return True
        
        except Exception as e:
            self.logger.error(f"Ошибка при сбросе статистик: {e}", exc_info=True)

    async def reset_inbound_stats(self, inbound_id: int) -> bool:
        await self.init()
        try:
            await self.client.inbound.reset_client_stats(inbound_id=inbound_id)
            return True
        
        except Exception as e:
            self.logger.error(f"Ошибки при сбросе статистик с inbound с ID {inbound_id}: {e}", exc_info=True)

    