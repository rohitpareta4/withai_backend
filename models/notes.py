from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from core.database import Base


class Note(Base):
    __tablename__ = "Noteinfo"

    id = Column(
        Integer,
        primary_key=True,
        unique=True
    )

    user_id = Column(
        Integer,
        ForeignKey("userinfo.id"),
        nullable=False
    )

    note = Column(
        String(10000),
        nullable=False
    )