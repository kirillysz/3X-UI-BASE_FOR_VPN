from src.xui.clients import XUIClient
from asyncio import run
from fastapi import FastAPI

import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

app = FastAPI()


logger = logging.getLogger(__name__)

