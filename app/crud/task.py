from app.models.task import Task

def create_task(db, task):
    db_task = Task(title=task.title)
    db.add(db_task)
    db.commit()
    return db_task