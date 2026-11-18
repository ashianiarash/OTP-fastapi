from sqlalchemy.orm import mapped_column , Mapped 
from database.database import Base 
from sqlalchemy import String  , Integer , Boolean, DateTime, func
from datetime import datetime 
class User(Base) :
    __tablename__ = 'users'

    id : Mapped[int] = mapped_column(Integer , primary_key=True ,autoincrement=True )
    hased_phone : Mapped[str] = mapped_column(String, unique=True ,nullable=False )
    is_active : Mapped[bool] = mapped_column(Boolean, default=True )
    is_admin : Mapped[bool] = mapped_column(Boolean , default=False)
    fullname : Mapped[str] = mapped_column(String(150) , nullable=True)
    created_at : Mapped[datetime] = mapped_column(DateTime(timezone=True) , server_default= func.now())
    updated_at : Mapped[datetime] = mapped_column(DateTime(timezone=True) , server_onupdate=func.now())
    