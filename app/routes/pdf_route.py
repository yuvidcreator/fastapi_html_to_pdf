import os
import time
import shutil
from fastapi import UploadFile, File, APIRouter
from starlette.responses import FileResponse

# from app.helper.utils import compress_pdf
from app.worker import celery_app
from app.tasks import generate_pdf_task


route = APIRouter() 




# Upload XLSX & generate PDF
@route.post("/upload-file/")
async def create_report(file: UploadFile = File(...)):
    file_path = f"temp/{file.filename}"
    output_pdf = f"reports/final_report.pdf"

    try:
        # Save file
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        # Run Celery task
        # task = generate_pdf_task.apply_async(args=[file_path, output_pdf])
        # print(task)
        # return {"message": "Report generation started", "task_id": task.id}
        
        start_time = time.time()
        output = generate_pdf_task(file_path, output_pdf)
        print(output)
        # compress_pdf(output)
        end_time = time.time()
        total_time: float = end_time-start_time
        print(f"Total time taken : {total_time: .2f}")

        return {"message": "Report generated successfully.", "total_time": {total_time}}
    except Exception as e:
        return {"Exception details": f"{e}"}



# Check task status
@route.get("/task-status/{task_id}")
def get_task_status(task_id: str):
    task = celery_app.AsyncResult(task_id)
    return {"task_id": task_id, "status": task.status}



# Download generated PDF
@route.get("/download-pdf/")
def download_pdf():
    file_path = "reports/final_report.pdf"
    if os.path.exists(file_path):
        return FileResponse(
            file_path, 
            media_type="application/pdf", 
            filename="final_report.pdf"
        )
    return {"error": "PDF Report not found"}
