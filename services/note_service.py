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

      print("NOTES FROM DB:")
      for n in Takenotes:
        print(n.id, n.title, n.note)

      if not Takenotes:
            raise HTTPException(status_code=400,detail="notes are not exist")

      return Takenotes


def deleteNote_service(id:int,user:User,db:Session):
     note=db.query(Note).filter(Note.user_id==user.id,Note.id==id).first()

     if not note:
      raise HTTPException(
        status_code=404,
        detail="Note not found"
    )

     db.delete(note) 
     db.commit()

     return {"message": "Note deleted successfully"}


def editNote_service(id:int,body:CreateNote,user:User,db:Session):
    getNote=db.query(Note).filter(Note.user_id==user.id,Note.id==id).first()

    if not getNote:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    getNote.title=body.title
    getNote.note=body.note

    db.commit()
    db.refresh(getNote)

    return getNote
     

    

