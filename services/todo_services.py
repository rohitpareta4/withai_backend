from sqlalchemy.orm import Session
from schemas.todo_schema import TodoItems
from models.todo import Todo
from models.users import User

def add_service(body:TodoItems,user:User,db:Session):

    todo=Todo(
        user_id=user.id,
        title=body.title,
        completed=False
    )

    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo


