from schemas.auth_schema import RegisterRequest,LoginRequest
from sqlalchemy.orm import Session
from services.auth_services import register_service,login_service

def register(body:RegisterRequest,db:Session):
    return register_service(body,db)

def login(body:LoginRequest,db:Session):
    return login_service(body,db)