from app.models.task import Task

def create_task(db, task):
    db_task = Task(
        title=task.title,
        description=task.description
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db):
    print(db.query(Task).all())
    return db.query(Task).all()