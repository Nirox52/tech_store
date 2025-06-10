from pydantic import BaseModel,field_validator,EmailStr

from auth.utils import hash_password
from users.model import Role

class UserSchemaBase(BaseModel):
    email:EmailStr = 'test@test.com'
    role:Role = Role.ADMIN

class UserShema(UserSchemaBase):
    user_id: int

class UserShemaAuth(UserShema):
    password:str = 'test'

class UserShemaCreate(UserSchemaBase): #class for create user and auth
    password:str = 'test'

    @field_validator('password')
    def validate_password(cls,value:str):
        password = hash_password(value)
        return password
    

