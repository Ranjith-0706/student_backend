from datetime import datetime
from typing import List
from pydantic import BaseModel, EmailStr, constr
from bson.objectid import ObjectId
from typing import Optional
from enum import Enum

class Role(str, Enum):
    ADMIN = "admin"
    STAFF = "staff"
    STUDENT = "student"
    
class UserBaseSchema(BaseModel):
    user_id: Optional[str] = None
    name: str
    email: str
    role: Role 
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    status: Optional[int] = 0
    delete: Optional[int] = 0
    archive: Optional[int] = 0

    class Config:
        orm_mode = True


# class CreateUserSchema(UserBaseSchema):
#     password: constr(min_length=8)
#     passwordConfirm: str
#     verified: bool = True

class CreateUserNewSchema(UserBaseSchema):
    name: str
    password: constr(min_length=8) # type: ignore
    mob_no: str
    email:str
    cntr_name: str
    univ_id: str
    verified: bool = False

class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8) # type: ignore


class UserResponseSchema(UserBaseSchema):
    id: str
    pass


class UserResponse(BaseModel):
    status: str
    user: UserBaseSchema


class FilteredUserResponse(UserBaseSchema):
    id: str



