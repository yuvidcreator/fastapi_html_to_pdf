from celery import Celery

celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    broker_connection_retry_on_startup = True
)

celery_app.autodiscover_tasks(['app.tasks'])
celery_app.conf.timezone = "UTC"
celery_app.conf.enable_utc = True


# celery_app.config_from_object('celeryconfig')


# celery_app.conf.task_routes = {"tasks.*": {"queue": "reports"}}
celery_app.conf.task_routes = {"tasks.add": {"queue": "reports"}}

celery_app.conf.update(
    worker_concurrency=4,  # 4 parallel tasks
    task_acks_late=True,    # Avoid duplicate processing
    result_expires=3600     # Auto-delete old results
)


'''
celery -A tasks worker --loglevel=INFO -E
'''
