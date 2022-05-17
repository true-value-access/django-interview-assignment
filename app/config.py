from pydantic import BaseSettings
class Settings(BaseSettings):
    DATABASE_NAME:str
    HOST_NAME:str
    USER_NAME:str
    USER_PASSWORD:str
    SECRETKEY:str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int
    SECURITYHHTPS:bool
    SAMESITE:str
    ORIGINS:str=[]
    class Config:
        env_file=".env"

settings=Settings()