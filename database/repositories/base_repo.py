from abc import abstractmethod, ABC

from sqlalchemy.ext.asyncio import AsyncSession

from database import Base


class BaseRepository(ABC):
    model = Base
    
    @classmethod
    @abstractmethod
    async def create(cls, session: AsyncSession, *args, **kwargs):
        ...
    
    @classmethod
    @abstractmethod
    async def get(cls, session: AsyncSession, *args, **kwargs):
        ...

    @classmethod
    @abstractmethod
    async def all(cls, session: AsyncSession):
        ...

    @classmethod
    @abstractmethod
    async def first(cls, session: AsyncSession):
        ...

    @classmethod
    @abstractmethod
    async def last(cls, session: AsyncSession):
        ...

    @classmethod
    @abstractmethod
    async def filter(cls, session: AsyncSession, *args, **kwargs):
        ...

    @classmethod
    async def _commit(cls, session: AsyncSession):
        try:
            await session.commit()
        except:
            await session.rollback()
