from enum import IntEnum, StrEnum, auto


class TaskStatus(IntEnum):
    WAITING = 0
    QUEUED = 1
    RUNNING = 2
    FINISHED = 3
    FAILED = 4


class SupportQueueTask(StrEnum):
    EMPTY_TASK = auto()
