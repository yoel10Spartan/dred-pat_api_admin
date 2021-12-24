from pydantic import BaseModel, Field
from typing import Optional
from Resources.helpers.generate_id import GenerateID, IDInt

class IdModel(BaseModel):
    id: int

class UserRegisterModel( BaseModel ):
    email_user: str
    name_user: str
    password_user: str
    url_photo_user: str

    class Config:
        orm_mode = True

class UserModel( UserRegisterModel, IdModel ):
    ...

class LogIn(BaseModel):
    email_user: str
    password_user: str

    class Config:
        orm_mode = True