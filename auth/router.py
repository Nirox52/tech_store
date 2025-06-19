from fastapi import APIRouter, Depends, Form, HTTPException, status
from jwt.exceptions import InvalidTokenError
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from auth.crud import add_user, get_user_by_email
from auth.token import Token
from auth.utils import check_password, decode_jwt, encode_jwt
from users.schema import UserShemaAuth, UserShemaCreate
from sqlalchemy.orm import Session
from database import SessionLocal

http_bearer = HTTPBearer()

router = APIRouter(prefix="/jwt",tags=["JWT"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def validate_user(email:str=Form(),password:str=Form(),db: Session = Depends(get_db)):
    exception = HTTPException(status.HTTP_401_UNAUTHORIZED,detail='Invalid email or password')
    user = get_user_by_email(db,email)
    if not user:
        raise exception
    if check_password(user.password,password):
        return user
    raise exception

def validate_auth_user(token_credentials:HTTPAuthorizationCredentials=Depends(http_bearer),db: Session = Depends(get_db)):
    token = token_credentials.credentials
    try:
        data = decode_jwt(token)
    except InvalidTokenError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,detail='Invalid token')

    user = get_user_by_email(db,data.get('email'))
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,'Invalid token')
    return user
    


@router.post('/register/',response_model=UserShemaCreate)
def register_user(user:UserShemaCreate,
                  db: Session = Depends(get_db)):
    add_user(db,user)
    return user

@router.post('/login/',response_model=Token)
def auth_user(user:UserShemaAuth=Depends(validate_user),
              db: Session = Depends(get_db)):
    data={"user_id":user.user_id,
          "email":user.email}
    token = encode_jwt(data)
    return Token(token=token,token_type='Bearer')

@router.get('/user/me/')
def get_me(user:UserShemaAuth = Depends(validate_auth_user)):
    return {"email":user.email,"role":user.role}
