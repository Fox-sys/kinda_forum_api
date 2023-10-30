from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey

from database import Base


class User(Base):
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True, unique=True, nullable=False)
    username: str = Column(String, unique=True, nullable=False)
    email: str = Column(String, unique=True, nullable=False)
    first_name: str = Column(String, nullable=False)
    last_name: str = Column(String, nullable=True)
    password: str = Column(String, nullable=False)
    is_active: bool = Column(Boolean, default=True)
    is_superuser: bool = Column(Boolean, default=False)
    register_date: str = Column(TIMESTAMP, default=datetime.utcnow)
    custom_role_prefix: str = Column(String, nullable=True)
    custom_role_color_scheme: str = Column(String, nullable=True)
    role: int = Column(Integer, ForeignKey('roles.id'))
