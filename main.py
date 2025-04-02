import os
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import Annotated

from app.database import SessionLocal, engine
import app.models as base_models
from app.routes.pdf_route import route as pdf_routes



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

