from schemas.interview_schema import Interview_create
from sqlalchemy.orm import Session
from models.users import User
from services.interview_service interview_create_service

def interview_create_controller(body:Interview_create,user:User,db:Session):
    return interview_create_service(body,user,db)