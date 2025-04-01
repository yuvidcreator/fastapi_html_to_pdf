from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData
from app.database import engine

metadata = MetaData()

# reports = Table(
#     "reports",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("filename", String(255)),
#     Column("status", String(50)),
# )

'''
# # As per Payal DB
# class ProcessTable(Base):
#     __tablename__ = 'process_table'
    
#     id = Column(Integer, primary_key=True, index=True)
#     process_id = Column(String(50), unique=True, index=True, nullable=False)
#     process_folder_name = Column(String(50), unique=True, index=True, nullable=False)
#     process_status = Column(String(50), nullable=False)
#     process_email = Column(String(250), nullable=False)
#     process_status_message = Column(String(50), nullable=False)
#     reg_date = Column(DateTime, nullable=True)
#     reg_by = Column(String(50), nullable=True)
'''


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
# reports.metadata.create_all(bind=engine)
