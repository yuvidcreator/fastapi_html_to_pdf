import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Load environment variables from .env file
load_dotenv()

# Get the environment variable
environment = os.getenv("ENVIRONMENT")

# Define the database URL based on the environment
SQLALCHEMY_DATABASE_URL = os.getenv(f"DATABASE_URL_{environment.upper()}")
port = int(os.getenv(f"PORT_{environment.upper()}"))


# Desired maximum connections
max_connections = 10000

# Compute pool_size and max_overflow based on max_connections
pool_size = 10  # You can adjust this as needed
max_overflow = max_connections - pool_size
Base = declarative_base()


# Create Engine for MySQL
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
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


