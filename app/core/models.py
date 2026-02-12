from datetime import datetime
from typing import Self
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        default=func.utcnow(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=func.utcnow(), onupdate=func.utcnow(), nullable=False
    )

class Base(DeclarativeBase):
    __abstract__ = True