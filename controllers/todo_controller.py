from sqlalchemy.orm import Session
from schemas.todo_schema import TodoItems,CompletedUpdateitem,titleUpdateitem
from models.users import User
from services.todo_services import add_service,getTdodo_service,updateCompleted_service,getupdatetodo_services,deleteTodo_service,updateTitle_service

def add_controller(body:TodoItems,user:User,db:Session):
    return add_service(body,user,db)

def getTdodo_controller(user:User,db:Session):
    return getTdodo_service(user,db)

def updateCompleted_controller(id:int,body:CompletedUpdateitem,user:User,db:Session):
    return updateCompleted_service(id,body,user,db)

def getupdatetodo_controller(user:User,db:Session):
    return getupdatetodo_services(user,db)

def deleteTodo_controller(id:int,user:User,db:Session):
    return deleteTodo_service(id,user,db)

def updateTitle_controller(id:int,body:titleUpdateitem,user:User,db:Session):
    return updateTitle_service(id,body,user,db)