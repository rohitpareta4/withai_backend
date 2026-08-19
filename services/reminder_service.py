from sqlalchemy.orm import Session
from models.users import User
from services.todo_services import get_incompleteTodos
from services.email_service import send_todo_email

def send_daily_reminder(db:Session):
    print("Reminder started")

    users=db.query(User).all()


    for user in users:
        print("Checking:", user.id, user.email)
        incomplete_todos=get_incompleteTodos(user.id,db)

        if not incomplete_todos:
         continue

        send_todo_email("rockk7x@gmail.com",incomplete_todos)





