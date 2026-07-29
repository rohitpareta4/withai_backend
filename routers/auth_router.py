from fastapi import APIRouter,Depends
from schemas.auth_schema import RegisterRequest,LoginRequest
from core.dependencies import get_db
from controllers.auth_controller import register,login,auth
from sqlalchemy.orm import Session
from fastapi import Response
from fastapi import Request


router=APIRouter(prefix="/auth")

@router.post("/register")
def register_user(body:RegisterRequest,db:Session=Depends(get_db)):
    return register(body,db)

@router.post("/login")
def login_user(body:LoginRequest,response:Response,db:Session=Depends(get_db)):
    return login(body,response,db)

@router.get("/authme")
def auth_user(request:Request,db:Session=Depends(get_db)):
    return auth(request,db)