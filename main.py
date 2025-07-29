from src.xui.inbounds import XUIClientInbound
from asyncio import run

import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

async def main():
    xui = XUIClientInbound(
        host="https://panel.detaflow.digital:52861/qhoyDyB7xQlarQcYxS",
        username="p51auujiAV",
        password="zG52nL5xBm",
        use_tls_verify=True
    )
    inbound = await xui.get_all_inbounds()
    print(await xui.get_connection_string(
        inbound=inbound[0],
        user_uuid="5473c451-dbab-486f-83bb-e41ea9be595d",
        user_email="jtj48zfo"
    ))

run(main())