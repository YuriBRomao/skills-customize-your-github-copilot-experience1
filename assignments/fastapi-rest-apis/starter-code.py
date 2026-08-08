from typing import Dict

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    # O titulo precisa ter ao menos 1 caractere.
    title: str = Field(min_length=1)
    done: bool = False


class Task(TaskCreate):
    id: int


TASKS: Dict[int, Task] = {}
NEXT_ID = 1


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.get("/tasks")
def list_tasks() -> list[Task]:
    return list(TASKS.values())


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate) -> Task:
    global NEXT_ID

    task = Task(id=NEXT_ID, title=payload.title, done=payload.done)
    TASKS[NEXT_ID] = task
    NEXT_ID += 1
    return task


@app.get("/tasks/{task_id}")
def get_task(task_id: int) -> Task:
    task = TASKS.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    if task_id not in TASKS:
        raise HTTPException(status_code=404, detail="Task not found")

    del TASKS[task_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
