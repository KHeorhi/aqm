from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse
from fastapi import status
from src.services.manager_queue import queue_manager
from src.schemas.task.input_model import QueueTask
from src.schemas.task.output_model import NewTaskResponse


router = APIRouter(prefix='/task', tags=['task'])


@router.post('/add_new_task')
async def add_new_task_to_queue(queue_params: QueueTask):
    """Метод предназначен для добавления новой задачи в очередь."""

    await queue_manager.put_task(queue_params)

    message = NewTaskResponse(
        name=queue_params.name,
        id=queue_params.id,
    )
    return JSONResponse(
        status_code=status.HTTP_201_CREATED, content=message.model_dump()
    )


@router.get('/task_status')
async def get_task_status(_task_id: str = Query()):
    """Метод для получения информации о статусе задачи."""


@router.get('/tasks_status')
async def get_list_task_status(_tasks_id: list[str] = Query()):
    """Метод для получения информации о статусе задач."""
