from pydantic_settings import BaseSettings
from typing import ClassVar
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os
load_dotenv()

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    
    API_V1_STR: str = '/api/v1'
    DB_URL: str = f"mysql+aiomysql://{str(os.getenv('USER'))}:{str(os.getenv('PASS'))}@localhost:3306/faculdade"
    DBBaseModel: ClassVar = declarative_base()
    
    class Config:
        case_sensitive = True
        
        
settings = Settings()
    