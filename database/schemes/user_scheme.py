from pydantic import BaseModel

from database.schemes.role_scheme import RoleScheme


class UserShortScheme(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    is_active: bool
    is_superuser: bool
    register_date: str
    custom_role_prefix: str
    custom_role_color_scheme: str
    role: int


class UserFullScheme(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    is_active: bool
    is_superuser: bool
    register_date: str
    custom_role_prefix: str
    custom_role_color_scheme: str
    role: RoleScheme
