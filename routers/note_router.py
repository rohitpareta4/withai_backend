from schemas.note_schema import CreateNote
from fastapi import APIRouter,Depends,Request
from core.dependencies import get_db
from sqlalchemy.orm import Session
from core.auth import get_curr_user
from controllers.note_controller import addNote_controller,getNote_controller

router=APIRouter(prefix="/note")

@router.post("/addnote")
def addNote_router(body:CreateNote,request:Request,db:Session=Depends(get_db)):
    user=get_curr_user(request,db)
    return addNote_controller(body,user,db)

@router.get("/getNote")
def getNote_router(request:Request,db:Session=Depends(get_db)):
    user=get_curr_user(request,db)
    return getNote_controller(user,db)
