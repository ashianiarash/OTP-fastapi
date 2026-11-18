from sqlalchemy.ext.asyncio import create_async_engine , AsyncSession , async_sessionmaker
from sqlalchemy.orm import DeclarativeBase 
from config.settings import get_settings

settings = get_settings()

engine = create_async_engine(
    settings.DATABASE_URL
,
pool_size = 20, 
max_overflow =10 , 
pool_pre_ping =True, 
pool_recycle =1800
)

AsyncSessiosnLocal = async_sessionmaker(
    bind=engine , class_ = AsyncSession
        ,autoflush=False , expire_on_commit=False , 
)

class Base(DeclarativeBase):
     pass


async def get_db():
     async with AsyncSessiosnLocal() as session :
            try:
               yield session 
               session.commit()
            except Exception:
               session.rollback()
               raise
          
          