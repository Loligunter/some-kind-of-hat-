from app.database import async_session_maker
from sqlalchemy import select,insert
from app.hotels.models import Hotels

class BaseDAO:
    model=None

    @classmethod
    async def find_by_id(cls,model_id: int):
        async with async_session_maker() as session:
            query=select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
        
        
    @classmethod
    async def find_one_or_none(cls,**filter_by):
        async with async_session_maker() as session:
            query=select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    
    @classmethod
    async def find_all(cls,**filter_by):
        async with async_session_maker() as session:
            query=select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def add(cls,**data):
        async with async_session_maker() as session:
            query=insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def find_by_location(cls):
        async with async_session_maker() as session:  # Убедитесь, что async_session_maker возвращает AsyncSession
            result = await session.execute(
                select(Hotels).filter(Hotels.location == "Республика Коми, Сыктывкар, Коммунистическая улица, 67")
            )
            return result.scalars().all()  # Используем scalars(), если ожидаем список объектов Hotels