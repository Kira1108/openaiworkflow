from sqlalchemy import engine, create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from functools import wraps
from config import get_settings

settings = get_settings()

class Base(DeclarativeBase):
    pass

engine = create_engine(settings.db_url, echo=False)

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def inject_db(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        if "db" in kwargs:
            return func(*args, **kwargs)

        with next(get_db()) as session:
            return func(*args, db=session, **kwargs)
        
    return wrapper
