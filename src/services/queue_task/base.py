from uuid import uuid4
from src.services.queue_task.enums import TaskStatus


class QueueTask:
    def __init__(self, name: str):
        self.status: TaskStatus = TaskStatus.WAITING
        self.task_id: str = str(uuid4())
        self.task_name: str = name

    def execute(self):
        ...
