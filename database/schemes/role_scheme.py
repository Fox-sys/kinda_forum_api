from pydantic import BaseModel


class RoleScheme(BaseModel):
    id: int
    title: str
    custom_role_color_scheme: str
    create_thread: bool
    create_comment: bool
    # По задумке имеются ввиду коменты других авторов
    delete_comment: bool
    # По задумке имеются ввиду треды других авторов
    delete_thread: bool
    # Не должен выдавать роли, разрешение которых не включены в действующую роль
    change_role: bool
    change_role_superuser: bool
    use_color_scheme: bool
    ban_user: bool
    change_own_prefix: bool
    change_other_prefix: bool
