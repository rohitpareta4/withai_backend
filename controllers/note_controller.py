from schemas.note_schema import CreateNote
from sqlalchemy.orm import Session
from models.users import User
from services.note_service import addNote_service,getNote_service,deleteNote_service,editNote_service


def addNote_controller(body:CreateNote,user:User,db:Session):
    return addNote_service(body,user,db)

def getNote_controller(user:User,db:Session):
    return getNote_service(user,db)

def deleteNote_controller(id:int,user:User,db:Session):
    return deleteNote_service(id,user,db)

def editNote_controller(id:int,body:CreateNote,user:User,db:Session):
    return editNote_service(id,body,user,db)