from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from src.core.models.users import UserModel
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column


class CredentialModel(Base):
    __tablename__ = "credentials"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    website: Mapped[str] = mapped_column(nullable=True)
    password: Mapped[str] = mapped_column(nullable=False)

    # relationship

    user: Mapped[UserModel] = relationship()
