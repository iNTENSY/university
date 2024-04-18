from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from arduino.database.config import get_async_session
from arduino.database.models import Cards
from arduino.services.interfaces import IRepository


class Repository(IRepository):
    Model = Cards

    async def find(self, parameter, session: AsyncSession = get_async_session()):
        statement = select(self.Model).where(self.Model.card == parameter)
        result = (await session.execute(statement)).scalar_one_or_none()
        if result is None:
            return None
        return result.__dict__

    async def create(self, data: dict, session: AsyncSession = get_async_session(), *args, **kwargs):
        statement = insert(self.Model).values(**data).returning(self.Model)
        result = (await session.execute(statement)).scalars()
        await session.commit()
        return result

    async def update(self, data: dict, session: AsyncSession = get_async_session()):
        try:
            statement = (
                update(self.Model)
                .where(self.Model.card == data["card"])
                .values(**data)
                .returning(self.Model)
            )
            result = (await session.execute(statement)).scalars()
            await session.commit()
        except Exception as exc:
            return None
        return result
