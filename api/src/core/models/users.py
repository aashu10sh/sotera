from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

SessionModel = "SessionModel"


class UserModel(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)
    key: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(nullable=True)

    # relationship
    sessions: Mapped[SessionModel] = relationship(back_populates="user")  # type:ignore
