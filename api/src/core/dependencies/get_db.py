from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine

from src.core.config import DATABASE_URL

from ..models import *

# DATABASE_URL = os.environ.get("DATABASE_URL") or "sqlite+aiosqlite:///database.db"

engine: AsyncEngine = create_async_engine(url=DATABASE_URL)
SessionLocal = async_sessionmaker(bind=engine)


async def get_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
