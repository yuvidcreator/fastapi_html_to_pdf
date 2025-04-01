import os
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy.orm import Session
# from contextlib import asynccontextmanager
from typing import Annotated

from app.database import SessionLocal, engine
import app.models as base_models
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

# app = FastAPI(lifespan=lifespan)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(
    title="PDF Generation Backend",
    description="This is to test",
)


# models.metadata.create_all(bind=engine)
base_models.metadata.create_all(bind=engine)


db_dependency = Annotated[Session, Depends(get_db)]

# Configuration
TEMP_DIR = "temp"
TEMPLATE_DIR = "templates"
STATIC_DIR = "static"
OUTPUT_DIR = "reports"
COMPRESSED_PDF_DIR = "compressed_pdfs"
INPUT_DATA_DIR = "input_data"

os.makedirs(STATIC_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(INPUT_DATA_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(COMPRESSED_PDF_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(pdf_routes)

