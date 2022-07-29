from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    cards = relationship("Pairs", back_populates="owner")


class Pairs(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    cardA = Column(String, index=True)
    cardB = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="cards")
