from typing import Any
from src.services.queue_task.enums import TaskStatus, SupportQueueTask


class BaseOperator:
    def __init__(self, name: str):
        self.status: TaskStatus = TaskStatus.WAITING
        self.task_name: str = name

    async def execute(self, params: dict[str, Any] = None):
        ...


class EmptyOperator(BaseOperator):
    def __init__(self):
        super().__init__(name=SupportQueueTask.EMPTY_TASK)


class QueueTaskMarket:

    @staticmethod
    def _support_queue_task():
        return [queue_task_name for queue_task_name in SupportQueueTask]

    @staticmethod
    def _mapped_queue_task(task_name: str) -> BaseOperator:
        return {
            SupportQueueTask.EMPTY_TASK: EmptyOperator(),
        }.get(task_name)

    def get_process_task(self, task_name: str) -> BaseOperator:
        return self._mapped_queue_task(task_name)
