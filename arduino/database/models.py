from sqlalchemy.orm import Mapped, mapped_column

from arduino.database.config import Base


class Cards(Base):
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(unique=True, index=True, autoincrement=True)
    card: Mapped[str] = mapped_column(unique=True)
    is_blocked: Mapped[bool] = mapped_column(default=False)
