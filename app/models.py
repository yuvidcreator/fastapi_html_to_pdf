from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData
from app.database import engine

metadata = MetaData()


reports = Table(
    "process_table",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("process_id", String(50), unique=True, index=True, nullable=False),
    Column("process_folder_name", String(255), unique=True, index=True, nullable=False),
    Column("process_status", String(50), nullable=False),
    Column("process_email", String(250), nullable=False),
    Column("process_status_message", String(50), nullable=False),
    Column("reg_date", DateTime, nullable=True),
    Column("reg_by", String(50), nullable=True),
)

