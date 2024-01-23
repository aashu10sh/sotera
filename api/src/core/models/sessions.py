from sqlalchemy import ForeignKey
from src.core.models.users import UserModel
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


class SessionModel(Base):
    __tablename__ = "sessions"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    key: Mapped[str] = mapped_column(nullable=False)
    expires_at: Mapped[datetime] = mapped_column(nullable=False)

    # relationship
    user: Mapped[UserModel] = relationship(back_populates="sessions", lazy="joined")
