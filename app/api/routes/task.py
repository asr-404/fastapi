from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.task import TaskCreate
from app.database import get_db

router = APIRouter()

@router.post("/tasks/")
def create(task: TaskCreate, db: Session = Depends(get_db)):
    return {"message": "Task received", "data": task}