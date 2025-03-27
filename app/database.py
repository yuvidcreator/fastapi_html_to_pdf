# from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base


# Desired maximum connections
max_connections = 10000

# Compute pool_size and max_overflow based on max_connections
pool_size = 10  # You can adjust this as needed
max_overflow = max_connections - pool_size
Base = declarative_base()

DATABASE_URL = "mysql+pymysql://root:@localhost:3306/testing_pdf_db"

# Create Engine for MySQL
engine = create_engine(
    DATABASE_URL,
    pool_size=pool_size, 
    max_overflow=max_overflow,
    pool_timeout=30,
    pool_recycle=3600,
    pool_pre_ping=True,
    connect_args={
        "init_command": "SET SESSION wait_timeout=2592000"
    }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata = MetaData()
