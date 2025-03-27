from sqlalchemy import Table, Column, Integer, String
from database import metadata

reports = Table(
    "reports",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("filename", String(255)),
    Column("status", String(50)),
)
