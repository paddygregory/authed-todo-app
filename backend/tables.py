from sqlalchemy import create_engine, Column, UUID, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from uuid import uuid4
from datetime import datetime, func

engine = create_engine("sqlite:///todo.db")

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

class User(Base):
    __tablename__ = "users"
    id = Column(UUID, primary_key=True, default=uuid4)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    status = Column(String, default="active")
    created_at = Column(datetime, default=func.now())
    updated_at = Column(datetime, default=func.now(), onupdate=func.now())

    todos = relationship("Todo", back_populates="owner")

class ToDo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False)

    owner_id = Column(UUID, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="todos")

class RefreshTokens(Base):
    __tablename__ = "refresh_tokens"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey=("users.id"), ondelete="CASCADE"), nullable=False
    token_hash = Column(String(64), nullable=False, unique=True)
    created_at = Column(datetime(timezone=True), server_default=func.now(), nullable=False)
    expires_at = 

