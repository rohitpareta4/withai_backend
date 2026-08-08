from schemas.todo_schema import TodoItems
from fastapi import APIRouter,Depends,Request
from core.dependencies import get_db
from sqlalchemy.orm import Session
from controllers.todo_controller import add_controller
from core.auth import get_curr_user


router=APIRouter(prefix="/todo")

@router.post("/Add")
def add_router(body:TodoItems,request:Request,db:Session=Depends(get_db)):
    user=get_curr_user(request,db)
    return add_controller(body,user,db)
