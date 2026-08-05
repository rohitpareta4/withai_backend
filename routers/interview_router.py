from fastapi import APIRouter,Request,Depends
from core.auth import get_curr_user
from schemas.interview_schema import Interview_create
from sqlalchemy.orm import Session
from core.dependencies import get_db
from controllers.interview_controller import interview_create_controller,getdetails_controller


router=APIRouter(prefix="/Interview")

@router.post("/session")
def interview_router(body:Interview_create,request:Request,db:Session=Depends(get_db)):
    user=get_curr_user(request,db)

    return interview_create_controller(body,user,db)


@router.get("/getdetails/{id}")
def getdetails_router(id:int,request:Request,db:Session=Depends(get_db)):
    user=get_curr_user(request,db)

    return getdetails_controller(id,user,db)

