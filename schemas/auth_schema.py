from pydantic import BaseModel,EmailStr,Field
from typing import Annotated

class RegisterRequest(BaseModel):
    name:Annotated[str,Field(...,max_length=50,description="User name")]
    email:EmailStr
    password:Annotated[str,Field(...,min_length=8,max_length=20)]

class LoginRequest(BaseModel):
    email:EmailStr
    password:Annotated[str,Field(...,min_length=8,max_length=20)]
