from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import text, create_engine
from data_base.config import settings

# Create the async engine
async_engine = create_async_engine(url=settings.DATABASE_URL_asyncpg, echo=True)
engine = create_engine(url=settings.DATABASE_URL_syncpg, echo=True)

async_sassion = async_sessionmaker(async_engine)
sync_sassion = sessionmaker(engine)

class Base(DeclarativeBase):
    pass