import redis
import json
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

class RedisCashing:
    config = RedisConfig().model_dump(by_alias=True)
    _r = redis.Redis(**config)
    
    def __init__(self, expire, key_gen = None):
        self._expire = expire
        self._key_gen = key_gen

    def __call__(self, func):
        def wrapper(*args):

            key = self._key_gen(args) if self._key_gen else \
                f"{func.__name__}:{':'.join(map(str, args[1:]))}"
            
            cached = RedisCashing._r.get(key)

            if cached is not None:
                return json.loads(cached)
            
            res = func(*args)

            for doc in res:
                if (_id := doc.get('_id', None)) is not None:
                    doc['_id'] = str(_id)

            RedisCashing._r.setex(key, self._expire, json.dumps(res))

            return res
        return wrapper
    