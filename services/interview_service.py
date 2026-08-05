from schemas.interview_schema import Interview_create
from sqlalchemy.orm import Session
from models.users import User

def interview_create_service(body:Interview_create,user:User,db:Session):
    