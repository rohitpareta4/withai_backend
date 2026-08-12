from schemas.note_schema import CreateNote
from sqlalchemy.orm import Session
from models.users import User
from models.notes import Note

def addNote_service(body:CreateNote,user:User,db:Session):
      new_note = Note(
        user_id=user.id,
        note=body.note
    )

      db.add(new_note)
      db.commit()
      db.refresh(new_note)

      return new_note
    

