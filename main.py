from src.xui.clients import XUIClient
from asyncio import run
from fastapi import FastAPI
from src.routes.user_routers import router as user_router
from src.routes.sub_routers import router as sub_router
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

app = FastAPI()
app.include_router(user_router)
app.include_router(sub_router)

logger = logging.getLogger(__name__)

