import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
from contextlib import asynccontextmanager

from app.database import SessionLocal, engine
import app.models as models



@asynccontextmanager
async def lifespan(app: FastAPI):
    # scheduler = AsyncIOScheduler(timezone=f'{your_timezone}')
    # repeat task every 10 seconds
    # scheduler.add_job(func=repeat_task, trigger='interval', seconds=10)
    # scheduler.start()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


models.metadata.create_all(bind=engine)


app = FastAPI(lifespan=lifespan)

# Configuration
TEMPLATE_DIR = "temp"
TEMPLATE_DIR = "templates"
STATIC_DIR = "assets"
OUTPUT_DIR = "reports"

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")


