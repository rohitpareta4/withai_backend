from schemas.auth_schema import RegisterRequest
from sqlalchemy.orm import Session
from models.users import User
from fastapi import HTTPException
from utils.password import hashpass

def register_service(body:RegisterRequest,db:Session):

    existing_user=db.query(User).filter(User.email==body.email).first()

    if existing_user:
        raise HTTPException(status_code=404,detail="user with same email already exist")

    hass_pass=hashpass(body.password)

    new_user=User(
        name=body.name,
        email=body.email,
        password=hass_pass
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
    "message": "User registered successfully"
    }

    




