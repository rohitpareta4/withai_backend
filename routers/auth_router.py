from fastapi import APIRouter,Depends
from schemas.auth_schema import RegisterRequest,LoginRequest
from core.dependencies import get_db
from controllers.auth_controller import register,login
from sqlalchemy.orm import Session


router=APIRouter(prefix="/auth")

@router.post("/register")
def register_user(body:RegisterRequest,db:Session=Depends(get_db)):
    return register(body,db)

@router.post("/login")
def login_user(body:LoginRequest,db:Session=Depends(get_db)):
    return login(body,db)