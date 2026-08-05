from schemas.auth_schema import RegisterRequest,LoginRequest
from sqlalchemy.orm import Session
from services.auth_services import register_service,login_service,auth_service
from fastapi import Response
from fastapi import Request


def register(body:RegisterRequest,db:Session):
    return register_service(body,db)

def login(body:LoginRequest,response:Response,db:Session):
    data=login_service(body,db)

    # data.access_token

    response.set_cookie(
        key="access_token",
        value=data["access_token"],
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60*60*24*3
    )

    return {
        "message": data["message"]
    }

def auth(request:Request,db:Session):
    return auth_service(request,db)

     