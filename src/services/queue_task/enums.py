from enum import IntEnum


class TaskStatus(IntEnum):
    WAITING = 0
    QUEUED = 1
    RUNNING = 2
    FINISHED = 3
    FAILED = 4
