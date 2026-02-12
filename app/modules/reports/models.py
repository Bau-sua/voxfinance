import uuid
from enum import Enum
from typing import Mapped, List
from sqlalchemy import String, Boolean, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import mapped_column, relationship
from app.core.models import Base, TimestampMixin

class Status(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

class Report(Base, TimestampMixin):
    __tablename__ = "reports"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    filename: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[Status] = mapped_column(SQLEnum(Status), default=Status.PENDING)
    content_md: Mapped[str | None] = mapped_column(nullable=True)
    binned_insights: Mapped[dict | None] = mapped_column(nullable=True)

    user: Mapped["User"] = relationship(back_populates="reports")