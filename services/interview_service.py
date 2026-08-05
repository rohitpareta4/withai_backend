from schemas.interview_schema import Interview_create
from sqlalchemy.orm import Session
from models.users import User
from models.interview import Interview
from fastapi import HTTPException
from services.gemini_service import generate_questions


def interviewcreate_service(body:Interview_create,user:User,db:Session):
    questions = generate_questions(body)
    interview=Interview(
        user_id=user.id,
        role=body.role,
        experience=body.experience,
        difficulty=body.difficulty,
        interviewType=body.interviewType,
        questionCount=body.questionCount,
        questions=questions
    )

    db.add(interview)
    db.commit()
    db.refresh(interview)

    return {
    "message": "Interview created successfully",
    "interviewId": interview.id
    }

def getdetails_service(interview_id:int,user:User,db:Session):

     interview = (
        db.query(Interview)
        .filter(
            Interview.id == interview_id,
            Interview.user_id == user.id
        )
        .first()
    )

    
     if not interview:
        raise HTTPException(status_code=400,detail="user is not found")


     return interview;

    