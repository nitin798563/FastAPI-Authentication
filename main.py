from fastapi import FastAPI
from database import engine
from models import Base
from jwt import router as authentication_router

app = FastAPI()

Base.metadata.create_all(bind = engine)

app.include_router(authentication_router, prefix= "/auth", tags=["Authentication Router"])