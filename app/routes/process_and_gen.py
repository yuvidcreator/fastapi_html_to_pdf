from datetime import datetime
import os
import time
from fastapi import UploadFile, File, HTTPException, status
from main import db_dependency

from app.crud.query import DbQuery



async def process_and_generate_pdf(db: db_dependency, process_email: str, file: UploadFile=File(...)):
    # Check if the file has a valid name
    if process_email is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email ID is required.",
        )
    filename = file.filename
    if not filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The uploaded file must have a valid filename.",
        )
    file_ext = os.path.splitext(filename)[1].lower()
    start_time = time.time()
    
    order_key_prefix = "PC"
    # Get the current year and month
    current_year = datetime.now().strftime('%y')
    current_month = datetime.now().strftime('%m')

    query_data = DbQuery.get_existing_order(db, payload = order_key_prefix + current_year + current_month)

    if query_data:
        # Get the maximum numeric part from the existing orders
        max_numeric_part = max(int(order.process_id[len(order_key_prefix) + 4:]) for order in query_data)

        # Increment the numeric part
        order_key_numeric = max_numeric_part + 1
    else:
        # If no existing orders, initialize order_key_numeric to 1
        order_key_numeric = 1