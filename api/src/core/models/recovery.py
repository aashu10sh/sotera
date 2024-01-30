from sqlalchemy import ForeignKey

from src.core.models.users import UserModel
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class RecoveryModel(Base):
    __tablename__ = "recoveries"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    phrase: Mapped[str] = mapped_column(nullable=False)

    # relationship

    user: Mapped[UserModel] = relationship(lazy="joined")
