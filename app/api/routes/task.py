from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.task import TaskCreate
from app.database import get_db
from app.crud import task as crud_task

router = APIRouter()

@router.post("/tasks/")
def create(task: TaskCreate, db: Session = Depends(get_db)):
    return crud_task.create_task(db, task)


@router.get("/")
def read_tasks(db: Session = Depends(get_db)):
    return crud_task.get_tasks(db)