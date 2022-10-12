# in-built
from uuid import uuid4

# 3rd party
from sqlalchemy import (
    Column, String, Boolean, DateTime, sql
)
from sqlalchemy.dialects.postgresql import UUID


# custom
from application import Base


class TodoList(Base):
    __tablename__ = "todolist"
    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True,
        nullable=False
    )
    created_at = Column(DateTime(timezone=True), default=sql.func.now())
    notes = Column(String, nullable=False)
    