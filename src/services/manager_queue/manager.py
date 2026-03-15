from asyncio import Queue


class QueueManager:
    def __init__(self, maxsize=10, count_workers=5):
        self.queue: Queue | None = None
        self.maxsize = maxsize
        self.count_workers = count_workers
        self._is_running = False

    async def create_queue(self):
        if not self._is_running:
            self.queue = Queue(maxsize=self.maxsize)
            self._is_running = True

    async def shutdown_queue(self):
        ...

    async def put_task(self, task):
        if self.queue is None:
            raise RuntimeError('Queue is None')
        await self.queue.put(task)


queue_manager = QueueManager()
