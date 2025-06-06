from pydantic import BaseModel

class UserSchemaBase(BaseModel):
    email:str
    role:str

class UserShema(UserSchemaBase):
    user_id: int

class UserShemaCreate(UserShema): #class for create user and auth
    password:str

