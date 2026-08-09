from sqlalchemy.orm import Session
from schemas.todo_schema import TodoItems,CompletedUpdateitem,titleUpdateitem
from models.todo import Todo
from models.users import User
from fastapi import HTTPException


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

def getTdodo_service(user:User,db:Session):
    todos=db.query(Todo).filter(Todo.user_id==user.id).all()

    if not todos:
        raise HTTPException(status_code=400,detail="user is not exist")

    return todos

def updateCompleted_service(id:int,body:CompletedUpdateitem,user:User,db:Session):
    getTodo=db.query(Todo).filter(Todo.user_id==user.id).all()

    store=None
    
    for x in getTodo:
        if x.id==id:
            store=x
            break

    if store is None:
     raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )


    store.completed=not body.completed
    

    db.commit()
    db.refresh(store)

    return store


def getupdatetodo_services(user:User,db:Session):
    getUpdatetodo=db.query(Todo).filter(Todo.user_id==user.id).all()

    if not getUpdatetodo:
        raise HTTPException(status_code=400,detail="todo's are not present")

    return getUpdatetodo

def deleteTodo_service(id:int,user:User,db:Session):

    getTodo=db.query(Todo).filter(Todo.user_id==user.id).all()

    store=None

    for x in getTodo:
        if x.id==id:
            store=x
            break

    if not store:
        raise HTTPException(status_code=400,detail="not exist")

    db.delete(store)
    db.commit()

def updateTitle_service(id:int,body:titleUpdateitem,user:User,db:Session):
    getalltodos=db.query(Todo).filter(Todo.user_id==user.id)

    store=None

    for x in getalltodos:
        if x.id==id:
            store=x
            break

    if not store:
        raise HTTPException(status_code=400,detail="not exist")

    store.title=body.title

    db.commit()
    db.refresh(store)

    return store
            


