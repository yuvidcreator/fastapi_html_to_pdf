


# Start Celery
celery -A app.tasks worker --loglevel=INFO -E

# Start Uvicorn
uvicorn main:app --reload