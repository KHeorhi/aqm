from asyncio import Queue, create_task, wait_for, TimeoutError
from src.schemas.task.input_model import QueueTask
from src.services.queue_task.base import QueueTaskMarket


class QueueManager:
    def __init__(self, maxsize=10, count_workers=5):
        self.queue: Queue | None = None
        self.order_tasks: list | None = None
        self.maxsize = maxsize
        self.count_workers = count_workers
        self.task_market = QueueTaskMarket()
        self._is_running = False

    async def process_worker(self, _worker_id: int):
        while True:
            task: QueueTask = await self.queue.get()
            try:
                process_task = self.task_market.get_process_task(task_name=task.name)
                await process_task.execute(params=task.parameter)
            except Exception as error:
                print(f'Ошибка при выполнении задачи c id {task.id}: {error}')
            self.queue.task_done()

    async def create_queue(self):
        if not self._is_running:
            self.queue = Queue(maxsize=self.maxsize)
            self._is_running = True
            self.order_tasks = [
                create_task(self.process_worker(_worker_id=worker_id))
                for worker_id in range(self.count_workers)
            ]

    async def shutdown_queue(self):
        """Метод для корректного завершения исполняемых задач."""

        if not self.queue.empty():
            try:
                await wait_for(self.queue.join(), timeout=10)
            except TimeoutError as _timeout_error:
                print(f'Время на завершение задач вышло!')
            finally:
                for task in self.order_tasks:
                    task.cancel()

    async def put_task(self, task: QueueTask):
        """Метод для добавления задачи в очередь."""

        if self.queue is None:
            raise RuntimeError('Queue is None')
        await self.queue.put(task)


queue_manager = QueueManager()
