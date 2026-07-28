from fastapi import APIRouter,Depends
from schemas.auth_schema import RegisterRequest
from core.dependencies import get_db
from controllers.auth_controller import register
from sqlalchemy.orm import Session


router=APIRouter(prefix="/auth")

@router.post("/register")
def register_user(body:RegisterRequest,db:Session=Depends(get_db)):
    return register(body,db)