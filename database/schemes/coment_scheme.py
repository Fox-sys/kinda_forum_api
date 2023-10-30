from pydantic import BaseModel

from database.schemes.thread_scheme import ThreadShortScheme
from database.schemes.user_scheme import UserShortScheme


class CommentShortScheme(BaseModel):
    id: int
    text: str
    auther: int
    thread: int
    upper_comment: int
    rating: int


class CommentFullScheme(BaseModel):
    id: int
    text: str
    auther: UserShortScheme
    thread: ThreadShortScheme
    upper_comment: CommentShortScheme
    rating: int
