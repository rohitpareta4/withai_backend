from sqlalchemy.orm import Session
from schemas.todo_schema import TodoItems
from models.users import User
from services.todo_services import add_service

def add_controller(body:TodoItems,user:User,db:Session):
    return add_service(body,user,db)