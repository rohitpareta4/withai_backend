from schemas.todo_schema import TodoItems,CompletedUpdateitem,titleUpdateitem
from fastapi import APIRouter,Depends,Request
from core.dependencies import get_db
from sqlalchemy.orm import Session
from controllers.todo_controller import add_controller,getTdodo_controller,updateCompleted_controller,getupdatetodo_controller,deleteTodo_controller,updateTitle_controller
from core.auth import get_curr_user


router=APIRouter(prefix="/todo")

@router.post("/Add")
def add_router(body:TodoItems,request:Request,db:Session=Depends(get_db)):
    user=get_curr_user(request,db)
    return add_controller(body,user,db)


@router.get("/getTodos")
def getTdodo_router(request:Request,db:Session=Depends(get_db)):
    user=get_curr_user(request,db)
    return getTdodo_controller(user,db)

@router.post("/update/{id}")
def updateCompleted_router(id:int,body:CompletedUpdateitem,request:Request,db:Session=Depends(get_db)):
    user=get_curr_user(request,db)
    return updateCompleted_controller(id,body,user,db)

@router.get("/getupdateTodo")
def getupdatetodo_router(request:Request,db:Session=Depends(get_db)):
    user=get_curr_user(request,db)
    return getupdatetodo_controller(user,db)

@router.post("/deleteTodo/{id}")
def deleteTodo_router(id:int,request:Request,db:Session=Depends(get_db)):
    user=get_curr_user(request,db)
    return deleteTodo_controller(id,user,db)

@router.post("/updatetitle/{id}")
def updateTitle_router(id:int,body:titleUpdateitem,request:Request,db:Session=Depends(get_db)):
    user=get_curr_user(request,db)
    return updateTitle_controller(id,body,user,db)