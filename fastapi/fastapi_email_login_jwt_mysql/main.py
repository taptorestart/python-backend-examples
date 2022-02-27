from fastapi import FastAPI

from app.api.api import api_router
from app.core.config import settings
from app.db.session import SessionLocal
from app.db.init_db import init_db


# Create first super user
def init() -> None:
    db = SessionLocal()
    init_db(db)


app = FastAPI()
app.include_router(api_router, prefix=settings.API_V1_STR)
init()
