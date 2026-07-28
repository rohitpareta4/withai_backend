from schemas.auth_schema import RegisterRequest,LoginRequest
from sqlalchemy.orm import Session
from models.users import User
from fastapi import HTTPException
from utils.password import hashpass,verify_pass
from core.config import settings
from datetime import datetime, timedelta
import jwt

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

def login_service(body:LoginRequest,db:Session):

    email_exist=db.query(User).filter(User.email==body.email).first()

    if not email_exist:
        raise HTTPException(status_code=400,detail="user is not exist....")

    password_verify=verify_pass(body.password,email_exist.password)

    if not password_verify:
        raise HTTPException(status_code=400,detail="password is invalid....")

    payload = {
    "_id": email_exist.id,
    "exp": datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
}

    token = jwt.encode(
    payload,
    settings.SECRET_KEY,
    algorithm=settings.ALGORITHM
)

    return {"token":token,"message":"login succesfully..."}

    




