from fastapi import status, HTTPException, Depends
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from Domain.users.Event.data import UserWorking, authenticate_user, create_access_token, hash_password
from Domain.users.Model.user_entities import LogIn, UserModel, UserRegisterModel

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from Resources.config.environment import get_settings
from datetime import datetime, timedelta

# =========================================================================
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1.0/users/login")
_SETTINGS = get_settings()
# =========================================================================

router = APIRouter()

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, _SETTINGS.JWT_SECRET_KEY, algorithms=[_SETTINGS.JWT_ALGORITHM])
        email_user: str = payload.get("email_user")
        if email_user is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = UserWorking().get_user_one(email_user)
    if user is None:
        raise credentials_exception
    return user

class Token(BaseModel):
    access_token: str
    token_type: str

@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"email_user": user.email_user}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/")
async def read_users_me(current_user: LogIn = Depends(get_current_user)):
    return current_user

@router.get(
    '/get_all_users',
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
    responses={
        200: {'description': 'Usuarios obtenidos con exito'},
        400: {'description': 'Error al obtener los usuarios'}
    }
)
async def get_all_users(current_user: LogIn = Depends(get_current_user)):
    user_working = UserWorking()
    return user_working.get()

@router.post(
    '/add_user',
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
    responses={
        200: {'description': 'Usuario agregado con exito'},
        400: {'description': 'Error al agregar el usuario'}
    }
)
async def add_new_user_db(
    data: UserRegisterModel,
    current_user: LogIn = Depends(get_current_user)
):
    user_working = UserWorking()
    if user_working.get_user_one(data.email_user):
        return { 'ok': False, 'detail': 'Ya existe un usuario con este correo', 'code': 400 }
    data.password_user = hash_password(data.password_user)
    user_working.add(data)
    return user_working.get_user_one(data.email_user)

@router.delete(
    '/delete_user/{id_user}',
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
    responses={
        200: {'description': 'Usuario agregado con exito'},
        400: {'description': 'Error al agregar el usuario'}
    }
)
async def delete_user_db(id_user: int, current_user: LogIn = Depends(get_current_user)):
    user_working = UserWorking()
    user_working.delete(id_user)