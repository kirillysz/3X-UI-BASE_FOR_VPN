from app.api.server import router as sever_router
from app.api.user import router as user_router
from app.api.payment import router as payment_router
from app.api.subcription import router as subscription_router


from app.core.init_tables import create_tables
from contextlib import asynccontextmanager

from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(sever_router)
app.include_router(user_router)
app.include_router(payment_router)
app.include_router(subscription_router)