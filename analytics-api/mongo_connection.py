from pymongo import MongoClient


from pydantic_settings import BaseSettings
from pydantic import Field


class MongoConfig(BaseSettings):
    MONGO_URI: str = Field('mongodb://localhost:27017') 
    MONGO_DB: str = Field('dev')
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"



class MongoConnection:

    _client = None

    @classmethod
    def connect(cls):

        cls._client = MongoClient(
                    MongoConfig().MONGO_URI,
                    maxPoolSize=50,
                    serverSelectionTimeoutMS=5000,
                    connectTimeoutMS=10000
                )

        cls._client.admin.command("ping")

        
    @classmethod
    def close(cls):
        cls._client.close()
        

def get_db():
    db_name =  MongoConfig().MONGO_DB
    return MongoConnection._client.get_database(name=db_name)