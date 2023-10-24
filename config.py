from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    db_url:str = "sqlite:///database.db"
    n_concurrent:int = 5

@lru_cache() 
def get_settings():
    return Settings()
    
    
