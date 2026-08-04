from sqlalchemy.orm import Session
from schemas.resume_schema import Createresume,getresume
from services.resume_services import Createresume_service,get_resume_service
from models.users import User

def create_resume(body:Createresume,user:User,db:Session):
    return Createresume_service(body,user,db);

def get_resume_controller(user:User,db:Session):
    return get_resume_service(user,db);
