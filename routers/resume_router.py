from fastapi import APIRouter,Depends,Request
from core.dependencies import get_db
from schemas.resume_schema import Createresume,getresume
from sqlalchemy.orm import Session
from controllers.resume_controller import create_resume,get_resume_controller
from core.auth import get_curr_user

router=APIRouter(prefix="/resume")

@router.post("/create")
def createresume(body:Createresume,request:Request,db:Session=Depends(get_db)):
    user=get_curr_user(request,db)
    return create_resume(body,user,db)

@router.get("/getresume")
def get_resume(request:Request,db:Session=Depends(get_db)):
    user=get_curr_user(request,db)
    return get_resume_controller(user,db)