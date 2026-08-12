from schemas.note_schema import CreateNote
from sqlalchemy.orm import Session
from models.users import User
from services.note_service import addNote_service


def addNote_controller(body:CreateNote,user:User,db:Session):
    return addNote_service(body,user,db)