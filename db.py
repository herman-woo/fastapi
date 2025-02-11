from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import Depends, FastAPI, HTTPException, Query
from typing import Annotated

# Define the database file
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Create engine and session factory
connect_args = {"check_same_thread": False}  # Needed for SQLite in multi-threaded apps
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]