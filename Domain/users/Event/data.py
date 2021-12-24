from DependencyInjection.build_dependencies import get_dependencies
from Domain.users.Model.user_entities import UserModel
from Domain.users.Service.user_service import add_user, delete_user, get_user, get_users
from passlib.context import CryptContext
from Resources.config.environment import get_settings
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
user = get_dependencies().user
_SETTINGS = get_settings()

class UserWorking:
    def add(self, data_user: UserModel):
        add_user(user, data_user)

    def get(self):
        return get_users(user)

    def delete(self, id: int):
        delete_user(user, id)

    def get_user_one(self, email):
        return get_user(user, email)
    
# =========================================================================

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

# =========================================================================

def authenticate_user(email: str, password: str):
    user_db = UserWorking()
    us = user_db.get_user_one(email)
    if not us:
        return False
    user = UserModel.from_orm(us)
    if not verify_password(password, user.password_user):
        return False
    return user

# =========================================================================

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=_SETTINGS.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, _SETTINGS.JWT_SECRET_KEY, algorithm=_SETTINGS.JWT_ALGORITHM)
    return encoded_jwt

# =========================================================================

def hash_password(password: str):
    return pwd_context.hash(password)