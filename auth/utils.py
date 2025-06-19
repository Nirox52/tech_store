from datetime import datetime, timedelta
from fastapi import HTTPException, status
import jwt
import bcrypt
from config import CONFIG
from users.model import Role

WORKERS_DICT=[Role.ADMIN,Role.SELLER,Role.CONSULTANT]

def encode_jwt(data:dict,token_timedelta:timedelta|None=None):
    now = datetime.utcnow()
    if token_timedelta:
        expire = now+token_timedelta
    else:
        expire = now+timedelta(minutes=int(CONFIG.ACCESS_TTL_MIN))
    data.update(exp=expire,iat=now)
    token = jwt.encode(data,CONFIG.SECRET_KEY,algorithm=CONFIG.JWT_ALGORITM)
    return token

def decode_jwt(token:str):
    token = jwt.decode(token,CONFIG.PUBLIC_KEY,algorithms=CONFIG.JWT_ALGORITM)
    return token

def hash_password(password:str):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(),salt)

def check_password(hashed_password:bytes,password:str):
    return bcrypt.checkpw(password.encode(),hashed_password)

def check_if_user_is_worker(user,detail='Forbidden'):
    if user.role not in WORKERS_DICT:
        raise HTTPException(status.HTTP_403_FORBIDDEN,detail=detail)

