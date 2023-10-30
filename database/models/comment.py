from sqlalchemy import Column, Integer, String, Text, ForeignKey

from database import Base


class Comment(Base):
    __tablename__ = 'comments'

    id: int = Column(Integer, primary_key=True)
    text: str = Column(Text, nullable=False)
    auther: int = Column(Integer, ForeignKey('users.id'), nullable=False)
    thread: int = Column(Integer, ForeignKey('threads.id'), nullable=False)
    upper_comment: int = Column(Integer, ForeignKey('comments.id'), nullable=True)
    rating: int = Column(Integer, default=0)
