from src.xui.base import XUIClientBase
from py3xui import Inbound

class XUIClientInbound(XUIClientBase):
    def __init__(self, host, username, password, use_tls_verify = False, custom_certificate_path = None):
        super().__init__(host, username, password, use_tls_verify, custom_certificate_path)

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

    async def get_connection_string(self, inbound: Inbound, user_uuid: str, user_email: int) -> str:
        await self.init()
        public_key = inbound.stream_settings.reality_settings.get("settings").get("publicKey")
        website_name = inbound.stream_settings.reality_settings.get("serverNames")[0]
        short_id = inbound.stream_settings.reality_settings.get("shortIds")[0]
        
        connection_string = (
            f"vless://{user_uuid}@panel.detaflow.digital:433"
            f"?type=tcp&security=reality&pbk={public_key}&fp=chrome"
            f"&sni={website_name}&sid={short_id}&spx=%2F&flow=xtls-rprx-vision"
            f"#DETAFLOW-{user_email}"
        )

        return connection_string