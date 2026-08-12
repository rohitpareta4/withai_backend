from schemas.note_schema import CreateNote
from sqlalchemy.orm import Session
from models.users import User
from models.notes import Note
from fastapi import HTTPException


def addNote_service(body:CreateNote,user:User,db:Session):
      new_note = Note(
        user_id=user.id,
        note=body.note,
        title=body.title
    )

      db.add(new_note)
      db.commit()
      db.refresh(new_note)

      return new_note

def getNote_service(user:User,db:Session):
      Takenotes=db.query(Note).filter(Note.user_id==user.id).all()

      if not Takenotes:
            raise HTTPException(status_code=400,detail="notes are not exist")

      return Takenotes

    

