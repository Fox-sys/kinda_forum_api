from sqlalchemy import Column, Integer, String, Text, ForeignKey

from database import Base


class Thread(Base):
    __tablename__ = 'threads'

    id: int = Column(Integer, primary_key=True)
    title: str = Column(String, nullable=False)
    short_description: str = Column(Text, nullable=False)
    long_description: str = Column(Text, nullable=False)
    auther: int = Column(Integer, ForeignKey('users.id'), nullable=False)
    rating: int = Column(Integer, default=0)
