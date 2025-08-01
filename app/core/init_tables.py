from app.core.database import Base, engine
from app.models.user import User
from app.models.payment import Payment
from app.models.server import Server
from app.models.subscription import Subscription

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)