import enum

from sqlalchemy import Column, Integer, String, Enum, Text, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

from database import engine

Base = declarative_base()


class Role(enum.Enum):
    PRINCIPAL = "Principal"
    MATH_TEACHER = "Math_Teacher"
    ENGLISH_TEACHER = "English_Teacher"
    SCIENCE_TEACHER = "Science_Teacher"
    HISTORY_TEACHER = "History_Teacher"
    COMPUTER_TEACHER = "Computer_Teacher"
    STUDENT = "Student"


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(Enum(Role), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"


def init_db():
    Base.metadata.create_all(bind=engine)
