#File for settings  from .env
from dotenv import load_dotenv
import os


load_dotenv()

class Config:
  #DB setting
  DB_HOST = os.getenv("DB_HOST")
  DB_PORT = os.getenv("DB_PORT")
  DB_USER = os.getenv("DB_USER")
  DB_PASS = os.getenv("DB_PASS")
  DB_NAME = os.getenv("DB_NAME")

  #JWT settings
  SECRET_KEY_PATH=os.getenv("SECRET_KEY_PATH")
  PUBLIC_KEY_PATH=os.getenv("PUBLIC_KEY_PATH")
  JWT_ALGORITM=os.getenv("JWT_ALGORITM")
  ACCESS_TTL_MIN = 25
  
  def __init__(self) -> None:
    try:
      with open(self.SECRET_KEY_PATH,'r') as f:
        self.SECRET_KEY = f.read()
    except:
      exit(1)

    try:
      with open(self.PUBLIC_KEY_PATH,'r') as f:
        self.PUBLIC_KEY = f.read()
    except:
      exit(1)

CONFIG= Config()
