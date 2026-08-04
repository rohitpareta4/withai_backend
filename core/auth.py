from sqlalchemy.orm import Session
from models.users import User
import jwt
from fastapi import HTTPException,Request
from core.config import settings

def get_curr_user(request:Request,db:Session):

    token=request.cookies.get("access_token")

    if not token:
        raise HTTPException(status_code=400,detail="token is exist")

    payload=jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])

    user_id=payload["_id"]

    user=db.query(User).filter(User.id==user_id).first()

    if not user:
        raise HTTPException(status_code=400,detail="token is exist")

    return user
