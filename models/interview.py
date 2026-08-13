# from core.database import Base
# from sqlalchemy import Column,String,Integer,DateTime
# from sqlalchemy.sql import func
# from sqlalchemy.dialects.mysql import JSON
# from sqlalchemy import ForeignKey

# class Interview(Base):
#     __tablename__="InterviewInfo"

#     id=Column(Integer,primary_key=True,nullable=False)
#     user_id=Column(Integer,ForeignKey("userinfo.id"),nullable=False)

#     role=Column(String,nullable=False)
#     experience=Column(String,nullable=False)
#     difficulty=Column(String,nullable=False)
#     interviewType=Column(String,nullable=False)
#     questionCount=Column(Integer,nullable=False)
#     questions=Column(JSON,nullable=False)


from core.database import Base

from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    ForeignKey
)

from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import JSON


class Interview(Base):
    __tablename__ = "InterviewInfo"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("userinfo.id"),
        nullable=False
    )

    role = Column(String(100), nullable=False)

    experience = Column(String(50), nullable=False)

    difficulty = Column(String(30), nullable=False)

    interviewType = Column(String(30), nullable=False)

    questionCount = Column(Integer, nullable=False)

    questions = Column(JSON, nullable=False)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )


class GithubInterview(Base):
    __tablename__ = "GithubInterview"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("userinfo.id"))
    github_url = Column(String, nullable=False)


