from pydantic import BaseModel,field_validator,EmailStr

from auth.utils import hash_password

class UserSchemaBase(BaseModel):
    # email:str
    email:EmailStr
    role:str

class UserShema(UserSchemaBase):
    user_id: int

class UserShemaAuth(UserShema):
    password:str

class UserShemaCreate(UserSchemaBase): #class for create user and auth
    password:str

    @field_validator('password')
    def validate_password(cls,value:str):
        password = hash_password(value)
        return password
    

