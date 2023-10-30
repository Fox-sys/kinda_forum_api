from pydantic import BaseModel

from database.schemes.user_scheme import UserShortScheme


class ThreadShortScheme(BaseModel):
    id: int
    title: str
    short_description: str
    long_description: str
    auther: int
    rating: int


class ThreadFullScheme(BaseModel):
    id: int
    title: str
    short_description: str
    long_description: str
    auther: UserShortScheme
    rating: int
