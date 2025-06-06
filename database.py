from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase
from config import CONFIG

DATABASE_URL = (
    f"postgresql://{CONFIG.DB_USER}:{CONFIG.DB_PASS}@{CONFIG.DB_HOST}:{CONFIG.DB_PORT}/{CONFIG.DB_NAME}"
)

engine = create_engine(DATABASE_URL,echo=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

class Base(DeclarativeBase):
    pass


