from schemas.auth_schema import RegisterRequest
from sqlalchemy.orm import Session
from services.auth_services import register_service

def register(body:RegisterRequest,db:Session):
    return register_service(body,db)