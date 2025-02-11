from fastapi import APIRouter, Depends, HTTPException
from .models import Rater
from .respository import RaterRepository
from db import SessionDep

router = APIRouter()

@router.get("/{rater_id}")
def get_rater(rater_id: int, session: SessionDep):
    repo = RaterRepository(session)
    rater = repo.find_by_id(rater_id)
    if not rater:
        raise HTTPException(status_code=404, detail="Rater not found")
    return rater

@router.get("/")
def get_all_raters(session: SessionDep):
    repo = RaterRepository(session)
    return repo.find_all()

@router.post("/", response_model=Rater)
def create_rater(rater: Rater, session: SessionDep):
    repo = RaterRepository(session)
    return repo.save(rater)

@router.delete("/{rater_id}")
def delete_rater(rater_id: int, session: SessionDep):
    repo = RaterRepository(session)
    success = repo.delete(rater_id)
    if not success:
        raise HTTPException(status_code=404, detail="Rater not found")
    return {"message": "Rater deleted successfully"}
