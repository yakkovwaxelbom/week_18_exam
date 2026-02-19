import redis
from pydantic_settings import BaseSettings
from pydantic import Field


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
        cls._r = redis.Redis(**config, decode_responses=True)


    @classmethod
    def get_queue(cls, urgent_queue_name, normal_queue_name):
        _, _id = cls._r.brpop([urgent_queue_name, normal_queue_name])
        data = cls._r.hgetall(_id)

        return data
