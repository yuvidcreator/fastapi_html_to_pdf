import os
import shutil
from typing import Annotated
from fastapi import UploadFile, File, BackgroundTasks
# from fastapi.responses import FileResponse
from starlette.responses import FileResponse
from celery.result import AsyncResult

from main import app
from app.tasks import generate_pdf_task




async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}



# Upload XLSX & generate PDF
@app.post("/generate-pdf/")
async def create_report(file: UploadFile = File(...), background_tasks: BackgroundTasks = None):
    file_path = f"temp/{file.filename}"
    output_pdf = f"reports/final_report.pdf"

    try:
        # Save file
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        # Run Celery task
        task = generate_pdf_task.apply_async(args=[file_path, output_pdf])
        # task = generate_pdf_task(file_path=file_path, output_filename=output_pdf)

        print(task)

        return {"message": "Report generation started", "task_id": task.id}
    except Exception as e:
        return {"details": f"{e}"}



# Check task status
@app.get("/task-status/{task_id}")
def get_task_status(task_id: str):
    # task = celery_app.AsyncResult(task_id)
    task = AsyncResult(task_id)
    return {"task_id": task_id, "status": task.status}



# Download generated PDF
@app.get("/download-pdf/")
def download_pdf():
    file_path = "reports/final_report.pdf"
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="application/pdf", filename="final_report.pdf")
    return {"error": "PDF not found"}
