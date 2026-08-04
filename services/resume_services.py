from sqlalchemy.orm import Session
from schemas.resume_schema import Createresume,getresume
from models.resume import Resume
# from core.auth import get_curr_user;
from models.users import User
from fastapi import HTTPException

def Createresume_service(body:Createresume,user:User,db:Session):
    resume=Resume(
        user_id=user.id,
        title=body.title,
        template=body.template,
        resume_data=body.resume_data
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    return resume


def get_resume_service(user:User,db:Session):

    get_user_resume=db.query(Resume).filter(Resume.user_id==user.id).all()

    if not get_user_resume:
        raise HTTPException(status_code=400,detail="resume is not exist...")

    return get_user_resume

