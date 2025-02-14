# How to Create a FastAPI backend (and other useful commands)
1. Create an ENV 
2. Create a Virtual Python Environment
 - python -m venv .venv
 - source .venv/bin/activate
 - - .\.venv\Scripts\activate
3. Install dependencies 
 - pip install "fastapi[standard]" sqlmodel alembic
 - pip install -r requirements.txt
 - pip freeze > requirements.txt
 - deactivate (if you need to go to another python env)


# FastAPI
1. Architecture
- main.py //entry for the api
- db.py //configuration to setup database sessions

2. Run FastAPI
 - fastapi dev main.
 - uvicorn main:app --host 0.0.0.0 --port 8080

# Spin up a db
need to create sessions. This repository has a db.py and gets called by main.py

## Alembic stuff
1. make migrations, initialize
- alembic init migrations
2. editscript to use your dependencies (sqlmodel)
3. Update the alembic.ini to confugre properly
sqlalchemy.url = sqlite:///./database.db

4. update the env.py in the migrations folder to point to the right db
target_metadata = SQLModel.metadata  # Use SQLModel's metadata


alembic revision --autogenerate -m "Fixed database connection"
alembic upgrade head

