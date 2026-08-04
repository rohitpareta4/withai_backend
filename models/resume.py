from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.dialects.mysql import JSON
from sqlalchemy.sql import func
from core.database import Base

class Resume(Base):
    __tablename__="resumeinfo"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("userinfo.id"))

    title=Column(String(150),nullable=False)

    template=Column(String(150),nullable=False)

    resume_data=Column(JSON,nullable=False)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )