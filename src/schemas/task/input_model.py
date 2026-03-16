from typing import Any
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, field_validator
from fastapi import status
from fastapi.exceptions import HTTPException
from src.services.queue_task.enums import SupportQueueTask


class QueueTask(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(min_length=3, max_length=25, default=SupportQueueTask.EMPTY_TASK)
    parameter: dict[str, Any] = Field(default_factory=dict)

    @field_validator('name')
    @classmethod
    def validate_support_task(cls, value):
        if value not in SupportQueueTask:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        return value
