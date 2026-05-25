from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from utils.setting import setting


engine = create_engine(setting.db_connection)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
