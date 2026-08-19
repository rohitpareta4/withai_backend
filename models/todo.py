from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,DateTime
from datetime import datetime
from core.database import Base

class Todo(Base):
    __tablename__="TodoData"

    id=Column(Integer,primary_key=True,index=True)

    user_id=Column(Integer,ForeignKey("userinfo.id"),nullable=False)

    title=Column(String(100),nullable=False)

    completed=Column(Boolean,nullable=False,default=False)

    createdAt = Column(
         DateTime,
        default=datetime.utcnow,
        nullable=False
    )
