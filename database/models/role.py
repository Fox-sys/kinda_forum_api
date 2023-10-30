from sqlalchemy import Column, Integer, String, Boolean

from database import Base


class Role(Base):
    __tablename__ = 'roles'

    id: int = Column(Integer, primary_key=True)
    title: str = Column(String, nullable=False)
    custom_role_color_scheme: str = Column(String, nullable=True)
    create_thread: bool = Column(Boolean, nullable=False)
    create_comment: bool = Column(Boolean, nullable=False)
    # По задумке имеются ввиду коменты других авторов
    delete_comment: bool = Column(Boolean, nullable=False)
    # По задумке имеются ввиду треды других авторов
    delete_thread: bool = Column(Boolean, nullable=False)
    # Не должен выдавать роли, разрешение которых не включены в действующую роль
    change_role: bool = Column(Boolean, nullable=False)
    change_role_superuser: bool = Column(Boolean, nullable=False)
    use_color_scheme: bool = Column(Boolean, nullable=False)
    ban_user: bool = Column(Boolean, nullable=False)
    change_own_prefix: bool = Column(Boolean, nullable=False)
    change_other_prefix: bool = Column(Boolean, nullable=False)
