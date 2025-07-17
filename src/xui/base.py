from py3xui import AsyncApi

import logging

class XUIClientBase:
    def __init__(
            self, 
            host: str, 
            username: str, 
            password: str,
            use_tls_verify: bool = False, 
            custom_certificate_path: str = None):
        self.client = AsyncApi(
            host=host, 
            username=username, 
            password=password,
            use_tls_verify=use_tls_verify,
            custom_certificate_path=custom_certificate_path)
        
        self.logger = logging.getLogger(__name__)

    async def init(self):
        await self.client.login()