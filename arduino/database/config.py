from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from arduino.settings import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, DB_PORT, DB_HOST


DATABASE_URL = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}'
engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_async_session():
    async with async_session() as session:
        yield session


class Base(DeclarativeBase):
    pass
