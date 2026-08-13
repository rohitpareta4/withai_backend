from schemas.interview_schema import Interview_create,git_create
from sqlalchemy.orm import Session
from models.users import User
# from services.interview_service interviewcreate_service
from services.interview_service import interviewcreate_service,getdetails_service,git_service

def interview_create_controller(body:Interview_create,user:User,db:Session):
    return interviewcreate_service(body,user,db)

def getdetails_controller(id:int,user:User,db:Session):
    return getdetails_service(id,user,db)

def git_controller(body:git_create,user:User,db:Session):
    return git_service(body,user,db)