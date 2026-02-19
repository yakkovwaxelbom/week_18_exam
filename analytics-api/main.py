from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager

from mongo_connection import MongoConnection 
from routes import route as alert_router

@asynccontextmanager
async def lifespan(app):
    MongoConnection.connect()
    yield
    MongoConnection.close()

app = FastAPI(lifespan=lifespan)

app.include_router(alert_router, prefix='/analytics')


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
