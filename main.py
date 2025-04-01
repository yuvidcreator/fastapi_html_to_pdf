import os
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager
from typing import Annotated

from app.database import SessionLocal, engine
import app.models as models
from app.routes.pdf_route import route as pdf_routes



# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # scheduler = AsyncIOScheduler(timezone=f'{your_timezone}')
#     # repeat task every 10 seconds
#     # scheduler.add_job(func=repeat_task, trigger='interval', seconds=10)
#     # scheduler.start()
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# app = FastAPI(lifespan=lifespan)
app = FastAPI()


models.metadata.create_all(bind=engine)


db_dependency = Annotated[Session, Depends(get_db)]

# Configuration
TEMP_DIR = "temp"
TEMPLATE_DIR = "templates"
STATIC_DIR = "static"
OUTPUT_DIR = "reports"

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(pdf_routes)

