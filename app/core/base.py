from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from sqlalchemy import Column, Integer

class HealthCheck(Base):
    __tablename__ = "health_checks"
    id = Column(Integer, primary_key=True)

# Future module imports for Alembic scanning
# from app.auth.models import *
# from app.banking.models import *
# from app.shared.models import *