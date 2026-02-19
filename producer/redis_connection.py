import redis
from pydantic_settings import BaseSettings
from pydantic import Field
from uuid import uuid4

class RedisConfig(BaseSettings):
    REDIS_HOST: str = Field('redis', alias='host') 
    REDIS_PORT: int = Field(6380, alias='port')
    REDIS_DB: int = Field(0, alias='db')
    REDIS_PASSWORD: str = Field('123456', alias='password')

    # class Config:
    #     env_file = ".env"
    #     env_file_encoding = "utf-8"


class RedisMsgQueue:
   
    _r = None

    @classmethod
    def connect(cls):
        config = RedisConfig().model_dump(by_alias=True)
        cls._r = redis.Redis(**config)


    @classmethod
    def push_queue(cls, queue_name, ttl, data):
        _id = str(uuid4())
        
        cls._r.lpush(queue_name, _id)
        cls._r.hmset(_id, data)
        cls._r.expire(_id, ttl)

